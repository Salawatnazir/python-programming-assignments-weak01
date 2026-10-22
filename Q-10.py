# Question 10:# Salary Calculator
# Input basic salary. Calculate:
#  HRA = 20% of basic
#  DA = 15% of basic
#  Total Salary = Basic + HRA + DA

basic_salary = float(input("Enter your basic salary: "))

hra = basic_salary * 20 / 100
da = basic_salary * 15 / 100

total_salary = basic_salary + hra + da

print("Basic Salary:", basic_salary)
print("HRA:", hra)
print("DA:", da)
print("Total Salary:", total_salary)
