class School:
    def __init__(self, classroom, playground):
        self.playground = playground   # Public
        self.__classroom = classroom # Private

    def attend_sports_playground(self):
        print(self.playground)

    def subscribe_school_class(self):
        self.__school_private_class()

    def school_class(self,is_school_student):
        if is_school_student == True:
            print(self.__classroom)
        else:
            print("You are not authorized")

    def __school_private_class(self):
        print("Private school class, can be accessed by only school students")

student = School(801,"Football ground")

student.attend_sports_playground()
print(student.playground)
student.school_class(False)
student.school_class(True)

student.subscribe_school_class()   # accesing private method by