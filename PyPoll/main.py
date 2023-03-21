import os
import csv

# specify the path to open the csv doc
csvpath = os.path.join("Resources", "election_data.csv")

# open the csv doc and convert to dictionary
with open(csvpath, "r") as csvfile:
    csvreader = (csv.DictReader(csvfile, delimiter =","))

    # initiate iteration for votes from 0
    total_votes = 0

    # set up an empty candidate and vote list
    candidate_list = []
    cand_vote = []
    percent_vote = []


    for row in csvreader:
        total_votes = total_votes + 1  
        # append unique candidate names into candidate_list
        if row["Candidate"] not in candidate_list:
            candidate_list.append(row["Candidate"])
            cand_vote.append(1)
        # calculate number of votes per unique candidate
        else:
            for i in range(len(candidate_list)):
                if row["Candidate"] == candidate_list[i]:
                    cand_vote[i] = cand_vote[i] + 1
    
    # initiate max_vote and set as the vote of the first candidate; max_cand as the first candidate
    max_vote = cand_vote[0]
    max_cand = candidate_list[0]
    # compute percentage of votes for each candidate
    for j in range(len(candidate_list)):
        percent_vote.append(round(cand_vote[j] * 100/total_votes, 3))
        # find maximum vote and associate candidate
        if cand_vote[j] > max_vote:
            max_vote = cand_vote[j]
            max_cand = candidate_list[j]
        
# write results to analysis.txt
output_path = os.path.join("Analysis", "analysis.txt")

lines = ["Election Results", "------------------------", 
        f"Total Votes: {total_votes}", "------------------------", 
        f"{candidate_list[0]}: {percent_vote[0]}% ({cand_vote[0]})",
        f"{candidate_list[1]}: {percent_vote[1]}% ({cand_vote[1]})", 
        f"{candidate_list[2]}: {percent_vote[2]}% ({cand_vote[2]})", "------------------------",
        f"Winner: {max_cand}"]


with open(output_path, "w") as txtfile:
    txtfile.write("\n".join(lines))
