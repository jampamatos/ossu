def fixed_payment(balance, annualInterestRate):
    
    fixedMonthlyPay = 10
    unpaidBalance = balance

    while unpaidBalance > 0:

        updatedBalance = balance
        fixedMonthlyPay += 10

        for i in range(0,12):
            unpaidBalance = updatedBalance - fixedMonthlyPay
            updatedBalance = unpaidBalance + ((annualInterestRate/12) * unpaidBalance)
    return "Lowest Payment:", fixedMonthlyPay

print(fixed_payment(3329,0.2))      # Lowest Payment: 310
print(fixed_payment(4773,0.2))      # Lowest Payment: 440
print(fixed_payment(3926, 0.2))     # Lowest Payment: 360
print(fixed_payment(99999999, 0.2))