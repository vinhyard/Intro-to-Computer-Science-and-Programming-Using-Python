balance = 3329
annualInterestRate = 0.2
will = 0

x = 0
while balance >= 0:
    if x == 12 and balance <= 0:
        print('Lowest Payment:', will)
        break
    elif x == 12 and balance > 0:
        will += 10
    else: 
        balance = (balance - will) + ((annualInterestRate/12) * (balance - will))
        will += 10
        x = x + 1


