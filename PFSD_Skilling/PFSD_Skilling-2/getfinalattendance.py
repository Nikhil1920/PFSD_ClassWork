import csv
f = open("FinalAttendence.csv", "w", newline="")
writer = csv.writer(f)
f1 = open("attendance.csv", "r")
reader = csv.reader(f1)
c = 0
for row in reader:
    if(c == 0):
        writer.writerow(row+["AttendencePercentage"])
        c += 1
    else:
        p = int((int(row[7])/int(row[6]))*100)
        p = str(p)+"%"
        print(row[0], p)
        writer.writerow(row+[p])
