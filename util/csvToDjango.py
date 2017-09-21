from dashboard.models import *
import csv
with open("/home/greichenbach/peabody/test3.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        _, created = Entry.objects.get_or_create(
            catNumber=str(row[2].encode('ascii', errors='ignore').decode('ascii')),
            siteNumber=str(row[3].encode('ascii', errors='ignore').decode('ascii')),
            locality=str(row[4].encode('ascii', errors='ignore').decode('ascii')),
            site=str(row[5].encode('ascii', errors='ignore').decode('ascii')),
            name=str(row[6].encode('ascii', errors='ignore').decode('ascii')),
            situation=str(row[7].encode('ascii', errors='ignore').decode('ascii')),
            accNum=str(row[8].encode('ascii', errors='ignore').decode('ascii')),
            fileName=str(row[9].encode('ascii', errors='ignore').decode('ascii'))
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
