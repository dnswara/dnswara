#DISCLAIMER
#so this is my first phyton project. I finsihed it at 5 April 2021 2 days before birthday at 10.19 and im gonna post it on github also my first upload on github so enjoy :)
Calculator = input("\"Danis\" Calculator\n PRESS ENTER -->")
calc = "No"

num1 = float(input("Input the first number: "))
op_number = input("Input the operating sign:")
num2 = float(input("Input the second number:"))

if op_number == "+":
        print(float(num1) + float(num2))


elif op_number == "-":
        print(float(num1) - float(num2))

elif op_number == "*":
        print(float(num1) * float(num2))

elif op_number == "/":
        print(float(num1) / float(num2))

else:
        print("The Operation Seems Not Valid, Please Run The Program Again")

calc = input("Do You Want To Calculate Again? \n Yes Or No : ")

while calc == "Yes":
    num1 = float(input("Input the first number: "))
    op_number = input("Input the operating sign:")
    num2 = float(input("Input the second number:"))

    if op_number == "+":
        print(float(num1) + float(num2))


    elif op_number == "-":
        print(float(num1) - float(num2))

    elif op_number == "*":
        print(float(num1) * float(num2))

    elif op_number == "/":
        print(float(num1) / float(num2))

    else:
        print("The Operation Seems Not Valid, Please Run The Program Again")

    calc = input("Do You Want To Calculate Again? \n Yes Or No : ")

    if num1 != float:
        print("Please Enter A Correct Number")
    if num2 != float:
        print("Please Enter A Correct Number")

while calc == "YES":
    num1 = float(input("Input the first number: "))
    op_number = input("Input the operating sign:")
    num2 = float(input("Input the second number:"))

    if op_number == "+":
        print(float(num1) + float(num2))


    elif op_number == "-":
        print(float(num1) - float(num2))

    elif op_number == "*":
        print(float(num1) * float(num2))

    elif op_number == "/":
        print(float(num1) / float(num2))

    else:
        print("The Operation Seems Not Valid, Please Run The Program Again")

    calc = input("Do You Want To Calculate Again? \n Yes Or No : ")

    if num1 != float:
        print("Please Enter A Correct Number")
    if num2 != float:
        print("Please Enter A Correct Number")

while calc == "yes":
    num1 = float(input("Input the first number: "))
    op_number = input("Input the operating sign:")
    num2 = float(input("Input the second number:"))

    if op_number == "+":
        print(float(num1) + float(num2))


    elif op_number == "-":
        print(float(num1) - float(num2))

    elif op_number == "*":
        print(float(num1) * float(num2))

    elif op_number == "/":
        print(float(num1) / float(num2))

    else:
        print("The Operation Seems Not Valid, Please Run The Program Again")

    calc = input("Do You Want To Calculate Again? \n Yes Or No : ")


if calc == "No":
    print("Thank You For Using The Calculator!")

elif calc == "no":
    print("Thank You For Using The Calculator!")

elif calc == "NO":
    print("Thank You For Using The Calculator!")
else:
     print("Your answer seems not valid, please run the program again")



