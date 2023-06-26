import math 
print("investment - to calculate the amount of interest you'll earn on your investment.")
print("bond- to calculate the amount you'll have to pay on a home loan")
X = input("Enter either 'investment' or 'bond' from the menu above to proceed:   ").lower()
value1 = "investment" 
value2 = "bond"
if X == value1:
    p = float(input("the amount of money to be deposited: "))
    r = float(input("the interest rate: "))/100
    t = float(input("number of years planned for investment: "))
    interest = input(" Either 'simple' or 'compound' interest: ")
    if interest == "simple":
        A= p*(1 + r*t)
        print(f"your amount is ${A}.00")
    elif interest == "compound":
        A = p * math.pow((1 + r),t)
        print(f"your amount is ${A}.00")
elif X == value2:
    p = float(input("present value of the house: "))
    i = float(input("the interest rate: "))/100/12
    n = float(input("number of months for repayment: "))
    R = float(i * p)/(1- (1 + i)** (-n))
    print(f"your monthly repayment value is {R}.00" )
else:
    print("Invalid response. please enter either of the options listed above")

print('adejoke')
