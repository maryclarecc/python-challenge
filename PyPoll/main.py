import os
import csv
import numpy as np
from numpy.core.fromnumeric import mean, sort

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    for row in csvreader:
        #print(row[1])
        data = list(csvreader)

#The total number of votes included in the dataset, count # of rows
    num_rows = -1 # to account for the header
    for row in open(csvpath):
        num_rows += 1

#A complete list of candidates who received votes
    candidates = []
    i = ["Voter ID", "County", "Candidate"]
    for row in data:
        candidates.append(row[2])
    uniquecand = sort(list(set(candidates)))
    #print(uniquecand)
#The total number of votes each candidate won
    khan = 0
    correy = 0
    li = 0
    otooley = 0
    for candidate in candidates:
        if candidate == "Khan":
            khan += 1
        if candidate == "Correy":
            correy += 1
        if candidate == "Li":
            li += 1
        if candidate == "O'Tooley":
            otooley += 1

#The percentage of votes each candidate won
    khanp = round((khan/num_rows * 100), 3)
    correyp = round((correy/num_rows * 100), 3)
    lip = round((li/num_rows * 100), 3)
    otooleyp = round((otooley/num_rows * 100), 3)

#The winner of the election based on popular vote.
    winner = {"Khan": khanp, "Correy": correyp, "Li": lip, "O'Tooley": otooleyp}
    max_value = max(winner, key = winner.get)
    
print("Election Votes")
print("-----------------------------------")
print(f"Total Votes: {num_rows}")
print("-----------------------------------")
print(f'{uniquecand[1]}: {khanp}% ({khan})')
print(f'{uniquecand[0]}: {correyp}% ({correy})')
print(f'{uniquecand[2]}: {lip}% ({li})')
print(f'{uniquecand[3]}: {otooleyp}% ({otooley})')
print("-----------------------------------")
print(f'Winner: {max_value}')
print("-----------------------------------")

output_path = os.path.join("analysis", "polls.txt")
f = open(output_path, "w")
f.write("Election Votes")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f"Total Votes: {num_rows}")
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f'{uniquecand[1]}: {khanp}% ({khan})')
f.write("\n")
f.write(f'{uniquecand[0]}: {correyp}% ({correy})')
f.write("\n")
f.write(f'{uniquecand[2]}: {lip}% ({li})')
f.write("\n")
f.write(f'{uniquecand[3]}: {otooleyp}% ({otooley})')
f.write("\n")
f.write("-----------------------------------")
f.write("\n")
f.write(f'Winner: {max_value}')
f.write("\n")
f.write("-----------------------------------")
f.close()
