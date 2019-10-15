import os
import csv

election_csv = os.path.join("Documents", "GitHub", "python-challenge", "PyPoll", "election_data.csv")

# Set variables
total_votes = 0
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

# with open(election_csv, newline="", encoding='utf-8') as csvfile:
with open(election_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header
    header = next(csvreader)

    # Iterate through each row
    for row in csvreader:

        # Set a variable of total_votes to count the votes by ID
        total_votes += 1

        # Seperate the values by candidates
        if row[2] == "Khan":
            khan_votes += 1
        elif row[2] == "Correy":
            correy_votes += 1
        elif row[2] == "Li":
            li_votes += 1
        elif row[2] == "O'Tooley":
            otooley_votes += 1

    # Create a dictionary for the candidates and votes
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    votes = [khan_votes, correy_votes, li_votes, otooley_votes]

    # Zip lists together
    candidates_votes_dict = dict(zip(candidates,votes))
    key = max(candidates_votes_dict, key = candidates_votes_dict.get)

    # Find the percentage of votes
    khan_percent = (khan_votes/total_votes) * 100
    correy_percent = (correy_votes/total_votes) * 100
    li_percent = (li_votes/total_votes) * 100
    otooley_percent = (otooley_votes/total_votes) * 100

    # Print the analysis
    print(f"Election Results")
    print(f"--------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"--------------------------")
    print(f"Khan: {khan_percent:.5}%  ({khan_votes})")
    print(f"Correy: {correy_percent:.5}%  ({correy_votes})")
    print(f"Li: {li_percent:.5}%  ({li_votes})")
    print(f"O'Tooley: {otooley_percent:.4}%  ({otooley_votes})")
    print(f"--------------------------")
    print(f"Winner: {key}")
    print(f"--------------------------")

    # Set variable for the output file
    output_file = os.path.join("election_results.csv")

    # Open the output file
    with open(output_file, "w", newline="") as datafile:
        # Write the analysis
        datafile.write(f"Election Results")
        datafile.write("\n")
        datafile.write(f"--------------------------")
        datafile.write("\n")
        datafile.write(f"Total Votes: {total_votes}")
        datafile.write("\n")
        datafile.write(f"--------------------------")
        datafile.write("\n")
        datafile.write(f"Khan: {khan_percent:.5}%  ({khan_votes})")
        datafile.write("\n")
        datafile.write(f"Correy: {correy_percent:.5}%  ({correy_votes})")
        datafile.write("\n")
        datafile.write(f"Li: {li_percent:.5}%  ({li_votes})")
        datafile.write("\n")
        datafile.write(f"O'Tooley: {otooley_percent:.4}%  ({otooley_votes})")
        datafile.write("\n")
        datafile.write(f"--------------------------")
        datafile.write("\n")
        datafile.write(f"Winner: {key}")
        datafile.write("\n")
        datafile.write(f"--------------------------")