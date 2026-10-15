number=int(input('Enter a number'))
if number%2==0:
    print("Number is even")
else:
    print("Number is odd")



print(" Wecome to the rollerCoaster")

height=int(input("Enter your height"))
if height>120:
    print("you can ride")
    Age=int(input("Enter your age"))
    if Age<18:
        print("please pay : "+str(12+4))
    else:
        print("please pay : "+str(12+7))
else:
    print("Sorry, you are not allowed because of your safety")   

......................................................................

print(" Wecome to the rollerCoaster")

height=int(input("Enter your height"))
if height>120:
    print("you can ride")
    Age=int(input("Enter your age"))
    if Age<=12:
        print("please pay : 5")
    elif Age<=18:
        print("please pay : 7")
    else:
        print("please pay : 12")
else:
    print("Sorry, you are not allowed because of your safety")  

Output: 
Wecome to the rollerCoaster
Enter your height123
you can ride
Enter your age13
please pay : 7
.........................................................
BMI Calculator with Interpretations
Add some if/elif/else statements to the BMI calculator so that it interprets the BMI values calculated.

If the bmi is under 18.5 (not including), print out "underweight"

If the bmi is between 18.5 (including) and 25 (not including), print out "normal weight"

If the bmi is 25 (including) or over, print out "overweight"
\
weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi<18.5:
    print("underweight")
elif bmi<25:
    print("normal weight")
else:
    print("overweight")
/

...........................................
print("Welcome to the rollerCoaster")
bill = 0

height = int(input("Enter your height: "))
if height > 120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age <= 12:
        bill = 4
    elif age <= 18:
        bill = 7
    else:
        bill = 12

    wants_photo = input("Do you want a photo? Y for Yes, N for No: ")
    if wants_photo == "Y":
        print(f"Please pay: {bill + 5}")
    else:
        print(f"Please pay: {bill}")
else:
    print("Sorry, you are not allowed because of your safety")
    
Output:
Welcome to the rollerCoaster
Enter your height: 123
You can ride
Enter your age: 23
Do you want a photo? Y for Yes, N for No: Y
Please pay: 17
.....................................
#work out how much they need to pay based on their size choice: S=15 ,M=20 ,L=25
# work out how much to add to their bill based on their pepperoni choice.S=+2,M/L=+3
#work out their final amount based on whether if they want extra cheese. +1
print("Welcome to python pizza Deliveries!")
bill=0
size=input("What size pizza do you want ? S, M OR L:")
if size=='S':
        bill+=15
elif size=='M':
        bill+=20
elif size=='L':
        bill+=25;
else
        print("You typed wrong")
pepperoni=input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
        if size=='S':
               bill+=2
        else:
               bill+=3
extra_cheese=input("Do you want extra cheese? Y or N : ")
if extra_cheese=='Y':
        bill+=1;
print(bill)

OutPut:
Welcome to python pizza Deliveries!
What size pizza do you want ? S, M OR L:L
Do you want pepperoni on your pizza? Y or N: Y
Do you want extra cheese? Y or N : N
28
.................................................................
