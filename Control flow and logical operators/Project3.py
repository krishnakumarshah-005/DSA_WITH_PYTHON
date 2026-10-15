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
