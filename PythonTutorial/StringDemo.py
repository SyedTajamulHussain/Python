Name = "Syed Tajamul"
designation = "QA"
Age = 38
print(Name,designation,Age)
print(Name[0:3])

print("Hellow \n world")  #Next line
print("Hellow \t world") # tab space

print(Name*5) # printing same string multiple times
print("Syed" in Name)
print("Syed" not in Name)
print("My Name is %s and My age is %d" %("Tajamul" ,38))
s1 ='''hi my name is hussain.
i work with empirix sogtware solutions , my skills 
are JAVA,Phthon , Selenium'''
print(s1)
s2= 'hi i\'m hussain'
print (s2)
s3 = "Hi i am learning \"PHYTHON\" and i am enjoying it"
print (s3)

str = "i Am New To phython but i am loving phython"
print(str.capitalize()) # made one letter capital
print(str.count("phython")) # gave me count of phython word in string
print(str.find("new"))  # give me index of new word in string
print(len(str)) # gives the length of string
print(str.lower()) # makes whole string in lower case.

str1 = '  Test  '
print(str1.lstrip())  # this method will remove left side space
print(str1.rstrip()) # this method will remove right side space

str2="Abc"
print(max(str2)) # this will print higest character in the string
print(min(str2)) # this will print lowest character in the string
str2="Hi this tom signing off"
print(str2.replace("Hi" , "Bye")) # this method will replace hi to bye

str3 = "JAVA_PHTHON_JAVASCRIPT_Selenium" # spliting the string and saving in the object.
str4 = str3.split("_")
print(str4)
str5=str4[0]
print(str5)
print(str3.upper()) # this will convert whole string to upper case

str6 = 'PHYTHON'
print(str6[6])
print(str6[-1])

a='test'  # string comparision
b='tes1'
print(a is b)
print(a==b)