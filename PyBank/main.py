# import modules
import csv
import os

# path for file that will be read
budget_csv = os.path.join("C:\\Users\\13139\\Desktop\\python-challenge\\python_challenge\\PyBank\\Resources\\budget_data.csv")

# set variables
total_months = []
previous_pl = 0
months_change = []
pl_change_list = []
greatest_decrease = ["", 9999999]
greatest_increase = ["", 0]
total_pl = 0

# open csv
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # read header row first
    csv_header = next(csvreader) 

    # iterate through data
    for row in csvreader:

        # get total months
        total_months.append(row[0])

        # calculate total profit/losses
        total_pl = total_pl + int(row[1])
        
        # iterate through all profit/losses change
        pl_change = int(row[1]) - previous_pl
        previous_pl = int(row[1])
        pl_change_list = pl_change_list + [pl_change]
        months_change = months_change + [row[0]]

        # finding the greatest increase 
        if pl_change > greatest_increase [1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = pl_change

        # finding the greatest decrease
        if pl_change < greatest_decrease [1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = pl_change
        
# calculate average in profit/loss
pl_average = sum(pl_change_list) / len(pl_change_list)

# write analysis
analysis = (
     f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {len(total_months)}\n"
    f"Total Revenue: ${total_pl}\n"
    f"Average Revenue Change: ${pl_average}\n"
    f"Greatest Increase in Revenue: {greatest_increase[0]} (${greatest_increase[1]})\n"
    f"Greatest Decrease in Revenue: {greatest_decrease[0]} (${greatest_decrease[1]})\n")

# print analysis
print(analysis)

# path for file that will have results from analysis
results_file = os.path.join("C:\\Users\\13139\\Desktop\\python-challenge\\python_challenge\\PyBank\\analysis\\results.txt")

# export results to file
with open (results_file, "w") as file:
    file.write(analysis)











    
