# Austin Powers Monthly Expense Tracker, yeah baby!

# Prompt user for income and expenses
# Float allows for decimals
income = float(input("Tell me your total monthly income, baby: "))

# * -1 to create a negative number, to be used for financial staus below
rent = float(input("How much do you pay for your LAIR?!... I mean, rent, baby? ")) * -1
electricity = float(input("What’s the damage on your electric bill, baby? ")) * -1
internet = float(input("How much for the internet, baby? ")) * -1
phone = float(input("And your GROOVY phone bill, baby? ")) * -1
gas = float(input("Excuse me, but how much on gas, baby? ")) * -1
groceries = float(input("What’s it cost to feed that mojo, baby? ")) * -1
car = float(input("What's the monthly payment for your shagadelic ride, yeaa!? ")) * -1
spending = float(input("Be honest, baby... how much are spending on impulse buys? ")) * -1
streaming_subscriptions = float(input("All those streaming subscriptions for late-night shag sessions, baby? ")) * -1
insurance = float(input("Gotta stay insured to stay sexy, yea! What’s the total, baby? ")) * -1

# Calculate monthly profit
monProf = (income + rent + electricity + internet + phone +
           gas + groceries + car + spending + streaming_subscriptions + insurance)

# Calculate weekly income estimate divide monthly profit by 4
weekProf = monProf / 4

# Print results
print("\n--- Your Groovy Financial Recap, Baby! ---")
print("Monthly Profit:", round(monProf, 2), "Yeah baby!") #rounds two decimal points
print("Estimated Weekly Profit:", round(weekProf, 2), "Shagadelic!")

# Financial status compares income to bills
if monProf >= income:
    print("Yeah baby, yeah! You’re living large—mojo fully intact.")
else:
    print("Oof, that’s not groovy baby... your finances have lost their mojo.")
