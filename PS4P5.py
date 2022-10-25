lstname = str(input("Enter last name "))
lvl = int(input("Enter job level "))
salary = float(input("Enter salary "))

if lvl >= 10:
  bnsrate = .25
elif lvl >= 5 and lvl <= 9:
  bnsrate = .2
else:
  bnsrate = .1

bonus = bnsrate*salary

print(lstname, "bonus:", bonus)
