print ("Welcome to My Python Code")
savings = input ("How much money did you save this month? ")
savings_year = savings * 12
#Attempt to get collect user date
try:
    savings = float(savings)
except ValueError:
    print("Please enter a valid value for savings.")
    savings = input ("How much money did you save this month? ")
    savings = float(savings)
#A fail safe, incase the user types in an invalid input
savings_year = savings * 12
print (f"You are on pace to save ${savings_year} this year.")
#Math to see how much the user will save in a year
       
