x = int(input("Please enter the value of X"))
if x < 0:
    print("X is a negarive number")
elif x > 0:
    print("X is a positive nubmber")
elif x == 0:
    print("x is equal to zero")
else:
    print("undefined")

# write a program to find the highest number

a = 100
b = 20
c = 30
if a > b and a > c:
    print("a is the highest number")
elif b > c:
    print("b is the highest number")
else:
    print("C is the  highest number")

total = int(input("Enter the total amount"))
if total < 100:
    total = total + 20
elif 100 < total < 500:
    total = total + 50
else:
    total = total + 100
    print(total)
    print("Total =" + str(total))
    print(f'{"total value ="}{total}')
