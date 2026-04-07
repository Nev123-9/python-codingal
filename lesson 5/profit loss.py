actual_cost =float(input("enter the actual cost"))
sales_amount =float(input("enter the sales amount"))



if sales_amount >actual_cost:
    amount=sales_amount-actual_cost
    print("total profit",amount)
else:
    print("no profit")




