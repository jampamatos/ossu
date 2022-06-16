def remaining_balance (balance, annualInterestRate, monthlyPaymentRate):
    '''
    balance: int or float, the outstanding value of the credit card
    annInterest: float, annual interest rate as a decimal
    monthPaym: float, minimum monthly payment rate as a decimal

    returns: the remaining balance to pay off credit card balance after 12 months, with two decimals of accuracy.
    '''

    minimum_payment = balance * monthlyPaymentRate
    unpaid_balance = balance - minimum_payment
    interest = (annualInterestRate/12) * unpaid_balance

    for i in range(0,12):
        new_balance = unpaid_balance + interest
        minimum_payment = new_balance * monthlyPaymentRate
        unpaid_balance = new_balance - minimum_payment
        interest = (annualInterestRate/12) * unpaid_balance
    return 'Remaining balance:', round(new_balance,2)

remaining_balance(42,0.2,0.04)