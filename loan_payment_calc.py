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


# Determining the lowest equal monthly payments needed ot pay off the balance within one year; increments by 10 each time

monthlyPaymentRate = 10
monthlyInterestRate = annualInterestRate/12.0
orig_balance = balance
while True:
    month = 0
    balance = orig_balance #defined
    for month in range(12):
        balance -= monthlyPaymentRate        
        balance = (monthlyInterestRate * balance) +balance
    if balance <= 0:
        print('Lowest payment: ' + str(round(monthlyPaymentRate,2)))
        break
    else:
        monthlyPaymentRate += 10
        
# Determining the lowest equal monthly payments needed ot pay off the balance within one year; using bisection search

origBalance = balance
monthlyInterestRate = annualInterestRate/12.0 
lowerBound = balance/12.0
upperBound = (balance * (1 + monthlyInterestRate)**12)/12.0
counter = 0
while True:
    balance = origBalance
    monthlyPaymentRate = float((lowerBound+upperBound)/2)
    for month in range(12):
        balance -= monthlyPaymentRate        
        balance = (monthlyInterestRate * balance) + balance        
    if balance <= 0.009 and balance >= 0.001:
        print('Lowest payment: ' + str(round(monthlyPaymentRate,2)))
        break
    elif balance < 0: 
        upperBound = monthlyPaymentRate
    elif balance > 0:
        lowerBound = monthlyPaymentRate


