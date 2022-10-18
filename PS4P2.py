pamt = float(input("Enter principal amount of CD "))
years = float(input("Enter years until maturity "))

if pamt > 100000 and years == 5:
  intrst = 0.06
elif pamt >= 50000 and pamt <= 100000 and years == 10:
  intrst = 0.05
elif pamt >= 50000 and pamt <= 100000 and years == 5:
  intrst = 0.04
else:
  intrst = 0.02

print("Principal amount is", pamt, "the interest rate is", intrst*100, "% and the interest amount for the first year is", intrst*pamt+pamt)
