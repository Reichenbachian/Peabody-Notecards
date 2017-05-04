from dashboard.models import *
import csv
with open("/Users/localhost/Desktop/Projects/Working/PeabodyNotecards/test.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Entry.objects.get_or_create(
            catNumber=row[1],
            siteNumber=row[2],
            locality=row[3],
            site=row[4],
            name=row[5],
            situation=row[6],
            accNum=row[7],
            fileName=row[8]
            )

    # i = 0
    # for row in reader:
    #     print("catNumber", row[1])
    #     print("siteNumber", row[2])
    #     print("locality", row[3])
    #     print("site", row[4])
    #     print("name", row[5])
    #     print("situation", row[6])
    #     print("accNum", row[7])
    #     print("fileName", row[8])
    #     print("---------------------")
    #     if i > 3:
    #         break
    #     i+=1