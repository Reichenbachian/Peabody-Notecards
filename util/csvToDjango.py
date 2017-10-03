# Clear db first if people didnt edit: email taylor to check

from dashboard.models import *
import csv
with open("../test4.csv") as f:
    reader = csv.reader(f)
    has_read = False
    for row in reader:
        if not has_read:
            has_read = True # skip first row
            continue
        _, created = Entry.objects.get_or_create(
            catNumber=str(row[2].decode('ascii', errors='ignore').encode('ascii')),
            accNum=str(row[8].decode('ascii', errors='ignore').encode('ascii')),
            name=str(row[6].decode('ascii', errors='ignore').encode('ascii')),
            site=str(row[5].decode('ascii', errors='ignore').encode('ascii')),
            siteNumber=str(row[3].decode('ascii', errors='ignore').encode('ascii')),
            locality=str(row[4].decode('ascii', errors='ignore').encode('ascii')),
            situation=str(row[7].decode('ascii', errors='ignore').encode('ascii')),
            fileName=str(row[9].decode('ascii', errors='ignore').encode('ascii'))
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
