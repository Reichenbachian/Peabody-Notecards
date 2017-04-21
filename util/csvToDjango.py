with open("/Users/localhost/Desktop/Projects/Working/PeabodyNotecards/test.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Entry.objects.get_or_create(
            catNumber=row[0],
            siteNumber=row[1],
            locality=row[2],
            site=row[3],
            name=row[4],
            situation=row[5]
            )