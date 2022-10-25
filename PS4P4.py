quant = int(input("Enter quantity of tickets "))

if quant >= 25:
  price = 50
elif quant >= 10 and quant <= 24:
  price = 60
elif quant >= 5 and quant <= 9:
  price = 70
elif quant < 5:
  price = 75

total = quant*price

print("The number of tickets is", quant, "the price of each ticket is", price, "and the total cost is", total)
