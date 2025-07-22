num = int(input("enter to fizbazz: "))

if num % 15 == 0:
    print("fizbazz")
elif num % 5 == 0:
    print("bazz")
elif num % 3 == 0:
    print("fiz")
else:
    print(num)