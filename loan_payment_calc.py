# Finding balance after 12 months based on only making the minimum monthly payment
month = 0
while month <= 12:
    if balance != 0:
        monthlyInterestRate = annualInterestRate/12.0
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        newBalance = (monthlyInterestRate * unpaidBalance) + unpaidBalance
    
    if month == 12:
        print('Remaining balance: ' + str(round(balance,2)))
    
    month += 1 
    balance = newBalance


# Incrementing by 10
month = 0
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

month = 0
while month <= 12:
    if balance != 0:
        monthlyInterestRate = annualInterestRate/12.0
        minimumPayment = balance * monthlyPaymentRate
        unpaidBalance = balance - minimumPayment
        newBalance = (monthlyInterestRate * unpaidBalance) + unpaidBalance
    
    if month == 12:
        print(round(balance/12,2))

    month += 1 
    balance = newBalance
