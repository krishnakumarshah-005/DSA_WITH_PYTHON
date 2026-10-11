'''
Data Types:
String
Integer
Float
Boolean
'''
print('Hello'[4])   #   Output : o
print('Hello'[-1]) #   Output : o
print("Hello"[-2]) # Output : l
print("KRISHNA"[len("KRISHNA")-1])   #   Output : A
print(123)   # Integer
print(123_456_789)  # Large_Integer
print(123.43)   # Floating point Number

num1 = 123456789
num2 = 123_456_789   # easier to read

print(num1 == num2)  # True

# Type error , Type checking and Type Conversion
print(type(123))
print(type('Hello'))
print(type(123.01))
print(type(True))


'''
OUTPUT:
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
'''

#Conversion type(Casting)
print(int('123')+int('456'))
print("Golmal hai bhai sab gol maal hai "+str(len(input("Enter your name "))))

''''
579
Enter your name krishna
Golmal hai bhai sab gol maal hai 7
'''
...............................................................
Mathematical Operation in Python (BODMAS(Left to right)-----> (),{},[], /,*,+,-)
---------------------------------------------------------------
print(2+9)
print(9-2)
print(2*2)
print(9/3)
print(9//3)
print(9*2)
print(9**2)


OUTPUT:
11
7
4
3.0
3
18
81

