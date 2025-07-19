# 03_strings

varA = 65
print(chr(varA))
print(ord("A"))

a = "Hello, World!"
print(a[1])     # positive indexing
print(a[-2])    # negative indexing

# string length
str1 = "Beerus"
print(len(str1))

# check if string is present or not
txt = "Python is easy to learn"
print("easy" in txt)
print("easy" not in txt)

# slicing
str2 = "Python Coder"
print(str2[0:6:1])
print(str2[0:6:2])  # this will skip the alternate characters till the 6th index (excluded)

# slicing from start
print(str2[:6])

# slicing to the end
print(str2[7:])

# modify strings
someStr = "Hello Bro!"

print(someStr.upper())  # uppercase
print(someStr.lower())  # lowercase

# remove white space
strWhiteSpace = "   Hello Broooo!    "
print(strWhiteSpace.strip())
