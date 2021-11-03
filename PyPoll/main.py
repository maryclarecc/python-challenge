import os
import csv
import numpy as np
from numpy.core.fromnumeric import mean

csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    for row in csvreader:
        #print(row[1])
        data = list(csvreader)

#The total number of votes included in the dataset, count # of rows
    num_rows = 0
    for row in open(csvpath):
        num_rows += 1

    print(f"Total Votes: {num_rows}")

    np.unique(data)