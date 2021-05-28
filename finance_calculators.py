
import math


#to determine whether the user requires an investment or loan calculation:

finance = input('''Choose either 'investment' or 'bond' from the menu below to proceed:
investment   - to caculate the amount of interest you'll earn on interest
bond         - to calculate the amount you'll have to pay on a home loan
:''')

#making the input by user case-insensitive. instead of using of using function casefold as we are only dealing with english words.
user_choice = finance.lower()

# Investment Calculation:

if user_choice == "investment":
        P = float(input("Enter the amount you are depositing: R "))
        r = float(input("Enter the current interest rate: "))/100
        t = float(input("How many years do you plan on investing: "))
        interest = input("Do you want simple or compound interest: ").lower()

        #Output if simple interest is selected

        if interest == "simple":
            A = P*(1+r*t)
            print(f"Total amount with simple interest is: R{A}")

        #Output if compound interest is selected    

        elif interest == "compound":
            A = P*math.pow((1+r),t)
            print(f"Total amount with compound interest is: R{A}")

# Loan Calculation:
elif user_choice == "loan":
        P = float(input("Enter the present value of the house: R "))
        i = float(input("Enter the current interest rate: "))/100
        n = float(input("How many months will it take to repay the loan: "))

        #Output loan amount payable per month
        x = ((i/12)*P)/(1-(1+(i/12))**(-n))
        print(f"The amount to be paid each month is: R{x}")
            
        
