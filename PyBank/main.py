import os
import csv

# Set path for file
budget_csv = os.path.join( "Documents", "GitHub", "python-challenge", "PyBank", "budget_data.csv" )

# Set variables to zero
total_months = 0
total_change = []
total = 0
minchange = 0
maxchange = 0
minchange_month = 0
maxchange_month = 0

# with open(budget_csv, newline="", encoding='utf-8') as csvfile:
with open(budget_csv, newline="", encoding="utf-8") as csvfile:

        # Store csv file in variable csvreader
        csvreader = csv.reader(csvfile, delimiter=",")

        # Skip the header labels to iterate with the values
        header = next(csvreader)
        row = next(csvreader)

        # Set variables for rows
        previous_value = (int(row[1]))
        total_months += 1
        total += (int(row[1]))
        minchange = (int(row[1]))
        minchange_month = row[0]

        # Iterate through the rows
        for row in csvreader:

            # Find total months
            total_months += 1

            # Find total profit/loss amount
            total += (int(row[1]))

            # Find the difference between profit/loss value and the previous profit/loss value
            change = (int(row[1])) - previous_value
            total_change.append(int(change))
            previous_value = (int(row[1]))
                
            # Find maximum difference for minimum and maximum values
            if int(row[1]) >= maxchange:
                maxchange = int(row[1])
                maxchange_month = str(row[0])
            elif int(row[1]) <= minchange:
                minchange = int(row[1])
                minchange_month = str(row[0])
        
        # Find average change
        average = sum(total_change)/len(total_change)

        # Correlate the maximum and minimum to each month           
        increase  = max(total_change)
        decrease  = min(total_change)

        # Print Statements
        print("Financial Analysis")
        print("--------------------------------")
        print(f"Total Months: {total_months}")
        print(f"Total: ${total}")
        print(f"Average Change: ${average:.2f}")
        print(f"Greatest Increase in Profits: {maxchange_month}, (${increase})")
        print(f"Greatest Decrease in Profits: {minchange_month}, (${decrease})\n")

        # Set variable for output file
        output_file = os.path.join("Documents", "GitHub", "python-challenge", "PyBank","Financial_Analysis.txt")

        # Open the outputfile
        with open(output_file, "w", newline="") as file:

        # Write methods to print to Financial_Analysis
            file.write("Financial Analysis")
            file.write("\n")
            file.write("-----------------------------")
            file.write("\n")
            file.write(f"Total Months: {total_months}")
            file.write("\n")
            file.write(f"Total: $ {total}")
            file.write("\n")
            file.write(f"Average Change: {average:.2f}")
            file.write("\n")
            file.write(f"Greatest Increase in Profits: {maxchange_month}, (${increase})")
            file.write("\n")
            file.write(f"Greatest Decrease in Profits: {minchange_month}, (${decrease})\n")
