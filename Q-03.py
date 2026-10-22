#Question 3:Calculate Compound Interest
#Use the formula:CI = P * (1 + R/100)**T - P
#Where P = principal, R = rate, T = time

principal = float(input("Enter the principal amount"))
rate = float(input("Enter the interest rate"))
time = float(input("Enter the time in years"))
CI = principal * (1 +rate/100)**time - principal
print(CI)
