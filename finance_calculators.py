import math

# HEADLINE
print("Financial calculator\n")

# INFORMATION ABOUT INVESTMENT AND BOND
print("Investment - to calculate the amount of interest you'll earn on your"
    "investment"
)
print("Bond - to calculate the amount you'll have to pay on a home"
    " loan \n"
)

user_input = input(
    "Enter 'investment' or 'bond' from the menu above to proceed: "
)
# IF THE USER CHOOSE INVESTMENT IF STATEMENT RUNS
if user_input.lower() in ["investment"]:
    # DID DO SOME RESEARCH ON HOW TO MAKE THIS STATEMENT SHORTER RATHER THAN
    # if user_input == "investment" or user_input == "Investment" or user_input
    # == "INVESTMENT" or user_input == "bond" or user_input == "Bond" or 
    # user_input == "BOND":
    
    # INFORMATION COLLECTED FROM USER IF INVESTMENT IS CHOSEN
    deposit = float(input("How much money are you depositing R "))
    rate = float(input("Enter the interest rate (only 8): "))
    years = int(input("How many years do you plan on investing: "))
    interest = input("simple or compound: ")
    
 
    # INTEREST VARIABLE INPUT WILL BE CHOSEN TO RUN NEXT IF STATEMENT
    if interest == "simple":
        # SIMPLE INTEREST CALCULATIONS AND OUTPUT
        total_amount = deposit * (1 + (rate / 100) * years)
        
        print(
            f"The total amount after {years} years with the simple interest" 
            f" is: R{total_amount}"
        )
    # COMPOUND INTEREST CALCULATIONS AND OUTPUT
    elif interest == "compound":
        total_amount = (deposit * math.pow((1 + (rate / 100)), years))
        print(
            f"The total amount after {years} years with the compound interest"
            f" is: R{round(total_amount, 2)}"
        )
    # PRINT IF NO INPUT OR WRONGLY INPUT RECEIVED
    else:
        print("Please enter a valid option. 'simple' or 'compound'")

# INFORMATION COLLECTED FROM USER IF THE USER CHOSE BOND
if user_input.lower() in ["bond"]:

    house_value = float(input("Please present the value of the house: "))
    rate = float(input("enter the interest rate: "))
    months_amount = int(input("Total months to repay: "))

    # CALCULATION OF BOND REPAYMENT
    monthly_rate = (rate / 100) / 12
    repayment = (monthly_rate * house_value) / (1 - (1 + monthly_rate) ** (-months_amount))
    
    # OUTPUT OF BOND CALCULATION
    print(f"You will have to repay R{round(repayment, 2)} each month.")
else:
    print("Please enter a valid option. 'investment' or 'bond'")
    