#sub
import os
import csv     # for reading the csv files
results = {}  # Creates a dictionary
data = os.path.join("C:\\Users\\antho\\Desktop\\pypypy\\03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv")
with open(data, newline='') as csvfile:
  # CSV reader specifies the delimiter and the variable that holds contents
  csvreader = csv.reader(csvfile, delimiter=',')
  # Read the header row first (skip this step if there is no header)
  csv_header = next(csvreader)
  # print(csv_header)
  # Read each row of data after the header
  #for row in csvreader:
      #print(row)
           #1st declare variable for row
  for row in csvreader:
      results[row[0]] = float(row[1])
  #line_count += 1
  #print(results)
  #print(results.keys())
  #print(results.values())
  #print(results.items())
# The total number of months included in the dataset
y = list(results.values())
print(len(y))
# The net total amount of "Profit/Losses" over the entire period
print(sum(results.values()))
# The average of the changes in "Profit/Losses" over the entire period
avg = sum(results.values()) / len(y)
print(avg)
# The greatest increase in profits (date and amount) over the entire period
#x = list(results.values())
maximum = max(results, key=results.get)
print(maximum, results[maximum])
# The greatest decrease in losses (date and amount) over the entire period
minimum = min(results, key=results.get)
print(minimum, results[minimum])