#!/usr/bin/env python

# Use the songs.csv file to generate the songbook_2017.txt file


import csv

rows = {}
with open('songs.csv', newline='') as csvfile:
    o2017 = open("Songbook_2017.txt", 'w')
    o2012 = open("Songbook_2012.txt", 'w')
    n1990 = open("The_Next_To_Come_In_1990.txt", 'w')
    reader = csv.DictReader(csvfile)
    for row in reader:
#        print(row['FileName'])
        if row['2017 Songbook'] == "Y" and row['VC Choice'] == "Y":
            o2017.write(row['FileName'] + "\n")
        if row['2012 Songbook'] == "Y" and row['VC Choice'] == "Y":
            o2012.write(row['FileName'] + "\n")
        if row['Next 1990'] == "Y" and row['VC Choice'] == "Y":
            n1990.write(row['FileName'] + "\n")

