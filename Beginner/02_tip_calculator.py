print("Welcome to tip calculator")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10,12,or 15?"))
people=int(input("How many person should pay: "))
bill_with_tip=(tip/100*bill)+bill
final=round(bill_with_tip/people,2)
final="{:.2f}".format(final)
print(f"Each person should pay: ${final}")