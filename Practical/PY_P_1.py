# To Calculate simple interast We have I = (P * R * T)/100
# I = Simple Interest
# P is the principal amount,
# R is the interest rate (in percentage),
# T is the time period (in years).
# For calculate Simple Interest rate R = (100 * I) / (P * T)

P = float(input("Enter Principle Amount : "))
I = float(input("Enter The Simple Interest : "))
T = float(input("Enter The time period (in years) : "))

R = (100 * I) / (P * T)
print("Simple Interest Rate is : ", R, "%") 