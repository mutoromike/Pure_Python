
import csv

with open('medical_data_small.tsv', 'r') as f:
    # reader = csv.reader(f, delimiter='\t')
    reader = csv.DictReader(f, dialect='excel-tab')
    # readr = csv.DictReader(open(reader, 'rb'))
    # decode = {r[0]: r[1] r[3], r[4], r[5], r[6], r[7], r[8] for r in reader}
    for r in reader:
        # z = {}
        print(r)



def compute_abs(a, b):

    if (a > b):
        res = a - b
    else:
        res = b - a

    return res
