import csv
import os

#read path
budget_read = "PyBank/resources/budget_data.csv"
#write path
budget_write = "PyBank/resources/buget_output.csv"

#create the relevant variables
date = []
profit = []
net_total = 0
profit_change = []
sum_change = 0

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

#create a profit change list
    for i in range(len(profit) - 1):
        profit_change.append(profit[i+1] - profit[i])

 #calculate average change   
    for i in range(len(profit_change)):
        sum_change = sum_change + profit_change[i]
    average_change = sum_change / len(profit_change)

    average_change.index

 #print the results
    print("Financial Analysis")
    print("------------------------")   
    print(f"Total Months: {len(date)}")
    print(f"Average Change: ${average_change}") 
    print(f"Greatest Increase in Profits: {max(profit_change)}")
    print(f"Greatest Decrease in Profits: {min(profit_change)}")

#NEED TO FIX THE INCREASE AND DECREASE IN PROFITS TO INCLUDE THE MONTH
#NEED TO PRINT SCRIPT TO A TEXT FILE TOO. 


