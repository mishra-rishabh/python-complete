# weight converter

weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds ? (K or L): ")

if unit == "K" or unit == "k":
    weight *= 2.205
    unit = "Lbs"
    print(f"Your weight is {round(weight, 3)} {unit}")
elif unit == "L" or unit == "l":
    weight = weight / 2.205
    unit = "Kgs"
    print(f"Your weight is {round(weight, 3)} {unit}")
else:
    print("invalid unit!")
