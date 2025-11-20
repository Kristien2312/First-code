print ("Welcome to My Python Code")
savings = input("How much money did you save for the future this month? ")
# Attempt to collect data from the user
try:
    savings = float(savings)
except ValueError:
    print("Please enter a valid number. ")
    savings = input("How much money did you save for the future this month? ")   
    savings = float(savings)
# A fail safe, incase the user types in a invalid input
savings_year = savings * 12
print(f"You are on pace to save ${savings_year} this year. ")
# Math to see how much money the user will save over a years span if they save that same amount each month