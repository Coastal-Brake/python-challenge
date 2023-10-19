import os
import csv

first_month="true"
total_months=0
total_balance=0
monthly_change=0
monthly_change_count=0
monthly_change_total=0
cur_month_value=0
pre_month_value=0
avg_change=0
greatest_increase=0
greatest_increase_date=""
greatest_decrease=0
greatest_decrease_date=""

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath, "r") as infile, open("budget_data_cleaned.csv", "w") as outfile:
   reader = csv.reader(infile)
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

print("Financial Analysis\n----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_balance}")
print(f"Average Change: ${"%.2f"%average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
