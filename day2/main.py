print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
percentage = int(input("What percentage bill would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
bill_for_each_man = round( (total_bill / number_of_people) * (percentage / 100 + 1), 2)

print(f"Each person should pay: ${bill_for_each_man}")