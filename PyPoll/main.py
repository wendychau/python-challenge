import os
import csv
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# list to keep track of number of voters
voter_IDs = []
# list of candidates to be generated from data
candidates = []
# list to keep track of votes for each candidate
votes = []

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    # loop through rows for name + quantity of unique candidates and count voters
    for row in csvreader:        
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
        if row[0] is not None:
            voter_IDs.append(row[0])
    
        # after gathering candidate names, count votes
        for i in range(0,len(candidates)):
            if row[2] == candidates[i]:
                votes[i] = votes[i] +1
        
    # winner declared based on highest number of votes, indexes matched up
    winner = candidates[votes.index(max(votes))]

    # use indexes from various lists for printing
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {len(voter_IDs)}")
    print("-------------------------")

    # loop through candidate name and their results, rounded to nearest whole percent, with 3 trailing zeroes
    for i in range(0,len(candidates)):
        print(f"{candidates[i]}: {'{:.3%}'.format(round((votes[i] / len(voter_IDs)),2))} ({votes[i]})")

    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    # EXPORT TO TEXT FILE!!