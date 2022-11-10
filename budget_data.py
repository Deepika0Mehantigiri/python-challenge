import os
import csv
data_path=os.path.join("..","PyBank\Resources", "budget_data.csv")

total_months =0
profit_loss = 0
value = 0
changes = 0
date_change = []
profits = []

with open(data_path) as budget_datafile:
    csvreader = csv.reader(budget_datafile, delimiter=",")

    csv_header = next(csvreader)
    first_row = next(csvreader)
    total_months += 1
    profit_loss += int(first_row[1])
    value = int(first_row[1])
  
    for row in csvreader:

        date_change.append(row[0])
        changes = int(row[1])-value
        profits.append(changes)
        value = int(row[1])

       
        total_months += 1

        profit_loss = profit_loss + int(row[1])

        average_change = sum(profits)/len(profits)

    greatest_increase = max(profits)
    greatest_increase_index = profits.index(greatest_increase)
    greatest__increase_date = date_change[greatest_increase_index]

    greatest_decrease = min(profits)
    greatest__decrease_index = profits.index(greatest_decrease)
    greatest__decrease_date = date_change[greatest__decrease_index]

print("Financial Analysis")
print("------------------------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(profit_loss)}")
print(f"Average Change: $ {str(round(average_change,2))}")
print(f"Greatest Increase in Profits: {greatest__increase_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {greatest__decrease_date} (${str(greatest_decrease)})")



budgetoutput_file = os.path.join('Resources', 'budget_data.txt')
pyBank = open(budgetoutput_file, "w")

line1 = "Financial Analysis"
line2 = "------------------------------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(profit_loss)}")
line5 = str(f"Average Change: ${str(round(average_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest__increase_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {greatest__decrease_date} (${str(greatest_decrease)})")


pyBank.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(
    line1, line2, line3, line4, line5, line6, line7))



