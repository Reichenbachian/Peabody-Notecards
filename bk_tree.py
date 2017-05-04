"""This file uses Burkhard-Keller trees to efficiently compute approximate string matches from a
dictionary."""


import numpy as np


class BKTree:
    """A Burkhard-Keller tree."""
    def __init__(self, wordlist):
        """Given a list of words, forms a BK Tree. Wordlist cannot be empty."""
        if not wordlist:
            raise ValueError("Wordlist must not be empty!")
        self.root = (wordlist[0], [])
        for word in wordlist:
            self.add(word)

    def add(self, word):
        """Adds a word to the BK-tree."""
        curr_node = self.root
        curr_d = self.levenshtein(curr_node[0], word)
        if curr_d == 0:  # nothing to do
            return None
        # otherwise, find the next child to recurse to
        while curr_d <= len(curr_node[1]) and curr_node[1][curr_d-1] is not None:
            curr_node = curr_node[1][curr_d-1]
            curr_d = self.levenshtein(curr_node[0], word)

        # now that we reached a new spot, add the word
        while len(curr_node[1]) <= curr_d:
            curr_node[1].append(None)  # filler
        curr_node[1][curr_d-1] = (word, [])


    def query(self, target, n):
        """Target is the string to fuzzy-match. n is the desired maximum distance to vary. Returns a
        list, sorted by closest-first but besides that unordered, of the words that fit the
        criteria."""
        curr_nodes = [self.root]  # unlike add, we have branching recursrion
        matches = []
        while curr_nodes:  # still things to branch
            new_nodes = []
            for node in curr_nodes:  # branch here
                d = self.levenshtein(node[0], target)
                if d <= n:  # add the node itself
                    matches.append(node[0])

                # now, branch by getting every extant subtree with distances between d-n and d+n
                low = max(0, d-n-1)
                high = min(len(node[0]), d+n)
                new_nodes += [n for n in node[1][low:high] if n is not None]
            curr_nodes = new_nodes

        matches.sort(key=lambda w: self.levenshtein(w, target))
        return matches


    def save_words(self, filename):
        """Saves the BK-Tree's words in a list to a file. DOES NOT save the tree's exact structure,
        just the words it has in it."""
        with open(filename, 'w') as outfile:
            # recursively go through the tree
            branches = [self.root]
            while branches:
                new_branches = []
                for branch in branches:
                    outfile.write(branch[0] + '\n')
                    new_branches += branch[1]

    @classmethod
    def read_words_from_file(cls, filename):
        """Reads in a newline-separated list of words and creates a BK-tree."""
        with open(filename, 'r') as infile:
            wordlist = [line.strip() for line in infile]
        return cls(wordlist)

    @staticmethod
    # algorithm for computing edit distance
    # Good artists copy, great artists steal
    # this is from https://en.wikibooks.org/wiki/Algorithm_Implementation/Strings/Levenshtein_distance#Python
    # and I take no credit for it whatsoever
    def levenshtein(source, target):
        if len(source) < len(target):
            return BKTree.levenshtein(target, source)
        
        # So now we have len(source) >= len(target).
        if len(target) == 0:
            return len(source)

        # We call tuple() to force strings to be used as sequences
        # ('c', 'a', 't', 's') - numpy uses them as values by default.
        source = np.array(tuple(source))
        target = np.array(tuple(target))

        # We use a dynamic programming algorithm, but with the
        # added optimization that we only need the last two rows
        # of the matrix.
        previous_row = np.arange(target.size + 1)
        for s in source:
            # Insertion (target grows longer than source):
            current_row = previous_row + 1
            
            # Substitution or matching:
            # Target and source items are aligned, and either
            # are different (cost of 1), or are the same (cost of 0).
            current_row[1:] = np.minimum(
                current_row[1:],
                np.add(previous_row[:-1], target != s))
            
            # Deletion (target grows shorter than source):
            current_row[1:] = np.minimum(
                current_row[1:],
                current_row[0:-1] + 1)
            
            previous_row = current_row
            
        return previous_row[-1]
