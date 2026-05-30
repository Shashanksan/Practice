class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

    def calculate_result(self):
        return self.marks

    def get_grade(self):
        marks = self.calculate_result()
        if marks >= 90:
            return "A"
        elif marks >= 75:
            return "B"
        elif marks >= 50:
            return "C"
        else:
            return "Fail"

    def __add__(self, other):
        return self.calculate_result() + other.calculate_result()

    def __gt__(self, other):
        return self.calculate_result() > other.calculate_result()

    def __str__(self):
        return f"{self.name} scored {self.calculate_result()}"


class SportsStudent(Student):
    def __init__(self, name, marks, bonus):
        super().__init__(name, marks)
        self.bonus = bonus

    def calculate_result(self):
        return self.get_marks() + self.bonus


class RegularStudent(Student):
    def calculate_result(self):
        return self.get_marks()

StudentsCount =int(input())
Students=[]
for i in range(StudentsCount):
    Studentname,marks,bonus,StudentType=input().split()
    if StudentType=="SportsStudent":
        Students.append(SportsStudent(Studentname,marks,bonus))
    elif StudentType=="RegularStudent":
        Students.append(RegularStudent(Studentname,marks))
    
# # Objects
# s1 = SportsStudent("Radhika", 80, 10)
# s2 = RegularStudent("Rahul", 85)
# s3 = RegularStudent("Anjali", 60)
# students = [s1, s2, s3]

# Display details
for s in Students:
    print(f"{s.name} Final Marks: {s.calculate_result()} Grade: {s.get_grade()}")

# Ranking
Students.sort(key=lambda x: x.calculate_result(), reverse=True)
print("\nRanking:")
for i, s in enumerate(Students, 1):
    print(f"{i}. {s.name}")

# Operator overloading
print("\nTotal Marks:", s1 + s2)
if s1 > s2:
    print(s1.name, "has higher marks")
else:
    print(s2.name, "has higher marks")
