import csv

# Files to load and output (Remember to change these)
file_to_load = "election_data_2.csv"
file_to_output = "election_analysis_1.txt"

# Read the csv and convert it into a reader

with open(file_to_load,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)[1:] 

Voter_ID = []
Candidate_Vote = []

for row in data:
# Populate revenue list and slice out the header
    Voter_ID.append((row[0]))

for row in data:
# Populate revenue list and slice out the header
    Candidate_Vote.append((row[2]))

# Determine the total number of vote

Total_Votes = len(Candidate_Vote)
Total_Votes = int(Total_Votes)

# Determine the unique candidate names by creating a set
Candidate_Set = set(Candidate_Vote)
names = []

for row in Candidate_Set:
    names.append(row)

# Start Printing the output

print(" Election Results   ")

print( "---------------------")

print("Total Number of Votes -  ", Total_Votes)

# Set up a loop to print out the candidates and votes

can = 0
Candidate_Dictionary = {}

# This for loop will print out each line of the output for each candidate
for row in names:
    candidate = str(names[can])
    Votes = Candidate_Vote.count(candidate)
    Votes = int(Votes)
    percentage = Votes / Total_Votes * 100
    percentage = int(percentage)
    Candidate_Dictionary.update({ candidate : Votes})
    print(candidate, ":  ", percentage, " %  (", Votes, ")" )
    can = can + 1



import operator

# This line of code I found will print out the name of the candidate with the most votes
winner = max(Candidate_Dictionary, key=lambda key: Candidate_Dictionary[key])


# Print out the last of the output
print("-------------------")
print("Winner:  ", winner)



