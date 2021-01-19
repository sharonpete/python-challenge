# python-challenge
This is a repo for the Python homework.
Sharon Templin
U of Mn Data Analytics Bootcamp Cohort 10


Development notes below:
- Created the Analysis and Resources directories and then added the CSV files to the Resources directories for the respective exercises.
- Adding these to git took three tries because of the large CSV files.  
- PyBank:
  - added opening and reading of CSV file... had a minor syntax error, but otherwise it was Chocolate Cake!
  - added iteration through the CSV file and initial calculations for total months, net profits/losses over entire period, greatest increase in profit (date and amount) over entire period, greatest decrease in losses (date and amount) over entire period (assuming that this means the greatest loss, because "greatest decrease in losses" could mean something else entirely)
  - I am not sure what "calculate the changes in profit/losses over the entire period, then find the average of those changes" means, so I am going to punt for the moment with my best guess
  - Okay, that was not so difficult to solve, the changes are calculated and the average change is good... had to put parens around the denominator (total_months-1).  I tried the calculations on the spreadsheet and found my python calculation was initially wrong.  How do we ensure accuracy in the real world? 
  - added functionality to print out the financial analysis results to a text file
  - Re-read rubric... printing out CSV header to show it is successfully stored 
- PyPoll
  - added opening and reading of CSV file... more Chocolate Cake!
  - created a list of candidates as we go, adding a new one as a unique candidate is found, so far, so good
  - got the initial pass at printing out results in place
  - decided to use a dictionary to tally the votes... had to play with the syntax a bit to gain some understanding.
  - wow, after all of this, I should check in my code! (ooops, missed about 5 check-ins as I was focused on getting this done)
  - found the winner of the election using the max function.  i notice that the candidates are always listed in order of the number of votes they receive (highest to lowest) with basically no intervention on my part.
  - i added the tally of voters per county just to get a little more practice... and it was fun.
  - maybe a needless refinement, but i made the separating line into its own variable on both main.py files, just to clean things up a bit
  - Re-read rubric ... printing out CSV header to show it is successfully stored
  - added functionality to print out the election results to a text file.  i had to make a call on this, i ended up looping through the candidates twice to print out to the terminal and then to the file.  I could have combined things so i only did the loop once, but decided that that would have been too messy, too confusing, and too difficult to maintain if this thing were going to be maintained.  so hence the two fairly duplicate loops