class students(object):
    _count = 0

    def __init__(self, Student_ID, Student_First_Name, Student_Last_Name, Course, Year,
                 GPA,
                 University,
                 Mobile):
        self.Student_ID = Student_ID
        self.Student_First_Name = Student_First_Name
        self.Student_Last_Name = Student_Last_Name
        self.Course = Course
        self.Year = Year
        self.GPA = GPA
        self.University = University
        self.Mobile = Mobile
        students._count += 1

    def getInstances(self):
        print("The class is initialised "+_count+"times")

    def mail(self):
        Email = self.Student_First_Name+self.Student_Last_Name+"@kluniversity.in"
        return Email


student1 = students(190031920, "NikhilReddy", "A", "cse",
                    "2nd year", 9.0, "KlUniversity", 987654321)
student2 = students(190031943, "Kishan", "A", "cse",
                    "2nd year", 9.5, "KlUniversity", 8456321844)
print(student1.Student_ID, student1.Student_First_Name, student1.Student_Last_Name, student1.Course,
      student1.Year, student1.GPA, student1.University, student1.Mobile, student1.mail())
print(student2.Student_ID, student2.Student_First_Name, student2.Student_Last_Name, student2.Course,
      student2.Year, student2.GPA, student2.University, student2.Mobile, student2.mail())
