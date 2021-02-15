import csv
f = open('attendance.csv', 'r')
reader = csv.reader(f)
next(reader)
ID = input("Enter student ID:\n")
Name = input("Enter studentname:\n")
for line in reader:
    if(ID == line[0] and Name == line[1]):
        print("ID:", line[0], "Name:", line[1], "Year:", line[2], "Section:", line[3], "Coursecode:", line[4], "Subject:",
              line[5], "NumberOfClassesConducted:", line[6], "NumberOfClassesPresent:", line[7], "NumberOfClassesAbsent:", line[8])
        break
