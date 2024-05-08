# Calculating the how each person will pay the bill splitted by people

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tips = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill?"))
each = (total_bill * ((tips / 100) + 1)) / people

print(f"Each person should pay: ${round(each, 2)}")