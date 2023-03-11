import csv
import os
from contextlib import redirect_stdout #for writing to .txt file
import sys

#read path
budget_read = "PyBank/resources/budget_data.csv"
#write path
budget_write = "PyBank/resources/buget_output.txt"

#create the relevant variables
date = []
profit = []
net_total = 0
profit_change = []
sum_change = 0
profit_dict = {}

#read in the data
with open (budget_read, 'r') as f:
    budget = csv.reader(f, delimiter = ",")

#skip the header
    header = next(budget)

#create date and profit lists, calculate net total

    for row in budget:
        date.append(row[0])
        profit.append(int(row[1]))
        net_total = net_total + int(row[1])
        profit_dict[row[0]] = row[1]

#create a profit change list
    for i in range(len(profit) - 1):
        profit_change.append(profit[i+1] - profit[i])

 #calculate average change   
    for i in range(len(profit_change)):
        sum_change = sum_change + profit_change[i]
    average_change = sum_change / len(profit_change)

    max(profit_change)
    date

 #print the results
    def print_output():
        print("Financial Analysis")
        print("------------------------")
        print(f"Total Months: {len(date)}")
        print(f"Total: {net_total}")
        print(f"Average Change: ${average_change}") 
        print(f"Greatest Increase in Profits: {date[profit_change.index(max(profit_change))+1]} {max(profit_change)}")
        print(f"Greatest Decrease in Profits: {date[profit_change.index(min(profit_change))+1]} {min(profit_change)}")

    #print the output to terminal
    print_output()

    #print the results to text 
    with open(budget_write, 'w') as f:
        with redirect_stdout(f):
            #code to print
            print_output()

