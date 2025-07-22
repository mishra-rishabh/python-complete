# 07_loops

# for loop
for i in range(0, 5, 1):
    print(i)

print("-----------------------------------")

for i in range(5):
    print(i)

print("-----------------------------------")

# print in reverse
for i in range(5, 0, -1):
    print(i)

print("-----------------------------------")

# print negative numbers
for i in range(-5, -11, -1):
    print(i)

print("-----------------------------------")

# print table of 5
for i in range(5, 51, 5):
    print(i)

print("-----------------------------------")

# looping through strings
a = "Hello"

for i in range(len(a)):
    print(a[i])

print("-----------------------------------")

# looping through string: method 2
for i in a:
    print(i)

print("-----------------------------------")

# break statement
for i in range(1, 6):
    if (i == 3):
        break
    else:
        print(i)

print("-----------------------------------")

# continue statement
for i in range(1, 6):
    if (i == 3):
        continue
    else:
        print(i)

print("-----------------------------------")
    
# else statement with for loop
for i in range(6):
    if i == 7:
        break
    print(i)
else:
    print("Finally finished!")