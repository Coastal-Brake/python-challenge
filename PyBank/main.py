import os
import csv
from pathlib import Path

first_month="true" #first month flag
total_months=0 #total months in dataset
total_balance=0 #total accumulated 
monthly_change=0 #month to month change
monthly_change_count=0 #tally of months for which change was calculated
monthly_change_total=0 #total of all monthly changes
cur_month_value=0 #current monthly value
pre_month_value=0 #previous monthly value
greatest_increase=0 #greatest monthly increase value
greatest_increase_date="" #date of greatest monthly increase
greatest_decrease=0 #greatest monthly decrease value
greatest_decrease_date="" #date of greatest monthly decrease

csvpath = os.path.join("Resources", "budget_data.csv")

with open(csvpath) as csvfile: 
   reader = csv.reader(csvfile, delimiter=",")
   next(reader, None)  # skip the headers

   for row in reader:              
      total_months += 1             #month tally 
      total_balance+=int(row[1])    #row value is added to the balance each loop cycle
      if first_month=="true":     #first row needs to be read in as the previous month value 
            first_month="false"      #ow 1 read in as previous month value otherwise the calculation
            pre_month_value=int(row[1]) #wrong
      elif first_month=="false":      #after first month
            cur_month_value=int(row[1]) #
            monthly_change=cur_month_value-pre_month_value #current
            pre_month_value=cur_month_value #once the change calculation is complete, the current month variable is moved into the previous month
            monthly_change_count+=1 #monthly change begins calculation after the first calculation
      monthly_change_total+=monthly_change #compares monthly change each loop,
      if monthly_change > greatest_increase: #replaced each time it is greater
            greatest_increase_date=row[0]    #stores date
            greatest_increase=monthly_change
      elif monthly_change < greatest_decrease:
            greatest_decrease_date=row[0]
            greatest_decrease=monthly_change
average_change=monthly_change_total/monthly_change_count #calculates change average

f = open('analysis/output.txt', 'w') #creates output txt file
print("Financial Analysis\n----------------------------", file=f) #each line is written to file
print(f"Total Months: {total_months}", file=f)
print(f"Total: ${total_balance}", file=f)
print(f"Average Change: ${"%.2f"%average_change}", file=f)
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})", file=f)
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})", file=f)
f.close() #closes text file
with open('analysis/output.txt', 'r') as f: #opens text file
    print(f.read()) #displays it in the terminal box