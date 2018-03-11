import os
import csv

#Eric Madigan = PyPoll for Python-Challenge 

# Set Path to our excel file with all the data and save it as a file 
file = os.path.join('election_data_2.csv')


#Create a dictionary to use for the candidate names and vote count. 
poll = {}

#Create a variable for total votes and set the intial count to 0 so we can add on it 
total_votes = 0

#Open up and read the csv file 
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)

#skip the header line so we can get into the actual data 
    next(csvread, None)

#creates dictionary from file using column 3 as keys, using each name only once

#counts votes for each candidate as an entry

#Keep a total vote count by adding one after each loop
    for row in csvread:
        total_votes += 1
        if row[2] in poll.keys():
            poll[row[2]] = poll[row[2]] + 1
        else:
            poll[row[2]] = 1
 
#Here we create an empty list for the candidates and the associated vote count
candidates = []
num_votes = []

#takes dictionary keys and values and dumps them into the lists as candiates and the number of votes 
for key, value in poll.items():
    candidates.append(key)
    num_votes.append(value)

# creates vote percent list
vote_percent = []
for n in num_votes:
    vote_percent.append(round(n/total_votes*100, 1))

# zips candidates, num_votes, vote_percent into tuples
clean_data = list(zip(candidates, num_votes, vote_percent))

#creates winner_list to put winners (even if there is a tie)
winner_list = []

for name in clean_data:
    if max(num_votes) == name[1]:
        winner_list.append(name[0])

# makes winner_list a string with the first entry 
winner = winner_list[0]

#only runs if there is a tie and puts additional winners into a string separated by commas
if len(winner_list) > 1:
    for w in range(1, len(winner_list)):
        winner = winner + ", " + winner_list[w]

#Print out to our text file 
output_file = os.path.join('Election_Output.txt')

with open(output_file, 'w') as txtfile:
    txtfile.writelines('Election Results \n------------------------- \nTotal Votes: ' + str(total_votes) + 
      '\n-------------------------\n')
    for entry in clean_data:
        txtfile.writelines(entry[0] + ": " + str(entry[2]) +'%  (' + str(entry[1]) + ')\n')
    txtfile.writelines('------------------------- \nWinner: ' + winner + '\n-------------------------')

#Print our file to the terminal using read 
with open(output_file, 'r') as readfile:
    print(readfile.read())
