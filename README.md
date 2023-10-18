# python-challenge
Candidate names are placed into, "candidate", list variable. List variables, "candidate_vote_count",  tallies condidate votes, and, "candidate_vote_percent", stores candidate votes as a percent of the total vote, contain elements that correspond directly to the position of the candidate in the, "Candidate", list variable. Doing this in a list format makes the code more reusable, because if you have three new candidates, all you have to do is change the name in the, "Candidates", list variable.

Program opens election results stored in the, "election_data.csv", then promptly removes the header. A for-loop cycles through the CSV line by line while tallying the popular/total votes. If statements compare the candidate name to the ballot, and adding one to that candidate's total. To determine the winner, a second set of If statements compare the candidate's vote total to that of the other candidates, the candidate with the most wins. Next the percent of popular vote is calculated for each candidate by dividing the votes each recevied by the total vote and multiplying by 100.

The output text file is created, which includes the, "write", parameter. Results are listed with, ", file", added, which writes the line to the output text file. Once the lines are written, the file is closed. To get the results to display at the terminal, the file is reopened with the, 'r', parameter and printed to the terminal.

*It should be noted that in the lines displaying the results, {"%.3f" % was added to the beginning of each, "candidate_vote_percent", variable. This was needed to format the floatin point result to three decimal ponts

Sources:
1) Enterprise DNA, "Python Write to File: A How-To Guide", Enterprise DNA Blog, https://blog.enterprisedna.co/python-write-to-file/ Accessed on 18 October 2023

2)Stack Overflow, "How can I format a decimal to always show 2 decimal places?", https://stackoverflow.com/questions/1995615/how-can-i-format-a-decimal-to-always-show-2-decimal-places , Accessed on 18 October 2023