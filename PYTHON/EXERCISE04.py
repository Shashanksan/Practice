class DataError(Exception):
    pass


class MarksError(Exception):
    pass


class Student:
    def __init__(self, name, marks):
        self.__name = name
        self.__marks = marks

    def validate(self):
        if self.__name.strip() == "":
            raise DataError("Data Error: Student name is missing")

        if self.__marks < 0 or self.__marks > 100:
            raise MarksError("Marks Error: Marks must be between 0 and 100")

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 75:
            return "B"
        elif self.__marks >= 50:
            return "C"
        else:
            return "Fail"

    def get_name(self):
        return self.__name


try:
    name = input()
    marks = int(input())

    student = Student(name, marks)
    student.validate()

    print(f"{student.get_name()} got grade: {student.grade()}")

except DataError as e:
    print(e)

except MarksError as e:
    print(e)