# Import modules
import os
import csv

# Define PyBank's variables as lists
months = []
profit_loss_changes = []

#setting the values as 0 
count_of_months = 0
profit_loss = 0
profit_loss_month_previous = 0
profit_loss_current_month = 0
profit_loss_change = 0


# Change directory to the directory of current python script
os.chdir(os.path.dirname(__file__))

# Path to collect data from the Resources folder
budget_data_csv_path = os.path.join("Resources", "budget_data.csv")


# Open and read csv
with open(budget_data_csv_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first
    csv_header = next(csvfile)
             
    # Read through each row of data after the header
    for row in csv_reader:

        # Count of months
        count_of_months += 1

        # Net total amount of "Profit/Losses" over the entire period
        profit_loss_current_month = int(row[1])
        profit_loss += profit_loss_current_month
        #conditional logic if there is no change
        if (count_of_months == 1):
            # Make the value of previous month to be equal to current month
            profit_loss_month_previous = profit_loss_current_month
            continue

        else:

            # Compute change in profit loss 
            profit_loss_change = profit_loss_current_month - profit_loss_month_previous

            # Append each month to the months list
            months.append(row[0])

            # Append each profit_loss_change to the profit_loss_changes list
            profit_loss_changes.append(profit_loss_change)

            # Make the current_month_loss to be previous_month_profit_loss for the next loop
            profit_loss_month_previous = profit_loss_current_month

    #sum and average of the changes in "Profit/Losses" over the entire period
    sum_profit_loss = sum(profit_loss_changes)
    average_profit_loss = round(sum_profit_loss/(count_of_months - 1), 2)

    # highest and lowest changes in "Profit/Losses" over the entire period
    highest_change = max(profit_loss_changes)
    lowest_change = min(profit_loss_changes)

    # Locate the index value of highest and lowest changes in "Profit/Losses" over the entire period
    highest_month_index = profit_loss_changes.index(highest_change)
    lowest_month_index = profit_loss_changes.index(lowest_change)

    # Assign best and worst month
    best_month = months[highest_month_index]
    worst_month = months[lowest_month_index]

# -->>  Print the analysis to the terminal
print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {count_of_months}")
print(f"Total:  ${profit_loss}")
print(f"Average Change:  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# -->>  Export a text file with the results
budget_data_file = os.path.join("analysis", "budget_data.txt")
with open(budget_data_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_of_months}\n")
    outfile.write(f"Total:  ${profit_loss}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")