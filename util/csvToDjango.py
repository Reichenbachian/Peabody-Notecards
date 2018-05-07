from dashboard.models import *
import csv
import pdb
from tqdm import tqdm
with open("../april15_sc.csv") as f:
    reader = csv.reader(f)
    has_read = False
    for row in tqdm(reader):
        if not has_read:
            has_read = True # skip first row
            continue
        try:
            _, created = Entry.objects.get_or_create(
                catNumber=int(''.join(x for x in str(row[4].decode('ascii', errors='ignore').encode('ascii')) if x.isdigit())),
                accNum=int(''.join(x for x in str(row[11].decode('ascii', errors='ignore').encode('ascii')) if x.isdigit())),
                name=str(row[2].decode('ascii', errors='ignore').encode('ascii')),
                site=str(row[7].decode('ascii', errors='ignore').encode('ascii')),
                siteNumber=str(row[6].decode('ascii', errors='ignore').encode('ascii')),
                locality=str(row[3].decode('ascii', errors='ignore').encode('ascii')),
                situation=str(row[5].decode('ascii', errors='ignore').encode('ascii')),
                fileName=str(row[12].decode('ascii', errors='ignore').encode('ascii')),
                remarks=str(row[9].decode('ascii', errors='ignore').encode('ascii'))
                )
        except:
            pass
