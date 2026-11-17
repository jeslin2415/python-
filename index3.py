#Write a program to check whether a number is positive, negative, or zero
num=int(input("Enter a number:"))
if num>0:
    print("Number is positive")
elif num<0:
    print("Number is negative")
elif num==0:
    print("Number is Zero")

#Write a program to check whether a number is even or odd
num=int(input("Enter a number:"))
if num%2==0:
    print(num,"is even")
else:
    print(num,"is odd")    

#Write a program to check whether a person is eligible to vote based on age
age=int(input("Enter your age:"))
if age>=18:
    print("You are eligible to vote")
else:
    print("Ineligible")    
     
#Write a program to find the largest of two numbers.
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if n1>n2:
    print(n1,"is largest")
else:
    print(n2,"is largest")    

#Write a program to find the smallest of two numbers
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
if n1<n2:
    print(n1,"is smallest")
else:
    print(n2,"is smallest")   

#Write a program to find the largest of three numbers.
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1>n2 and n1>n3:
    print(n1,"is largest")
elif n2>n1 and n2>n3:
    print(n2,"is largest")    
elif n3>n1 and n3>n2:
    print(n3,"is largest") 

#Write a program to find the smallest of three numbers.
n1=int(input("Enter first number:"))
n2=int(input("Enter second number:"))
n3=int(input("Enter third number:"))
if n1<n2 and n1<n3:
    print(n1,"is smallest")
elif n2<n1 and n2<n3:
    print(n2,"is smallest")    
elif n3<n1 and n3<n2:
    print(n3,"is smallest")   

#Write a program to check whether a given year is a leap year.
year=int(input("Enter year:"))
if year%100!=0 and year%4==0:
    print(year,"is a leap year")
elif year%400==0:
    print(year,"is a leap year")    
else:
    print(year,"is not a leap year")    

#Write a program to check whether a student has passed or failed based on marks.
mark=float(input("Enter your mark:"))
if mark>=35:
    print("You are passed")
else:
    print("You are failed")    

#Write a program to calculate a student's grade based on marks.
mark=float(input("Enter your mark:"))
if mark>90:
    print("Grade A")
elif mark>80:
    print("Grade B")
elif mark>65:
    print("Grade C")  
elif mark>45:
    print("Grade D") 
else:
    print("Grade E (Failed)")

#Write a program to check whether a person is eligible for a driving licence based on age.
age=int(input("Enter your age:"))
if age>=18:
    print("Eligible for driving licence")
else:
    print("Ineligible for driving licence")

#Write a program to check whether a number is divisible by both 5 and 10.
n=int(input("Enter a number:"))
if n%5==0 and n%10==0:
    print(n,"is divisible by both 5 and 10")
else:
    print(n,"is not divisible by both 5 and 10")

#Write a program to check whether a number is divisible by 3 or 7.
n=int(input("Enter a number:"))    
if n%3==0 or n%7==0:
    print(n,"is divisible by either 3 or 7")
else:
    print(n,"is neither divisible by 3 nor by 7") 

#Write a program to check whether a given character is a vowel or consonant.
vowel=["A","E","I","O","U","a","e","i","o","u"]   
char=input("Enter a character:")
if char in vowel:
    print(char,"is a vowel")
else:
    print(char,"is a consonant")

#Write a program to check whether a number is a two-digit number
n=int(input("Enter a number:"))
if n>9 and n<100:
    print(n,"is a two digit number")
else:
    print(n,"is not a two digit number")