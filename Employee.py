class Employee:
    def __init__(self):
        self.__name=" "
        self.__salary=0.0
        self.__age=0
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_salary(self,salary):
        if salary>0:
            self.__salary=float(salary)
        else:
            print("Error: The salary should be greater than 0.")
    def get_salary(self):
        return self.__salary
    def set_age(self,age):
        if age>=18 and age<=100:
            self.__age=age
        else:
            print("Error: The age should be between 18 and 100.")
    def get_age(self):
        return self.__age

e1=Employee()
e1.set_name("Geeth")
e1.set_salary(50000)
e1.set_age(30)
print(f"Employee name: {e1.get_name()}")
print(f"Employee salary: {e1.get_salary()}")
print(f"Employee age: {e1.get_age()}")
e1.set_salary(-20)
