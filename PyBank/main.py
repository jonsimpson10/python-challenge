
import os
import csv

total = 0
month_count = 0
month = []
revenue_change = []
profit = []


# Set path for file
csvpath = os.path.join("..", "Resources", "budget_data.csv")


# Open the CSV
with open(csvpath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")

# Set Header row
  header = next(csvreader)
#Sum the values in the profit column
 
  for row in csvreader:
    revenue = row[1]
    total += int(revenue)
    month_count += 1 
    month.append(str(row[0]))
    profit.append(float(row[1]))

  for i in range(1, len(profit)):
    
    revenue_change.append(profit[i] - profit[i-1])
    avg_change = sum(revenue_change)/len(revenue_change)
    max_profit = max(revenue_change)
    min_profit = min(revenue_change)
    max_date = str(month[revenue_change.index(max_profit)+1])
    min_date = str(month[revenue_change.index(min_profit)+1])
      



print("Financial Analysis")
print("-----------------------")
print("Total months: " + str(month_count))
print("Total profit: $" + str(total))
print("Average change: " + str(avg_change))
print("Greatest profit: " + max_date + " ($" + str(max_profit) + ")")
print("Greatest loss: " + min_date + " ($" + str(min_profit) + ")")

with open("analysis.txt", "w") as txt:
  print("Financial Analysis", file=txt)
  print("-----------------------", file=txt)
  print("Total months: " + str(month_count), file=txt)
  print("Total profit: $" + str(total), file=txt)
  print("Average Profit: " + str(avg_change), file=txt)
  print("Greatest profit: " + max_date + " ($" + str(max_profit) + ")", file=txt)
  print("Greatest loss: " + min_date + " ($" + str(min_profit) + ")", file=txt)

