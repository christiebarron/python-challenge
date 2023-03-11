#import dependencies
import csv
import os
from contextlib import redirect_stdout #for writing to .txt file
import sys


#create variables
total_votes = 0
candidates = []
percent_votes = []
candidate_count = []
candidate_names = []
candidate_votes = {}

#readpath
read_election = "PyPoll/resources/election_data.csv"

#writepath
write_election = "PyPoll/analysis/results.txt"

#open file and save relevant data
with open (read_election, 'r') as f:
    election = csv.reader(f, delimiter = ",")

    header = next(election)

    
    for row in election:
        total_votes = total_votes + 1 #calculate the total number of votes 

        candidate_names = row[2] #save the candidate name for each row

        #
        if (candidate_names not in candidates):
            candidates.append(candidate_names)

            #save candidate name as an index to the dictionary. Set candidate vote as zero.
            candidate_votes[candidate_names] = 0
        
        #in the dictionary, index by the 'candidate name', add one to their vote count. 
        candidate_votes[candidate_names] = candidate_votes[candidate_names] +1

    #calculate the percentage of votes for each candidate
    for i in range(len(candidates)):
        percent_votes.append(candidate_votes[candidates[i]]/total_votes)
        
    #create a function to make printing easier
    def print_out(number):
        print(f"{candidates[number]}: {percent_votes[number]}% ({candidate_votes[candidates[number]]})")

    #create a printing function
    def print_full_out():

    # #printing the results
        print("Election Results")
        print("-----------------------------")
        print(f"Total Votes: {total_votes}")
        print("-----------------------------")

        #print out the remaining results
        for i in range(len(candidates)):
            print_out(i)

        print("--------------------------")
        print(f"Winner: {max(candidate_votes, key=lambda k: candidate_votes[k])}")

    #print results to terminal    
    print_full_out()

    #save printed results to text file
    with open(write_election, 'w') as f:
        with redirect_stdout(f):
            #code to print
            print_full_out()
