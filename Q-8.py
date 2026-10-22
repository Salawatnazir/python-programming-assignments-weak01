#Question 8:Calculate Profit or Loss
#Input cost price and selling price. Display either:
#Profit and amount, or
#Loss and amount, or
#No Profit No Loss

cost_price = int(input("Enter the cost price Rs:"))
selling_price = int(input("Enter the selling price Rs:"))
print("Cost price is:",cost_price)
print("Selling price is:",selling_price)
print(" ")

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit is: Rs", profit)
elif selling_price < cost_price:
    loss = cost_price - selling_price
    print("Loss is: Rs", loss)
else:
    print("No Profit No Loss")




