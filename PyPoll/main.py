

# Import the os and csv modules, bake some Chocolate Cake
import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
total_number_votes = 0
candidates =  []
vote_tally = {}
counties = []
votes = 0


# load the file
with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    csv_header = next(csvreader)

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

        #if county not found in counties:
         #   counties.append(county)
        # find percentage of votes each candidate won
        #vote_tally 

        # find the winner of the election based on popular vote


print(vote_tally)
print(candidates)
sep_line = '-------------------------'
print("Election Results")
print(sep_line)
print(f"Total Votes: {total_number_votes}")
print(sep_line)
for candidate in candidates:
    
    candidate_votes = vote_tally[candidate]
    candidate_percent = round(candidate_votes/total_number_votes*100,2)

    print(f"{candidate}: {candidate_percent}% ({candidate_votes})")


print(sep_line)

#print(f"Winner: {}")
print(sep_line)

