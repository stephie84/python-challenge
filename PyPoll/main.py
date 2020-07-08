import csv,os

polls = os.path.join('Resources', 'election_data.csv')
output_file = os.path.join('Analysis', 'output.txt')

#Import csv file

with open(polls) as csv_file:
    csv_reader = csv.reader(csv_file)

# Strip header
    next(csv_reader)

#Define variables

    total_votes = 0
    candidates = []
    candidate_votes = {}
    percentage = 0
    

    


    for row in csv_reader:

        total_votes += 1

        candidate = row[2]

        if candidate not in candidates:
            candidates.append(candidate)
            candidate_votes[candidate] = 0
        
        
        candidate_votes[candidate] += 1

      

    output = ('\n\nElection Results\n' +
    '----------------------------\n' +
    "Total Votes: " + str(total_votes) + '\n' +
    '----------------------------\n') 

#The percentage of votes each candidate won and the total number of votes each candidate won
    for candidate in candidate_votes:
        output += (f"{candidate}: {round(candidate_votes[candidate] / (sum(candidate_votes.values()))*100, 2)} ({candidate_votes[candidate]})\n----------------------------\n")
    
#The winner of the election based on popular vote
    maxvotes = max(candidate_votes , key=candidate_votes.get)
    output += ("Winner: " + (maxvotes) +   '\n----------------------------')

    print(output)
    #Write data to txt file
    
    with open(output_file, "w") as txt_file:
        txt_file.write(output)