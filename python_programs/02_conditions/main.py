# Accept 2 numbers and print the greatest between them

num1 = int(input("First number: "))
num2 = int(input("Second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}!")
elif num2 > num1:
    print(f"{num2} is greater than {num1}!")
else: 
    print(f"{num1} is equal to {num2}!")

