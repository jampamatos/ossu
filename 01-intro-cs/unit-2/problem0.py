from signal import pause


def card_payment(balance, payment):
    unpaid_balance = round(balance - payment, 2)

    if unpaid_balance == 0:
        print("You have completely paid your credit card balance.")
    else:
        interest = 0.18/12 * unpaid_balance
        remaining_payment = unpaid_balance + interest
        minimum_payment = remaining_payment * 0.02
        print("You have paid $" + str(round(payment, 2)) + "." )
        print("The interest value is $" + str(round(interest)) + ".")
        print("Next month credit card value is of $" + str(round(remaining_payment,2)) + ", with a minimum payment of $" + str(round(minimum_payment, 2)) + ".")
    return remaining_payment

print(card_payment(5000, 100))
print(card_payment(4973.5, 99.47))