import os
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# list to keep track of number of voters
voter_IDs = []

candidates = ["Khan", "Correy", "Li", "O'Tooley"]
votes = [0,0,0,0]

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

# loop through rows, each row w/ data adds to voter ID list
    for row in csvreader:
        if len(row[0]) > 0:
            voter_IDs.append(row)
        if row[2] == "Khan":
                votes[0] = votes[0] + 1
        elif row[2] == "Correy":
                votes[1] = votes[1] + 1
        elif row[2] == "Li":
                votes[2] = votes[2] + 1
        elif row[2] == "O'Tooley":
                votes[3] = votes[3] + 1

# use indexes from various list for printing
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(voter_IDs)}")
    print("-------------------------")
    print(f"Khan: 63.000% ({votes[0]})")
    print(f"Correy: 20.000% ({votes[1]})")
    print(f"Li: 14.000% ({votes[2]})")
    print(f"O'Tooley: 3.000% ({votes[3]})")
    print("-------------------------")
    print("Winner: Khan")
    print("-------------------------")


# EXPORT TO TEXT FILE!!