lst = [1, 2, 3]
lst[1] = "ali"

t = (1, 2, 3)
# t[1] = "ali"
l = list(t)
l[1] = "ali"
t = tuple(l)
print(t)