import csv,os

polls = os.path.join('Resources', 'election_data.csv')

#Import csv file

with open(polls) as csv_file:
    csv_reader = csv.reader(csv_file)

# Strip header
    next(csv_reader)

#Define variables

    total_votes = 0
    
    
#Create a complete list of candidates who received votes
    
#The percentage of votes each candidate won

#The total number of votes each candidate won

#The winner of the election based on popular vote

    for row in csv_reader:

        total_votes += 1


        

        


    print('\n\nElection Results')
    print('----------------------------')
    print("Total Votes: " + str(total_votes))
    print('----------------------------')
    