import csv
import os

#create variables
total_votes = 0
candidates = []
percent_votes = []
candidate_count = []
#winner = "a"

#create a count of the candidate votes
ccs = 0
rad = 0
dd = 0

#readpath
read_election = "PyPoll/resources/election_data.csv"

#writepath
write_election = "PyPoll/analysis/results.txt"



with open (read_election, 'r') as f:
    election = csv.reader(f, delimiter = ",")

    header = next(election)

    
    for row in election:
        total_votes = total_votes + 1 #calculate the total number of votes
        candidates.append(row[2]) #create list of all candidates

        #calculate counts for each candidate
        if (row[2] == "Charles Casper Stockham"):
            ccs = ccs + 1
        
        elif (row[2] == "Raymon Anthony Doane"):
            rad = rad + 1

        elif (row[2] == "Diana DeGette"):
            dd = dd + 1

        else:
            print("typo or unexpected vote")

    candidates = set(candidates) #just keep unique values for candidates

    #calculate percentages
    ccs_pct = (ccs / total_votes) * 100
    dd_pct = (dd / total_votes) * 100
    rad_pct = (rad / total_votes) * 100

    #calculate winner
    

    #printing the results
    print("Election Results")
    print("-----------------------------")
    print(f"Total Votes: {total_votes}")
    print("-----------------------------")
    print(f"Charles Casper Stockham: {ccs_pct}% ({ccs})")
    print(f"Diana DeGette: {dd_pct}% ({dd})")
    print(f"Raymon Anthony Doane: {rad_pct}% ({rad})")
    print(f"-----------------------------")
    print(f"Winner: ")

    # print(total_votes)
    # print(set(candidates))
    # print(ccs, rad, dd)
