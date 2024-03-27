Score = [10, 20, 30, 40, 50]
print(Score)
print(Score[0])
print(Score[-1])

print(Score[:])  # new copy of list

# concatenate
print(Score + [1, 2, 3] + ["ABC","tajamul"])

# values are mutable and can be changed at run time
number = [1, 2, 3, 4]
number[2] = 30.33  # based on index changed 3 to 30.33 on index position 2
print(number)

# append
number.append(100)
print(number)

# assigning value in real time
name = ['a', 'b', 'c', 'd', 'e', 'f']
name[2:5] = ['C', 'D', 'E']
print(name)
name[2:5] = []
print(name)
name[:] = []  # removing all values from list
print(name)
name.append([1, 2, 3, 4])  # adding new values now.
print(name)

# nested List
a = ['a', 'b', 'c', 'd']
b = [1, 2, 3, 4, 5, 6]
c = [a, b]
print(c)
print(a[0])
print(b[1])
print(c[0][3])
print(c[1][3])
