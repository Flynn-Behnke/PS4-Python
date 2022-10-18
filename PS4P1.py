quant = int(input("Enter quantity of widgets "))

if quant > 10000:
  price = 10.00
elif quant >= 5000 and quant <= 10000:
  price = 20.00
elif quant < 50000:
  price = 30.00

extprice = price*quant
tax = extprice*0.07
total = extprice+tax
print("Extended price is", extprice, "tax is ", tax, "and the total is ", total)
