# Programmer: Timothy Pickering
# Date: 2/13/25
# Title: Average Rainfall Calc

years = int(input("How many years would you like to calculate?: ")) #ask number of years
rainfallTotal = 0 #initalize rainfall
monthsTotal = years * 12 #total months based on years input
for year in range(1, years + 1): # Outer loop, Iterates for each year
    print(f"Year {year})")

    for month in range(1,13): # Inner loop, Iterates for each month
        rainfall = float(input(f"Enter rainfall (in inches) for month {month}: "))
        rainfallTotal = rainfallTotal + rainfall # Add rainfall to the total
rainfallAvg = rainfallTotal / monthsTotal # Calculate the average rainfall per month
print("Rainfall Data Summary:") # Display results
print(f"Total months recorded: {monthsTotal}")
print(f"Total rainfall in inches: {rainfallTotal:.2f}")
print(f"Average rainfall per month: {rainfallAvg:.2f}")
