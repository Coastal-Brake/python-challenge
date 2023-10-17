import array
import os
import csv
import statistics

total_months=0
total_balance=0
monthly_change=0
monthly_change_list=[]
profit_days=0
loss_days=0
total_monthly_change=0
cur_month_value=0
pre_month_value=0
total_profits_list=[]
total_losses_list=[]
total_profits=0
total_losses=0
avg_change=0
greatest_increase=0
greatest_increase_date=""
greatest_decrease=0
greatest_decrease_date=""
i=0
csvpath = os.path.join("Resources", "budget_data.csv")
#csvpath_bonus = os.path.join("..", "Resources", "cereal_bonus.csv")

with open(csvpath, "r") as infile, open("budget_data_cleaned.csv", "w") as outfile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers
   for row in reader:
        total_months += 1
        total_balance+=int(row[1])
        pre_month_value=cur_month_value
        cur_month_value=int(row[1])
        monthly_change=cur_month_value-pre_month_value
        monthly_change_list.append(monthly_change)
        total_monthly_change+=monthly_change
        if monthly_change>0:
              total_profits+=int(row[1])
              total_profits_list.append(monthly_change)
              profit_days+=1
        elif monthly_change<0:
              total_losses+=int(row[1])
              total_losses_list.append(monthly_change)
              loss_days+=1
        if monthly_change > greatest_increase:
                greatest_increase_date=row[0]
                greatest_increase=monthly_change
        elif monthly_change < greatest_decrease:
                greatest_decrease_date=row[0]
                greatest_decrease=monthly_change

profits_ave=statistics.mean((total_profits_list))
losses_ave=statistics.mean((total_losses_list))
average_change=profits_ave+losses_ave
print(f"total profits: {total_profits}")
print(f"total profit days: {profit_days}")
print(f"total profit days ave: {profits_ave}")
print("----------------------------")
print(f"total losses: {total_losses}")
print(f"total loss days: {loss_days}")
print(f"total loss days ave: {losses_ave}")
print("----------------------------")
print(average_change)
print("----------------------------")
#print(average_change)
#print(profits_ave)
#print(profit_days)
#print(loss_days)
#print(losses_ave)
#print(average_change)
print("Financial Analysis\n\n----------------------------\n")
print(f"Total Months: {total_months}")
print(f"Total: {total_balance}")
print(f"Average Change: ${average_change}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")
