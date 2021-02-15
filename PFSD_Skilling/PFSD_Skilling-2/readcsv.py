import csv
f = open('attendance.csv', 'rt')
reader = csv.reader(f)
for row in reader:
    print(row)
