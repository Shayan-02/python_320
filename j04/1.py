naam = input("enter your firstname: ")
naam_khanevadegi = input("enter your lastname: ")
sen = input("enter your age: ")
kodemelli = input("enter your personal ID: ")

print("your firstname is:", naam, "\nyour lastname is:", naam_khanevadegi, "\nyour fullname is:", naam, naam_khanevadegi, "\nyour age is:", sen, "years old")

print("---------------------------------")


print(f"your firstname is: {naam} \nyour lastname is: {naam_khanevadegi}\nyour fullname is: {naam} {naam_khanevadegi}\nyour age is: {sen} years old\nyour personal ID is {kodemelli}")

print("=================================")

print("your firstname is: {} \nyour lastname is: {}\nyour fullname is: {} {}\nyour age is: {} years old".format(naam, naam_khanevadegi, naam, naam_khanevadegi, sen))