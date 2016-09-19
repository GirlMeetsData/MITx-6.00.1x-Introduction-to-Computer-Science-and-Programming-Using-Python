# Incrementing by 10

month = 0
balance = 5000
annualInterestRate = 0.18
monthlyPaymentRate = 0.02

# Paste your code into this box
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
