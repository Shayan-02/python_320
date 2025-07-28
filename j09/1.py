import random

start = int(input("enter a number: "))
end = int(input("enter a number: "))

c = random.randint(start, end)

for i in range(5):
    a = int(input("hads: "))
    if a == c:
        print("bordi")
        break
    elif a > c:
        print("bozorg")
    else:
        print("koochak")
else:
    print("bakhti")