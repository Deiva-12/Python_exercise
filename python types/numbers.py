"""Python's 2 main types for Numbers is int and float (or integers and floating point  numbers). """

print(type(1)) # int  
print(type(-10)) # int 
print(type(0)) # int 
print(type(0.0)) # float 
print(type(2.2)) # float 
print(type(4E2)) # float - 4*10 to the power of 2

#Arithmetic

a ,b = 10,3
print(a+b,a-b)
print(a * b)
print(a ** 3)
print(a/b)
print(a//b) # --> floor division - no decimals and returns an int 10 % 3 # 1 --> modulo operator - return the reminder. Good for deciding if  number is even or odd 


#Basic Functions 

print(pow(5,2)) # like doing 5 ** 2
print(abs(-10))
print(round(5.78))
print(round(5.678,2))
print(bin(512)) # binary fprmate
print(hex(500)) # hexdecimal format

#converting strings to Numbers

age = input("How old are yoy ?")
age = int(age)
print(type(age))
pi = input("what is the value of pi?")
pi = float(pi)
print(type(pi))















