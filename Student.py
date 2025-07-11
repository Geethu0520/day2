class Student:
    def __init__(self):
        self.__name=" "
        self.__marks=0
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_marks(self,marks):
        if marks>0 and marks<100:
            self.__marks=marks
        else:
            print("Error: Marks should be between 0 and 100")
    def get_marks(self):
        return self.__marks

s1=Student()
s1.set_name("Geeth")
s1.set_marks(90)
print(f"Student name: {s1.get_name()}")
print(f"Student marks: {s1.get_marks()}")
s1.set_marks(105)
print(f"Student marks (after valid input): ",s1.get_marks())


s1.set_marks(80)