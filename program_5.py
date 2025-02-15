#Programmer: Timothy Pickering
#Date: 2/14/25
#Title: Budget Tool

budgetAmount = float(input("Enter your budgeted amount for the month: "))
totalExpenses = 0 # Initialize total expenses
while True: # Start expense input loop
    expense = float(input("Enter an expense amount or 0: "))
    totalExpenses = totalExpenses + expense  # Add expense to total
    if expense == 0:
        break  # Exit the loop
difference = budgetAmount - totalExpenses  # Calculate difference
print("Total expenses:", totalExpenses)
print("Budgeted amount:", budgetAmount)
if difference > 0:
    print("You are under budget by:$", difference)
elif difference < 0:
    print("You are over budget by:$", -1*difference)
else:
    print("You met your budget exactly.")
