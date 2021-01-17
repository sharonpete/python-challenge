# This will analyze the financial records for ACME 

# Import the os and csv modules, bake some Chocolate Cake
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# load the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")
    
    total_months = 0
    net_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""
    

    # iterate through the file... 
    for row in csvreader:

        # find the total number of months included in the dataset
        total_months = total_months +1

        # find the net total amount of "Profit/Losses" over the entire period
        net_profit = net_profit + int(row[1])

        # Find the greatest increase in profits (date and amount) over the entire period
        # .... this is measuring a month over month increase?
        if int(row[1]) > greatest_increase:
            greatest_increase = int(row[1])
            greatest_increase_month = row[0]

        # Find the greatest decrease in losses (date and amount) over the entire period
        # .... this is measuring a month over month loss?
        if int(row[1]) < greatest_decrease:
            greatest_decrease = int(row[1])
            greatest_decrease_month = row[0]

        # calculate the changes in "Profit/Losses" over the entire period, 
        # then find the average of those changes
        

average_change = net_profit/total_months
print(f"average change = {average_change}")

# Print the anaylysis to the terminal window
print("Financial Analysis")
print("----------------------------")
print(f"Total number of months: {total_months}")
print(f"Net profit: ${net_profit}")
print(f"Greatest increase: ${greatest_increase} in {greatest_increase_month}")
print(f"Greatest decrease: ${greatest_decrease} in {greatest_decrease_month}")

# Export the analysis to a text file

