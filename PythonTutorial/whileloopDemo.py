# while Loop
a = 0
while (a < 4):
    # print("Hello pyhton")
    print(a + 1)
    a = a + 1

print("------------")

num = 0
while (num < 3):
    print("Hello Tajamul")
    num = num + 1
else:
    print("bye Tajamul")

print("------------")
# for loop
Languages = ["Java", "phython", "dot net", "c sharp"]  # list
for i in Languages:
    print(i)

print("------------")
string = "Syed tajamul Hussain"
for i in string:
    print(i)

print("------------")
list = ["Syed", "Tajamul", "Hussain"]
for index in range(len(list)):
    print(list[index])
    name = list[0]
    print(name)

print("------------")
# for loop with else
countrylist = ["India", "Pakistan", "srilanka", "China"]
for index in range(len(countrylist)):
    print(countrylist[index])
else:
    print("countrylist is over")

print("------------")
citylist = ["India", "Pakistan", "srilanka", "China"]
for index in range(2):
    print(citylist[index])
else:
    print("citylist is over")

print("------------")
# nested loop to print a pattern
for i in range(1, 5):
    for j in range(i):
        print(i, end='')
    print()
