import os
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')
# variable to count number of months
total_months = []
profit_loss=[]
monthly_change = []


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # loop through rows, each row w/ data adds to month list
    for row in csvreader:
        if len(row[0]) > 0:
            total_months.append(row)
            profit_loss.append(int(row[1]))
    
    for i in range(0,(len(total_months)-1)):
        change = profit_loss[i] - profit_loss[i+1]
        monthly_change.append(change)

    average_change = sum(monthly_change) / (len(total_months)-1)
    
    



    print("Financial Analysis")
    print("----------------------------")
    print(f"Total Months: {len(total_months)}")
    print(f"Total: ${sum(profit_loss)}")
    print(f"Average Change: $[{round(average_change,2)}]")
    #print("Greatest Increase in Profits: Feb-2012 ($1926159)")
    #print("Greatest Decrease in Profits: Sep-2013 ($-2196167)")

# EXPORT TO TEXT FILE!!