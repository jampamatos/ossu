def fixPayBiSearch(balance, annualInterestRate):

    monthlyInterest = annualInterestRate / 12
    fixedPaymentLowerBound = balance / 12
    fixedPaymentUpperBound = (balance * (1 + monthlyInterest)**12)/12
    fixedPayment = (fixedPaymentUpperBound + fixedPaymentLowerBound) / 2
    unpaidBalance = balance
    epsilon = 0.01

    while abs(unpaidBalance) > epsilon:

        updatedBalance = balance
        fixedPayment = (fixedPaymentUpperBound + fixedPaymentLowerBound) / 2
        
        for i in range(0,12):
            unpaidBalance = updatedBalance - fixedPayment
            updatedBalance = unpaidBalance + (monthlyInterest * unpaidBalance)
        
        if updatedBalance > epsilon:
            fixedPaymentLowerBound = fixedPayment
        elif updatedBalance < epsilon:
            fixedPaymentUpperBound = fixedPayment

    return "Lowest Payment:", round(fixedPayment,2)

print(fixPayBiSearch(320000, 0.2)) # Lowest Payment: 29157.09
print(fixPayBiSearch(999999, 0.18)) # Lowest Payment: 90325.03