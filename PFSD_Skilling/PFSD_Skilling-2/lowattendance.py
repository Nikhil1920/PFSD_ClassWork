import csv
f = open('FinalAttendence.csv', 'r')
reader = csv.reader(f)
next(reader)
for row in reader:
    if(row[9] < "60%"):
        print(row)
