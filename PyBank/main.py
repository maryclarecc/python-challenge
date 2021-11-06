import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, "r") as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

   # print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    # print(f"CSV Header: {csv_header}")

    # # Read each row of data after the header
    #The total number of months included in the dataset, count # of rows
    prls = []
    dates = []
    num_rows = 0
    for row in csvreader:
        #i = int(float(row[1]))
        #print(row[1])
        #data = list(csvreader)
        prls.append(int(row[1]))
        dates.append(row[0])
        num_rows += 1
    #print(prls)   
        

    print("Financial Analysis")
    print("----------------------------------------------")
    print(f"Total Months: {num_rows}")

#The net total amount of "Profit/Losses" over the entire period
    profloss = (sum(prls))
    print(f"Total: ${profloss}")

#Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
    change = round((prls[-1] - prls[0])/len(prls), 2)
    print(f"Average Change: ${change}")

#The greatest increase in profits (date and amount) over the entire period
    maximum = max(prls)
    indexing = prls.index(maximum)
    increasepr = dates[indexing]
    print(f"Greatest Increase in Profits: {increasepr} (${maximum})")

#The greatest decrease in profits (date and amount) over the entire period
    minimum = min(prls)
    indexing2 = prls.index(minimum)
    increasepr2 = dates[indexing2]
    print(f"Greatest Decrease in Profits: {increasepr2} (${minimum})")

#write txt file
output_path = os.path.join("analysis", "budget.txt")
f = open(output_path, "w")
f.write("Financial Analysis")
f.write("\n")
f.write("----------------------------------------------")
f.write("\n")
f.write((f"Total Months: {num_rows}"))
f.write("\n")
f.write((f"Total: ${profloss}"))
f.write("\n")
f.write((f"Average Change: ${change}"))
f.write("\n")
f.write((f"Greatest Increase in Profits: {increasepr}, (${maximum})"))
f.write("\n")
f.write((f"Greatest Decrease in Profits: {increasepr2}, (${minimum})"))
f.write("\n")
f.close()
