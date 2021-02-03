class students(object):
    _count = 0

    def __init__(self, Student_ID, Student_First_Name, Student_Last_Name, Course, Year,
                 GPA,
                 University,
                 Email,
                 Mobile):
        Student_ID = self.Student_ID
        Student_First_Name = self.Student_First_Name
        Student_Last_Name = self.Student_Last_Name
        Course = self.Course
        Year = self.Year
        GPA = self.GPA
        University = self.University
        Email = self.Email
        Mobile = self.Mobile
        _count += 1

    def getinstancescount():
        return _count
