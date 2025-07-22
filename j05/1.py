num1 = int(input("enter number1: "))
op = input("enter an operator: ")
num2 = int(input("enter number2: "))

if op == "+": print(num1+num2)
elif op == "-": print(num1-num2)
elif op == "*": print(num1*num2)
elif op == "/":
    if num2 == 0: print("error")
    else: print(num1/num2)
else: print("amalgar ghalateh")

