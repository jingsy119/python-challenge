import os
import csv

# specify the path to open the csv doc
csvpath = os.path.join("Resources", "budget_data.csv")

# open the csv doc
with open(csvpath, "r") as csvfile:
    csvreader = (csv.reader(csvfile, delimiter =","))
    # skip header row
    next(csvreader)
    # cast csvreader into a list
    data_list = list(csvreader)

    # initiate iteration for month as 0
    total_month = 0
    # initiate iteration for profit
    profit_sum = 0


    for row in data_list:
        # count iterations of month
        total_month = total_month + 1

        # add new number to previous number and assign to profit_sum; convert string to integer
        profit_sum += int(row[1])
    
    # set the first difference value as the absolute max for later comparison
    max_value = int(data_list[1][1]) - int(data_list[0][1])
    # set the first difference value as the absolute min for later comparison
    min_value = int(data_list[1][1]) - int(data_list[0][1])

    # find greatest increase and decrease in profit
    for counter in range(2, len(data_list)):
        profit_diff = int(data_list[counter][1]) - int(data_list[counter-1][1])
        
        if  profit_diff > max_value:
            max_value = profit_diff
            max_month = data_list[counter][0]
    
        if  profit_diff < min_value:
            min_value = profit_diff
            min_month = data_list[counter][0]    

    
    # find the first number in the profit column
    start_profit = int(data_list[0][1])
    # last number in the profit column
    end_profit = int(row[1])

    # average change is calculated as "(last profit # - first profit #)/(total # of month - 1)""
    average_change = round((end_profit-start_profit)/(total_month - 1), 2)

# write results to analysis.txt
output_path = os.path.join("Analysis", "analysis.txt")

lines = ["Financial Analysis", "------------------------", 
         f"Total Months: {total_month}", f"Total: $ {profit_sum}", f"Average Change: $ {average_change}", 
         f"Greatest Increase in Profits: {max_month} ($ {max_value})", f"Greatest Decrease in Profits: {min_month} ($ {min_value})"]

with open(output_path, "w") as txtfile:
    txtfile.write("\n".join(lines))

  
    print("Financial Analysis")
    print("--------------------------")      
    # display total number of months
    print(f"Total Months: {total_month}")
    # display sum of profit
    print(f"Total: $ {profit_sum}")
    print(f"Average Change: $ {average_change}")
    print(f"Greatest Increase in Profits: {max_month} ($ {max_value})")
    print(f"Greatest Decrease in Profits: {min_month} ($ {min_value})")

