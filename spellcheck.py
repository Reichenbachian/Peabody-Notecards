"""Given a sentence, return a spell-checked version, with the desired corpus of words sorted by
frequency."""

import re

from bk_tree import BKTree

tree = BKTree.read_words_from_file("spellcheckcorpus.dat")

# now get frequency data
frequencies = {}
with open("spellcheckcorpuswithfreqs.csv", 'r') as infile:
    for line in infile:
        word, freq = line.strip().split(',')
        frequencies[word] = int(freq)



REGEX_REPLACEMENTS = [["(\w)[£€]", "\1e"],
                      ["[£€](\w)", "e\1"],
                      ["(\w)5", "\1s"],
                      ["5(\w)", "s\1"]]

# now to spell-check a single word, we find its closest thing (within the parameter PRECISION) and
# then use a less-precise match if it's a lot more commmon (
PRECISION = 1  # set to 0 to use the closest match regardless of commonality
def correct(input_word):
    """Returns the closest words in the list of words we have, sorted by likelihood."""
    for pattern, substitution in REGEX_REPLACEMENTS:
        processed = re.sub(pattern, substitution, input_word)

    curr_distance = 0
    while len(tree.query(input_word, curr_distance)) == 0:  # no matches, decrease precision
        curr_distance += 1

    # now curr_distance is the distance from the shortest match, so add "wiggle room"
    matches = tree.query(input_word, curr_distance + PRECISION)
    return max(matches, key=lambda w: frequencies.get(w, 1) / ((tree.levenshtein(w, input_word) + 1) ** 4))

def sentence_correct(input_sentence):
    """Returns a new corrected sentence, being sensitive to punctuation."""
    corrected = input_sentence.strip()
    ENDING_PUNCTUATION = "?!."
    if corrected[-1] in ENDING_PUNCTUATION: # this will be added back later
        ending_mark = corrected[-1]
    else:  # just assume the sentence ends with a normal word
        ending_mark = ""

    corrected = corrected.split(' ')  # perhaps there's edge cases this misses?

    # anything that should be preserved at word boundaries
    # specific to side: the start only has quotes and starting brackets
    # but the end can have a much wider range of things
    WORD_STARTING_PUNCTUATION = "\"'(["  
    WORD_ENDING_PUNCTUATION = "-:;\"')]."
    ALL_WORD_PUNCTUATION = WORD_STARTING_PUNCTUATION + WORD_ENDING_PUNCTUATION
    corrected_words = []
    # preserves the above punctuation only at word boundaries
    for word in corrected:
        # the below makes two lists of ending and starting punctuation to be kept
        if all([c not in word for c in ALL_WORD_PUNCTUATION]):  # no need to mess with symbols
            start_punc = []
            end_punc = []
        else:  # fix the punctuation
            start_punc = []
            i = 0
            while word[i] in WORD_STARTING_PUNCTUATION and i < len(word):
                start_punc.append(word[i])
                i += 1
                # remove those from the word: they'll mess up correction, and we stored them
            word = word[i:] if i < len(word) else word
            # now go from the end backwards to grab those marks
            end_punc = []
            i = -1
            while word[i] in WORD_ENDING_PUNCTUATION and i >= -len(word):
                end_punc.append(word[i])
                i -= 1

            # same thing: remove it once we have it stored
            if i == -1:
                pass  # doing word[:-1] removes a letter
            else:
                word = word[:i+1] if i >= -len(word) else word

        # now, we finally just correct it and add to the list, punctuation added back
        corrected_words.append(''.join(start_punc) + correct(word) + ''.join(end_punc))

    return ' '.join(corrected_words)


def save_corpus(words, corpusfile="spellcheckcorpus.dat", freqsfile="spellcheckcorpuswithfreqs.csv"):
    """Writes the corpus to the file, as well as the frequency values."""
    with open(corpusfile, 'w') as outfile:
        with open(freqsfile, 'w') as freqsfile:
            for word in sorted(words, key=lambda w: frequencies.get(w, 1), reverse=True):
                outfile.write(word + '\n')
                freqsfile.write("{},{}\n".format(word, frequencies.get(w, 1)))


def add_word(word, bump_up_by=30):
    """Adds a word to the spellcheck corpus. If already present, bumps it up a specified number of
    places."""
    BKTree.add(word)
    if word in words:
        frequencies[word] += bump_up_by
    else:
        words.append(word)
        frequencies[word] = 1


print(sentence_correct("Name urude quartzite stone."))
