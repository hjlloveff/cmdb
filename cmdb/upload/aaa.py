#!/usr/bin/python
import csv
with open('deb5737e-7659-11e9-8101-000c29717c28.csv',encoding='utf-8') as f:
    f_csv = csv.reader(f)
    for row in f_csv:
        print(row[1])
