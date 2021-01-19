# Import the os and csv modules, bake some Chocolate Cake
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
total_number_votes = 0
candidates =  []
vote_tally = {}
counties = []
votes = 0
county_tally = {}
new_count = 0
candidate_votes = 0
candidate_percent = 0



# load the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    # print(csvreader) this is not needed for the final printout

    csv_header = next(csvreader)

    # proof that CSV header row successfully stored
    print(f"CSV Header: {csv_header}") 

     # iterate through the file... 
    for row in csvreader:

        total_number_votes = total_number_votes + 1
        county = row[1] 
        candidate = row[2]
        # find complete list of candidates who received votes
        if candidate not in candidates:
            candidates.append(candidate)
            vote_tally[candidate] = 1
        else:  
            new_count = 0
            new_count = vote_tally[candidate] + 1
            vote_tally[candidate] = new_count

        if county not in counties:
            counties.append(county)
            county_tally[county] = 1
        else:
            new_tally = 0
            new_tally = county_tally[county] + 1
            county_tally[county] = new_tally
        
        

#print(vote_tally)
#print(candidates)
sep_line = '-------------------------'
print("Election Results")
print(sep_line)
print(f"Total Votes: {total_number_votes}")
print(sep_line)

for candidate in candidates:

    # find percentage of votes each candidate won
    candidate_votes = vote_tally[candidate]
    candidate_percent = round(candidate_votes/total_number_votes*100,2)

    print(f"{candidate}: {candidate_percent}% ({candidate_votes})")


print(sep_line)
# find the winner of the election based on popular vote
winner = max(vote_tally, key=vote_tally.get)
print(f"Winner: {winner}")
print(sep_line)
# find the number of votes per county, just for fun
for county in counties:
    print(f"{county} county had {county_tally[county]} voters")
print(sep_line)

# Export the analysis to a text file, more chocolate cake... frosting, maybe?

# Specify the file to write to TODO: more meaningful file name?
output_path = os.path.join("Resources","election_results.txt")

# Open the file using "write" mode.  Specify the variable to hold the contents
with open(output_path, 'w', newline='') as newfile: #don't conflict with the opened file

    #Initialize the filewriter
    filewriter = csv.writer(newfile, delimiter=',')

    filewriter.writerow([sep_line])
    filewriter.writerow(["Election Results"])
    filewriter.writerow([sep_line])
    
    for candidate in candidates:
        candidate_votes = vote_tally[candidate]
        candidate_percent = round(candidate_votes/total_number_votes*100,2)

        filewriter.writerow([f"{candidate}: {candidate_percent}% ({candidate_votes})"])

    filewriter.writerow([sep_line])
    filewriter.writerow([f"Winner: {winner}"])
    filewriter.writerow([sep_line])

    for county in counties:
        filewriter.writerow([f"{county} county had {county_tally[county]} voters"])
    
    filewriter.writerow([sep_line])