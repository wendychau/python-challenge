import os
import csv
csvpath = os.path.join('.', 'Resources', 'budget_data.csv')

# list to track different months on record
months = []
# list of profits or losses from month to month
profit_loss = []
# list to track changes
monthly_change = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    
    # loop through rows, each row w/ data adds to month & profit/loss list
    for row in csvreader:
        if row[0] is not None:
            months.append(row[0])
            profit_loss.append(int(row[1]))
    # loop through rows and calculate change from month to month
    for i in range(0,(len(months)-1)):
        change = profit_loss[i+1] - profit_loss[i]
        monthly_change.append(change)

    # variable / formula for average
    average_change = sum(monthly_change) / (len(months)-1)

    # month with greatest increase/decrease in profits is one-after the matching index
    # it's the more recent month when calculating change
    greatest_increase_month = months[monthly_change.index(max(monthly_change))+1]
    greatest_decrease_month = months[monthly_change.index(min(monthly_change))+1]

    print("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {len(months)}\n"
        f"Total: ${sum(profit_loss)}\n"
        f"Average Change: ${round(average_change,2)}\n"

        # using indexes from lists, find greatest increase/decrease months
        f"Greatest Increase in Profits: {greatest_increase_month} (${max(monthly_change)})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${min(monthly_change)})")

    # export to text file
    file_bank = open("financial_analysis.txt","w")
    file_bank.write("Financial Analysis\n"
        "----------------------------\n"
        f"Total Months: {len(months)}\n"
        f"Total: ${sum(profit_loss)}\n"
        f"Average Change: ${round(average_change,2)}\n"
        f"Greatest Increase in Profits: {greatest_increase_month} (${max(monthly_change)})\n"
        f"Greatest Decrease in Profits: {greatest_decrease_month} (${min(monthly_change)})\n")

    file_bank.close()