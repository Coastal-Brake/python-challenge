# python-challenge

--------Pypoll---------- 
Candidate names are placed into the, "candidate", list,candidate vote tallies are stored in the, "candidate_vote_count", list, and votes as a percent of the total vote are stored in the, "candidate_vote_percent" list. These lists contain elements that correspond directly to the position of the candidate in the, "Candidate", list variable. Doing this in a list format makes the code more reusable since you are not creating unique labels. So, if you have three new candidates, all you have to do is change the name in the, "Candidates", list variable, then everything lines up. The code makes this easier to understand

Program opens election results stored in the, "election_data.csv", then promptly removes the header. A for-loop cycles through the CSV line by line while tallying the popular/total votes. If statements compare the candidate name to the ballot, then adds one to that candidate's total. To determine the winner, a second set of If statements compare the candidate's vote total to that of the other candidates, the candidate with the most wins. Next the percent of popular vote is calculated for each candidate by dividing the votes each recevied by the total vote and multiplying by 100.

The output text file is created, which includes the, "write", parameter. Results are listed with, ", file", added, which writes the line to the output text file. Once the lines are written, the file is closed. To get the results to display at the terminal, the file is reopened with the, 'r', parameter and printed to the terminal.

*It should be noted that in the lines displaying the results, {"%.3f" % was added to the beginning of each, "candidate_vote_percent", variable. This was needed to format the floatin point result to three decimal ponts

---------pybank------

Program begins by opening financial data stored in the, "budget_data.csv", then promptly removes the header, and begins cycling through the csv file row by row using a for-loop. A counter is used to count the months in the dataset, and a totalizer adds each month's balance to itself.

Typically the monthly change, current monthly change subtracted by the previous monthly change is subtracted. However, the first loop cycle requires a special operation since we don't have a previous month value yet. To account for this, an if conditional is used the first time through that checks the, "first_month", variable. If, "First_month", is true, "pre_month_value", equals the row1 value, and the monthly change calculation is ignored. At the end of the loop, "first_month", is changed to false. With, "first_month", being false, the monthly change is calculated and totalized cycle by cycle, and, "monthly_change_count", the number of months a monthly change is calculated, is incremented by one. Once we have the monthly change, we can begin figuring out the greatest increase and decrease values. This operation is performed by comparing the current monthly change to the stored greatest monthly change, and if the monthly change is greater, or lesser, it writes over the contents, then date is recorded. Once all of the monthly changes have been totalized, it is then divided by the total monthly change months to give us the monthly change average.

Next, output text file is created, which includes the, "write", parameter. Results are printed with, ", file", added, which writes the line to the output text file. Once the lines are written, the file is closed. To get the results to display at the terminal, the file is reopened with the, 'r', parameter and printed to the terminal.

*It should be noted that in the lines displaying the results, {"%.2f" % was used to format the decimal points. This was needed to format the floatin point result to three decimal ponts

Sources:
1) Enterprise DNA, "Python Write to File: A How-To Guide", Enterprise DNA Blog, https://blog.enterprisedna.co/python-write-to-file/ Accessed on 18 October 2023

2)Stack Overflow, "How can I format a decimal to always show 2 decimal places?", https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places , Accessed on 18 October 2023
goigjioa jmio[re[kla;lkmdfkm;'lbvmiogriaergm'g,og,oerp,gapgm  jgjggjggfvbmkmkmvmrkavk'lakdjjjjjjjj89jhuoouyboaeiomervc]]