print("Welcome to the tip calculator")
bill=float(input("What was the total bill ?"))
tip=float(input("How much percent tip would like to give? 10, 12 or 15 ?"))
total_person=int(input("How much people to split the bill?"))
eachbill=(bill+(tip*bill/100))/total_person
print(f"Each person should pay : {eachbill}")

OutPut:
Welcome to the tip calculator
What was the total bill ?500
How much percent tip would like to give? 10, 12 or 15 ?10
How much people to split the bill?2
Each person should pay : 275.0
