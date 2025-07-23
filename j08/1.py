i = 20

a = 5
while a > 0:
    g = int(input("hads e khood ra vared konid: "))
    if g > i:
        print("adad e entekhabi bozorgtar az adad e dorost ast")
    elif g < i:
        print("adad e entekhabi kocektar az adad e dorost ast")
    else:
        print("bordi")
        break
    a = a - 1
else:
    print("bakhti")