#import modules
import os
import csv

# defining pPyBank's variables
months = []
changes_profit_loss = []

count_months = 0
profit_losses = 0
proft_losses_previous = 0
profit_losses_current = 0
profit_loss_change = 0

# change directory to current python script
os.chdir(os.path.dirname(__file__))

#set path to collect the data from the file
budget_data_path = os.path.join("Resources", "budget_data.csv")



# open and read the csv
with open(budget_data_path, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read header in row first
    csv_header = next(csvfile)

    #print(f"Header: {csv_header}"")
    # this prints the Header: Date, Profit/Losses

    # Read through each row of data after the header
    for row in csv_header:

        # count of months
        count_months += 1

        # Net total amount of proft/lossesover the period
        profit_losses_current = int(row[1])
        profit_losses += profit_losses_current

        if (count_months == 1):    
            # make the value the previous month to be equal to current
            proft_losses_previous = profit_losses_current
            continue

        else:
            
            # compute changes in profit loss
           profit_loss_change = profit_losses_current - proft_losses_previous

           #append each month to months[]
           months.append(row[0])

           #append each profit_loss_change to the changes_profit_loss[]
           changes_profit_loss.append(profit_loss_change)

           #make current month loss to be previois loss for next loop
           proft_losses_previous = profit_losses_current

#sum and average of the changes in profit/loss over period
sum_profit_loss = sum(changes_profit_loss)
average_profit_loss = round(sum_profit_loss/(count_months - 1), 2)

#highest and lowest changes in profit/loss
highest_change = max(changes_profit_loss)
lowest_change = min(changes_profit_loss)

#locate the index value for highest and lowest months
highest_month_index = changes_profit_loss.index(highest_change)
lowest_month_index = changes_profit_loss.index(lowest_change)

# assign best and worst month
best_month = months[highest_month_index]
worst_month = months[lowest_month_index]

# print the analysis to the terminal
print("Financial Analysis")
print("----------------------")
print(f"Total Months:  {count_months}")
print(f"Total:  ${profit_losses}")
print(f"Average Change  ${average_profit_loss}")
print(f"Greatest Increase in Profits:  {best_month} (${highest_change})")
print(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})")


# -->>  Export a text file with the results
budget_data_file = os.path.join("analysis", "budget_data.txt")
with open(budget_data_file, "w") as outfile:

    outfile.write("Financial Analysis\n")
    outfile.write("----------------------------\n")
    outfile.write(f"Total Months:  {count_months}\n")
    outfile.write(f"Total:  ${profit_losses}\n")
    outfile.write(f"Average Change:  ${average_profit_loss}\n")
    outfile.write(f"Greatest Increase in Profits:  {best_month} (${highest_change})\n")
    outfile.write(f"Greatest Decrease in Losses:  {worst_month} (${lowest_change})\n")