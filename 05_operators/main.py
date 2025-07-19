# 05_operators

# 1. Arithmetic Operators
a = 10
b = 5

print("----------Arithmetic Operators----------")
print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multuplication: {a * b}")
print(f"Division: {a / b}")
print(f"Modulus: {b % a}")
print(f"Exponentiation: {a ** b}")
print(f"Floor Division: {a // b}")

# 2. Assignment Operators
x = 10
x += 10
x -= 5
print("----------Assignment Operators----------")
print(x)

# 3. Comparison Operators
c = 10
d = 10

print("----------Comparison Operators----------")
print(c == d)
print(c != d)
print(10 > 3)
print(10 < 3)
print(c <= d)
print(c >= d)

# 4. Logical Operators
print("----------Logical Operators----------")
print(123 > 100 and 30 == 30)
print(123 > 100 and 30 > 30)
print(123 > 100 or 30 > 30)
print(not(4 > 2))
print(not(4 < 2))