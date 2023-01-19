# import modules
import os 
import csv

# set path to file
election_csv = os.path.join("C:\\Users\\13139\\Desktop\\python-challenge\\python_challenge\\PyPoll\\Resources\\election_data.csv")

# set variables
total_votes = 0
candidates_names = []
candidate_votes = {}
winning_candidate = ""
winning_votes = 0

# open csv
with open (election_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row
    csv_header = next(csvreader) 

    # loop through data 
    for row in csvreader:

        # find total votes
        total_votes += 1 

        # finding candidates 
        candidates = row[2]

        if candidates not in candidates_names:

            #if its not in candidate_name then add it 
            candidates_names.append(row[2])

        # count candidates votes 
        candidate_votes[candidates] = 0
        
        # add vote to candidate's count
        candidate_votes[candidates] = candidate_votes[candidates] + 1

# Write results for votes
election_results = (
    f"\n\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes}\n"
    f"-------------------------\n")

print(election_results, end="")

# path for file with results for votes
E_results_file = os.path.join("C:\\Users\\13139\\Desktop\\python-challenge\\python_challenge\\PyPoll\\analysis\\results.txt")

# export results to file
with open (E_results_file, "w") as file:
    file.write(election_results)

# loop through counts to find winner
for candidate in candidate_votes:

    # get vote count and percent
    votes = candidate_votes[candidate]
    vote_percent = float(votes) / float(total_votes) * 100 

    # determine winning winning candidate and votes
    if (votes > winning_votes):
        winning_votes = votes 
        winning_candidate = candidate

    # print voter count and percent
    voter_output = f"{candidate}: {vote_percent:.3f}% ({votes})\n"
    print(voter_output, end="")

E_results_file = os.path.join("C:\\Users\\13139\\Desktop\\python-challenge\\python_challenge\\PyPoll\\analysis\\results.txt")

with open (E_results_file, "a") as file:
    # add to file
    file.write(voter_output)

    # print winning candidate
    winning_candidate_results = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"-------------------------\n")

    print(winning_candidate_results)

    # add to file
    file.write(winning_candidate_results)
