revenue = int(input("Enter firm revenue: "))
costs = int(input("Enter firm costs: "))
n = revenue - costs

if n > 0:
    print("You are well done. You are in profit. You profit= " + f"{n}")
    rent = n/revenue
    print("You profitability= " + f"{rent}")
    employers = int(input("Enter number of employees "))
    employers_revenue = revenue/employers
    print("Profit you employers= " + f"{employers_revenue}")
else:
    if n < 0:
        print("You are loser. You profit= " + f"{n}")
    else:
        print("You are loser. You profit = 0")