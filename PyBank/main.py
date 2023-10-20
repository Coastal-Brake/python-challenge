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
      
      #for the first monh the first row needs to be read in as the previous month value 
      if first_month=="true":
           pre_month_value=int(row[1])  
           #after first month, monthly change begins calculation 
      elif first_month=="false":      
            cur_month_value=int(row[1]) #
            monthly_change=cur_month_value-pre_month_value #current
            pre_month_value=cur_month_value #once the change calculation is complete
            monthly_change_count+=1
            monthly_change_total+=monthly_change
      #greatest values are replaced by the monthly change each they are greater
      # and the date is recorded
      if monthly_change > greatest_increase: 
            greatest_increase_date=row[0]
            greatest_increase=monthly_change
      elif monthly_change < greatest_decrease:
            greatest_decrease_date=row[0]
            greatest_decrease=monthly_change
      first_month="false" #first month is complete
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