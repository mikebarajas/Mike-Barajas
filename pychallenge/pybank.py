import csv

# Files to load and output (Remember to change these)
file_to_load = "budget_data_1.csv"
file_to_output = "budget_analysis_1.txt"

# Read the csv and convert it into a reader

with open(file_to_load,"r") as f:
    reader = csv.reader(f,delimiter = ",")
    data = list(reader)[1:] 
    
    # Create two empty lists to populate
    revenue = []

    revenue_change = []
    # difference = int(data(row[1]))

    for row in data:
        # Populate revenue list and slice out the header
        revenue.append((row[1]))
        # convert list of strings into list of integers
        revenue = list(map(int, revenue)) 

change = 0
change = int(change)
previous_row = revenue[0]

for row in revenue:
    change = row - previous_row
    revenue_change.append((change))
    previous_row = row

revenue_change = revenue_change[1:]
revenue_change = list(map(int, revenue_change)) 

# Row count without the headers will give you the total number of months. 
row_count =  len(revenue) 
# Now that the revenue list is converted to integers, I can sum the row to dete1rmine the total revenue for the spread sheet
total_revenue = sum(revenue) 
# Determine the average change between months
total_change = sum(revenue_change)
total_change = int(total_change)
number_of_changes = len(revenue[1:])
number_of_changes = int(number_of_changes)
average_change = total_change / number_of_changes

# Make of new list of the changes by months

month2 = []

for row in data:
        # Populate revenue list and slice out the header
    month2.append((row[0]))
        # convert list of strings into list of integers
    
        
         
month2 = month2[1:]
month_changes = [
     ("Month", [month2]),
     ("Changes in Revenue", [revenue_change])]

# Determine the Maximun and Minumum monthly revenue in the list

Max = max(revenue)
Min = min(revenue)
Max2 = max(revenue_change)
Min2 = min(revenue_change)   



for row in data:
    if row[1] == str(Max):
        max_row = row

for row in data:
    if row[1] == str(Min):
        min_row = row

keys = month2
values = revenue_change
dictionary = dict(zip(keys, values))



# Print Output
print(" Financial Analysis ----------------------------")
print("      Total Months - ", row_count)
print("      Total Reveue- ", total_revenue)
print("      Average Revenue Change- ", average_change)
print("      Month with the Greatest Revenue- ", max_row)
print("      Month with the Lowest Revenue- ", min_row)
print("      Greatest Increase in Revenue- ", max(dictionary), Max2)
print("      Greatest Decrease in Revenue- ", min(dictionary), Min2)




