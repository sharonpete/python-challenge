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

    # proof that CSV header row successfully stored
    print(f"CSV Header: {csv_header}")
    
    total_months = 0
    net_profit = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = ""
    greatest_decrease_month = ""
    prior_month_result = 0
    current_month_result = 0
    current_increase = 0
    current_decrease = 0
    current_change = 0
    accumulate_changes = 0  
    first_row = True

    # iterate through the file... 
    for row in csvreader:

        # find the total number of months included in the dataset
        total_months = total_months +1

        # find the net total amount of "Profit/Losses" over the entire period
        net_profit = net_profit + int(row[1])

        # Find the greatest increase in profits (date and amount) over the entire period
        # .... this is measuring a month over month increase
        prior_month_result = current_month_result #save the prior month!
        current_month_result = int(row[1])
        
        current_change = current_month_result - prior_month_result

        if current_month_result > prior_month_result:  # gain
            current_increase = current_month_result - prior_month_result
           
        elif current_month_result < prior_month_result: #loss
            current_decrease = current_month_result - prior_month_result #this is wrong
            

        if current_increase > greatest_increase:
            greatest_increase = current_increase
            greatest_increase_month = row[0]

        # Find the greatest decrease in losses (date and amount) over the entire period
        # .... this is measuring a month over month loss?
        if current_decrease < greatest_decrease:
            greatest_decrease = current_decrease
            greatest_decrease_month = row[0]

        # calculate the changes in "Profit/Losses" over the entire period, 
        # then find the average of those changes
        if first_row == False:
          
            accumulate_changes = accumulate_changes + current_change

        first_row = False  


#average_change = net_profit/total_months
average_change = round(accumulate_changes / (total_months - 1),2)
sep_line = '-------------------------'

# Print the anaylysis to the terminal window
print(sep_line)
print("Financial Analysis")
print(sep_line)
print(f"Total number of months: {total_months}")
print(f"Net profit: ${net_profit}")
print(f"Average Change = ${average_change}")

print(f"Greatest increase in Profits: ${greatest_increase} in {greatest_increase_month}")
print(f"Greatest decrease in Profits: ${greatest_decrease} in {greatest_decrease_month}")
print(sep_line)

# Export the analysis to a text file, more chocolate cake... frosting, maybe?

# Specify the file to write to 
output_path = os.path.join("Resources","financial_analysis.txt")

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newfile: #don't conflict with the opened file

    #Initialize the filewriter
    filewriter = csv.writer(newfile, delimiter=',')

    filewriter.writerow([sep_line])
    filewriter.writerow(["Financial Analysis"])
    filewriter.writerow([sep_line])
    filewriter.writerow([f"Total number of months: {total_months}"])
    filewriter.writerow([f"Net profit: ${net_profit}"])
    filewriter.writerow([f"Average Change = ${average_change}"])
    filewriter.writerow([f"Greatest increase in Profits: ${greatest_increase} in {greatest_increase_month}"])
    filewriter.writerow([f"Greatest decrease in Profits: ${greatest_decrease} in {greatest_decrease_month}"])
    filewriter.writerow([sep_line])