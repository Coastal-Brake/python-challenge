import os
import csv

total_months=0
total_balance=0
profit=0
profit_avg=0
change_monthly=int([0,0,0])
value_current=0
value_prev=0
value_prev_set=False

greatest_profit=0
greatest_profit_date=str
loss=0
loss_avg=0
greatest_loss=0
greatest_loss_date=str
net_change=0
csvpath = os.path.join("Resources", "budget_data.csv")
#csvpath_bonus = os.path.join("..", "Resources", "cereal_bonus.csv")

with open(csvpath, "r") as infile, open("budget_data_cleaned.csv", "w") as outfile:
   reader = csv.reader(infile)
   next(reader, None)  # skip the headers
   for row in reader:
        total_months += 1
        total_balance+=int(row[1])
        #use list to hold current and past balance changes, balance[0]=current, balance[1]=previou, balance{}
        if monthly_change_init==false
        if  int(row[1])>0:
            profit+=int(row[1])

            if int(row[1]) > greatest_profit:
                   greatest_profit=int(row[1])
                   grestest_profit_date=greatest_profit_date=row[0]

        elif int(row[1])<0:
            loss+=int(row[1])
            if  int(row[1])<greatest_loss:
                greatest_loss=int(row[1])
                greatest_loss_date=greatest_loss_date=row[0]
        
        #print(row[0],row[1])

profit_avg=profit/total_months
loss_avg=loss/total_months
net_change=profit_avg+loss_avg
print(greatest_profit)
print(greatest_profit_date)
print(greatest_loss)
print(greatest_loss_date)
#print(total_months)
#print(total_balance)
#print(profit)
#print(loss)
#print(net_change)
#print(profit_avg)
#print(loss_avg)
        #print(row[0],row[1])
   #print(row[0],row[1])
#output_file = os.path.join("budget_data_final.csv")
#with open(output_file, "w", newline='') as datafile:
#    writer = csv.writer(datafile)
#    output_file = os.path.join("budget_data_final")
#    writer.writerows(row[0],row[1])