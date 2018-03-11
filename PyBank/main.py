import csv
import os

#Eric Madigan = PyBank for Python-Challenge 

# Here we are creating our file path and saving it as a file
file = os.path.join('budget_data2.csv')

# Creating empty list for our data in the columns
months = []
revenue = []

#Read csv with csv.reader and parse csv into lines
with open(file, 'r') as csvfile:
    csvread = csv.reader(csvfile)
    
    next(csvread, None)

    for row in csvread:
        months.append(row[0])
        revenue.append(int(row[1]))

#Figuring out our total amount of months 
total_months = len(months)

#create greatest increase, decrease variables and set them equal to the first revenue entry
#set total revenue = 0 
greatest_inc = revenue[0]
greatest_dec = revenue[0]
total_revenue = 0

#loop through revenues and compare each revenue against the next to fine the Biggest and smallest revenue number
#While we loop we add the revenues together to get the total revenue
for r in range(len(revenue)):
    if revenue[r] >= greatest_inc:
        greatest_inc = revenue[r]
        great_inc_month = months[r]
    elif revenue[r] <= greatest_dec:
        greatest_dec = revenue[r]
        great_dec_month = months[r]
    total_revenue += revenue[r]

#calculate average_change for our revenue
average_change = round(total_revenue/total_months, 2)

#sets path for output file
output_dest = os.path.join('Output.txt')

# opens our Output.text destination and prints the summary for the data 
with open(output_dest, 'w') as writefile:
    writefile.writelines('Financial Analysis\n')
    writefile.writelines('----------------------------' + '\n')
    writefile.writelines('Total Months: ' + str(total_months) + '\n')
    writefile.writelines('Total Revenue: $' + str(total_revenue) + '\n')
    writefile.writelines('Average Revenue Change: $' + str(average_change) + '\n')
    writefile.writelines('Greatest Increase in Revenue: ' + great_inc_month + ' ($' + str(greatest_inc) + ')'+ '\n')
    writefile.writelines('Greatest Decrease in Revenue: ' + great_dec_month + ' ($' + str(greatest_dec) + ')')

#opens the output file in read mode and prints to the terminal 
with open(output_dest, 'r') as readfile:
    print(readfile.read())
