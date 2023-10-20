import os
import csv

total_votes=0
candidate=["Charles Casper Stockham","Diana DeGette","Raymon Anthony Doane"]
candidate_vote_count=[0,0,0] #elements correlate with, "candidate", list element
candidate_vote_percent=[0,0,0] #elements correlate with, "candidate", list element
winner_winner_chicken_dinner="" 

csvpath = os.path.join("Resources", "election_data.csv")

with open(csvpath, "r") as csvfile:
   reader = csv.reader(csvfile, delimiter=",")
   next(reader, None)  # skip the headers

   for row in reader:
        total_votes += 1 
        #tallies popular vote count row by row, if candidate name matches
        #they are given one vote
        if candidate[0]==row[2]:
            candidate_vote_count[0]+=1 #they are given one vote
            
        elif candidate[1]==row[2]:
            candidate_vote_count[1]+=1
            
        elif candidate[2]==row[2]: 
            candidate_vote_count[2]+=1
 #once votes are tallied, if conditionals are used to determine who won           
if candidate_vote_count[0] > candidate_vote_count[1] and candidate_vote_count[2]:
    winner_winner_chicken_dinner=candidate[0]   
elif candidate_vote_count[1] > candidate_vote_count[2] and candidate_vote_count[0]:
    winner_winner_chicken_dinner=candidate[1]  
elif candidate_vote_count[2] > candidate_vote_count[0] and candidate_vote_count[1]:
    winner_winner_chicken_dinner=candidate[2] 

#calculates candidate vote as a percentage of the popular vote
candidate_vote_percent[0]=100*candidate_vote_count[0]/total_votes
candidate_vote_percent[1]=100*candidate_vote_count[1]/total_votes
candidate_vote_percent[2]=100*candidate_vote_count[2]/total_votes

f = open('analysis/output.txt', 'w') #creates output txt file
print("Election Results", file=f)
print("-------------------------", file=f)
print(f"total votes: {total_votes}", file=f)
print("-------------------------", file=f)
print(f"{candidate[0]}: {"%.3f" % candidate_vote_percent[0]}% ({candidate_vote_count[0]})", file=f)
print(f"{candidate[1]}: {"%.3f" % candidate_vote_percent[1]}% ({candidate_vote_count[1]})", file=f)
print(f"{candidate[2]}: {"%.3f" % candidate_vote_percent[2]}% ({candidate_vote_count[2]})", file=f)
print("-------------------------", file=f)
print(f"Winner: {winner_winner_chicken_dinner}", file=f)
print("-------------------------", file=f)
f.close()
with open('analysis/output.txt', 'r') as f: #opens text file
    print(f.read())
