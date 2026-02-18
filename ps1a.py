annual_salary = float(input("enter annual salary :"))
#user enters annual salary.

portion_saved = float(input("Enter the percent of your salary to save, as a decimal (> 0 and <= 1) :"))
# user enters portion he wnats to save.

Cost_of_house = float(input("enter the cost of dream house :"))
# user enters cost of house.

down_payment = 0.25 * Cost_of_house
# calculaes the downpayment for the house.

monthly_salary = annual_salary / 12
# calculates monthly salary

monthly_return = 0.04 / 12
# calculates monthly return on investment.

savings = 0

months = 0
while savings < down_payment:     # loop runs while the condition is true.
    
    savings += savings * monthly_return          # calculates savings on monthly return.
    
    savings += monthly_salary * portion_saved    # calculates savings on user entered portion.
    
    months+=1                                    # increases one month for each iteration.
    
print(f"no of months = {months}")                # prints no of months.