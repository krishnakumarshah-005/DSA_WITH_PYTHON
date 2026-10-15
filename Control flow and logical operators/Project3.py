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
