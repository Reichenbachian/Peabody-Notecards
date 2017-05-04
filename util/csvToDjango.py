from dashboard.models import *
import csv
with open("/Users/localhost/Desktop/Projects/Working/PeabodyNotecards/test2.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Entry.objects.get_or_create(
            catNumber=row[2],
            siteNumber=row[3],
            locality=row[4],
            site=row[5],
            name=row[6],
            situation=row[7],
            accNum=row[8],
            fileName=row[9]
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