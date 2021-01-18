

# Import the os and csv modules, bake some Chocolate Cake
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')



# load the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

    print(f"CSV Header: {csv_header}")

    total_number_votes = 0

     # iterate through the file... 
    for row in csvreader:

        total_number_votes = total_number_votes + 1


sep_line = '-------------------------'
print("Election Results")
print(sep_line)
print(f"Total Votes: {total_number_votes}")
print(sep_line)



print(sep_line)


print(sep_line)

