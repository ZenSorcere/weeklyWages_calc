# File: weeklyWages_calc.py
# Desc: a program designed to take input of hours worked and wage rate,
#       and calculate total weekly wages, accounting for overtime pay.
# Class: ITC 110 (summer)
# Author: Mike Gilson
# Date: 8/3/19


# defining the main function:
def main():

    # introduce user to program and ask for input for hours and hourly rate of pay
    print("Calculate your weekly pay: \n")
    hours = float(input("Enter the amount of hours worked for the week: "))
    wage = float(input("Enter your hourly wage: "))

    # define variable for weekly pay
    pay = hours*wage

    # define variable for how many hours are overtime hours, and multiplying those by "time and a half"
    overtime = (hours-40)*(wage*1.5)

    # defining variable for combining maximum base pay amount, plus overtime pay
    totalPay = (40*wage)+overtime
    
    # set up if/elif statement:
    #     inform user what their weekly pay is, based on if hours are 40 or less.
    # Because I want all numerical values to display as strings, but give me a standard of two decimal places,
    #     I used string formatting to enforce the desired two decimal places.
    if hours <= 40:
        print("For working " + "{:.2f}".format(hours) + " hours, your weekly pay, before taxes, is " + "${:.2f}".format(pay) + ".")

    # Or, if more than 40 hours, inform user what their overtime amount is, along with their grand total pay,
    #     again using string formatting to enforce the desired two decimal places.
    elif hours > 40:
        print("For working " + "{:.2f}".format(hours) + " hours, your weekly pay, before taxes, is " + "${:.2f}".format(40*wage) +
              " at normal rate, plus " + "${:.2f}".format(overtime) + " for " + "{:.2f}".format(hours-40) + " hours of overtime, for a total of "
              + "${:.2f}".format(totalPay) + ".")


# Guarantees that the main will automatically run when the program is
#     invoked directly, but not if the module is imported.
if __name__ == '__main__':
    main()

    
