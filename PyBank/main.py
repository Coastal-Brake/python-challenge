import os
import csv
from pathlib import Path

first_month="true"
total_months=0 #total months in dataset
total_balance=0 #total accumulated 
monthly_change=0 #month to month change
monthly_change_count=0 #tally of months for which change was calculated
monthly_change_total=0 #total of all monthly changes
cur_month_value=0 #current monthly value
pre_month_value=0 #previous monthly value
greatest_increase=0
greatest_increase_date=""
greatest_decrease=0
greatest_decrease_date=""

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile:
   reader = csv.reader(csvfile, delimiter=",")
   next(reader, None)  # skip the headers

   for row in reader:
      total_months += 1
      total_balance+=int(row[1])
      if first_month=="true":
            first_month="false"
            pre_month_value=int(row[1])
      elif first_month=="false":
            cur_month_value=int(row[1])
            monthly_change=cur_month_value-pre_month_value
            pre_month_value=cur_month_value
            monthly_change_count+=1
      monthly_change_total+=monthly_change
      if monthly_change > greatest_increase:
            greatest_increase_date=row[0]
            greatest_increase=monthly_change
      elif monthly_change < greatest_decrease:
            greatest_decrease_date=row[0]
            greatest_decrease=monthly_change
average_change=monthly_change_total/(monthly_change_count)

f = open('analysis/output.txt', 'w')
print("Financial Analysis\n----------------------------", file=f)
print(f"Total Months: {total_months}", file=f)
print(f"Total: ${total_balance}", file=f)
print(f"Average Change: ${"%.2f"%average_change}", file=f)
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=f)
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=f)
f.close()
with open('analysis/output.txt', 'r') as f:
    print(f.read())