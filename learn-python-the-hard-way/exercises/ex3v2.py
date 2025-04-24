# Monthly Expense Tracker with User Input

# Prompt user for income and expenses
income = float(input("Enter your total monthly income: "))
# multiply by -1 to turn into a negative value, flaot allows for deicmal points
rent = float(input("Enter your rent/mortgage amount: ")) * -1
electricity = float(input("Enter your electricity bill: ")) * -1
internet = float(input("Enter your internet bill: ")) * -1
phone = float(input("Enter your phone bill: ")) * -1
gas = float(input("Enter your monthly gas cost: ")) * -1
groceries = float(input("Enter your grocery budget: ")) * -1
car = float(input("Enter your car payment: ")) * -1
spending = float(input("Enter your general spending: ")) * -1
streaming_subscriptions = float(input("Enter your streaming subscriptions total: ")) * -1
insurance = float(input("Enter your insurance cost (health, auto, etc.): ")) * -1

# Calculate monthly profit, adds all pormpts
monProf = (income + rent + electricity + internet + phone +
           gas + groceries + car + spending + streaming_subscriptions + insurance)

# Calculate weekly income estimate by dividing monthly by 4
weekProf = monProf / 4

# Print results
print("\n----- Summary -----") #\n will start a new line
print("Monthly Profit:", round(monProf, 2)) # rounds by 2 deimcal places
print("Estimated Weekly Profit:", round(weekProf, 2))

# Financial status, compares income to bills
if monProf >= income:
    print("Yeah baby, yeah! You’re living large—mojo fully intact.")
else:
    print("Oof, that’s not groovy baby... your finances have lost their mojo.")

