# Accept the gender from the user as char and print the respective greeting message
# Good morning Sir of Good morning ma'am

gender = input("Enter you gender (M/F): ")

if gender == "m" or gender == "M":
    print("Good morning sir.")
elif gender == "f" or gender == "F":
    print("Good morning ma'am")
else:
    print("Invalid input!")