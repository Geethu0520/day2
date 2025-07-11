class Calculator:

    #Addition of two numbers
    def addition(self,a,b):
        add=a+b
        print(f"Addition({a}+{b}): {add}")

    #Subtraction of two numbers
    def subtraction(self,a,b):
        sub=a-b
        print(f"Subtraction({a}-{b}): {sub}")

    #Multiplication of two numbers
    def multiplication(self,a,b):
        mul=a*b
        print(f"Multiplication({a}*{b}): {mul}")

    #Division of two numbers
    def division(self,a,b):
        try:
            div=a/b
            print(f"Division({a}/{b}): {div}")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")


c=Calculator()
c.addition(10,20)
c.subtraction(20,10)
c.multiplication(10,20)
c.division(10,5)
c.division(20,0)


