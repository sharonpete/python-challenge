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
    prior_month_result = 0
    current_month_result = 0
    current_increase = 0
    current_decrease = 0
    current_change = 0
    accumulate_changes = 0  # this is a terrible name, CHANGE ME
    first_row = True

    # iterate through the file... 
    for row in csvreader:

        # find the total number of months included in the dataset
        total_months = total_months +1

        # find the net total amount of "Profit/Losses" over the entire period
        net_profit = net_profit + int(row[1])

        # Find the greatest increase in profits (date and amount) over the entire period
        # .... this is measuring a month over month increase?
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
        # skip the first row... this is ugly
        if first_row == False:
            #print(f"... current change: {current_change} and accumulated changes: {accumulate_changes}")
            accumulate_changes = accumulate_changes + current_change

        first_row = False  

#print(f"accumulated changes: {accumulate_changes}")
#average_change = net_profit/total_months
average_change = accumulate_changes / (total_months - 1)

# Print the anaylysis to the terminal window
print("Financial Analysis")
print("----------------------------")
print(f"Total number of months: {total_months}")
print(f"Net profit: ${net_profit}")
print(f"Average Change = ${average_change}")

print(f"Greatest increase: ${greatest_increase} in {greatest_increase_month}")
print(f"Greatest decrease: ${greatest_decrease} in {greatest_decrease_month}")

# Export the analysis to a text file, more chocolate cake... frosting, maybe?

# Specify the file to write to TODO: more meaningful file name?
output_path = os.path.join("Resources","new.csv")

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newfile: #don't conflict with the opened file

    #Initialize the filewriter
    filewriter = csv.writer(newfile, delimiter=',')

    filewriter.writerow(["Financial Analysis"])
    filewriter.writerow(["----------------------------"])
    filewriter.writerow([f"Total number of months: {total_months}"])
    filewriter.writerow([f"Net profit: ${net_profit}"])
    filewriter.writerow([f"Average Change = ${average_change}"])
    filewriter.writerow([f"Greatest increase: ${greatest_increase} in {greatest_increase_month}"])
    filewriter.writerow([f"Greatest decrease: ${greatest_decrease} in {greatest_decrease_month}"])