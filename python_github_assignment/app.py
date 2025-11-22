print ("Welcome to My Python Code")
savings = input ("How much money did you save this month? ")
savings_year = savings * 12
try:
    savings = float(savings)
except ValueError:
    print("Please enter a valid value for savings.")
    savings = input ("How much money did you save this month? ")
    savings = float(savings)
savings_year = savings * 12
print (f"You are on pace to save ${savings_year} this year.")
       
