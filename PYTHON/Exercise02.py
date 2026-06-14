
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def get_marks(self):
#         return self.marks
#     def calculate_results(self):
#         return self.marks
#     def get_grade(self):
#         marks=self.calculate_result()
#         if marks>=90:
#             return "A"
#         elif marks >= 75:
#             return "B"
#         elif marks >=50:
#             return "C"
#         else:
#             return "Fail"
#     def __add__(self,other):
#         return self.calculate_result()+other.calculate_result()
#     def __gt__(self,other):
#         return self.calculate_result()>other.calculate_result()
#     def __str__(self):
#         return f"{self.name} scored {self.calculate_result()}"
        
# class SportsStudent(Student):
#     def __init__(self,name,marks,bonus):
#         super().__init__(name,marks)
#         self.bonus = bonus
#     def calculate_result(self):
#         return self.get_marks() + bonus()
        
# class RegularStudent(Student):
#     def calculate_result(self):
#         return self.get_marks()
# StudentsCount= int(input())
# Students=[]
# for i in range(StudentsCount):
#      Data = input().split()
    
#      if (len(Data)==4):
#         StudentType,Studentname,marks,bonus=Data
#         Students.append(SportsStudent(Studentname,int(marks), int(bonus)))
#      elif (len(Data)==3):
#           StudentType,Studentname,marks=Data
#           Students.append(RegularStudent(Studentname,int(marks)))
         
# for s in Students:
#     print(f"{s.name} Final Marks: {s.calculate_result()} Grade:{s.get_grade()}")
    
#     Students.sort(key=lambda x: x.calculate_result(),reverse=True)
#     print("/nRanking:")
# for i , s in enumerate(Students,1):
#     print(f"{i}. {s.name}")
    
# if len(Students)>=2:
#     print("\nTotal Marks : ",Students[0]+Students[1])
#     if Students[0]>Students[1]:
#         print(f"{Students[0].name} has higher marks")
#     else :
#         print(f"{Student[1].name} has higher marks")    

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


StudentsCount = int(input())
Students = []

for i in range(StudentsCount):

    Data = input().split()

    if len(Data) == 4:
        StudentType, Studentname, marks, bonus = Data
        Students.append(
            SportsStudent(
                Studentname,
                int(marks),
                int(bonus)
            )
        )

    elif len(Data) == 3:
        StudentType, Studentname, marks = Data
        Students.append(
            RegularStudent(
                Studentname,
                int(marks)
            )
        )

# Display details
for s in Students:
    print(f"{s.name} Final Marks: {s.calculate_result()} Grade: {s.get_grade()}")

# Ranking
Students.sort(key=lambda x: x.calculate_result(), reverse=True)

print("\nRanking:")

for i, s in enumerate(Students, 1):
    print(f"{i}. {s.name}")

# Total marks and comparison
if len(Students) >= 2:

    print("\nTotal Marks:", Students[0] + Students[1])

    if Students[0] > Students[1]:
        print(f"{Students[0].name} has higher marks")
    else:
        print(f"{Students[1].name} has higher marks")