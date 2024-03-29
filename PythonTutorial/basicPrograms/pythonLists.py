# Lists are used to store multiple items in a single variable
# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.
exampleList = ["Glass", "Cup", "plate", "Glass"]
print(exampleList)
print(len(exampleList))
# A list can contain different data types:
exampleListTwo = [40, "Syed Hussain", 5.1, 'male']
print(exampleListTwo)
print(exampleListTwo[0])  # access list
print(exampleListTwo[-1])  # Print the last item of the list:
print(exampleListTwo[0:3])  # specify a range of indexes by specifying where to start and where to end the range
if 40 in exampleListTwo:  # Check if value is present in the list:
    print("yes. found it")
else:
    print("sorry better luck next time")
