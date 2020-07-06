import csv,os

file = os.path.join('Resources', 'budget_data.csv')

#Import csv file

with open(file) as csv_file:
    csv_reader = csv.reader(csv_file)

# Strip header
    next(csv_reader)

# Initialize variables
    months = 0
    total = 0
    avg = 0
    diff = 0
    total_diff = 0
    curr_row = 0
    prev_row = 0
    initial_value = 0
    greatest_increase = 0
    greatest_decrease = 0
    greatest_increase_month = " "
    greatest_decrease_month = " "


    for row in csv_reader:

# Total number of months included in the dataset
        months += 1
        total += int(row[1])

# Net total amount of Profit/Losses over the entire period
        curr_row = int(row[1])

 #Greatest increase and decrease in P&L so far

        diff = (curr_row - prev_row)
        if prev_row == 0:
            diff = 0
        total_diff += diff

        if diff > greatest_increase:
            greatest_increase = diff
            greatest_increase_month = str(row[0])

        if diff < greatest_decrease:
            greatest_decrease = diff
            greatest_decrease_month = str(row[0])

        prev_row = int(row[1])


    # total_diff -= initial_value
    # total_diff = 

    avg = int( total_diff / (months - 1) ) 

    print('\n\nFinancial Analysis')
    print('----------------------------')
    print('Total Months: ' + str(months))
    print('Total: $' + str(total))
    print ("Average Change: $" + str(avg))
    print ("Greatest Increase in Profits: " + greatest_increase_month + " " + "($" + str(greatest_increase) +")")
    print ("Greatest Decrease in Profits: " + greatest_decrease_month + " " + "($" + str(greatest_decrease) +")")

    
    #print ("Total Monthly Diff: $" + str(initial_value))