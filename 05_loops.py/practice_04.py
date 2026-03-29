#Concept : While loop
#Write a program for palindrome number using while loop
num=int(input("enter the number:"))
original=num
reverse=0
while num>0:
    last_digit=num%10  # gives last digit of the number
    reverse=reverse*10+last_digit
    num=num//10   #floor divison:- removes last digit from the number
if original==reverse:
        print("palindrome number")
else:
        print("Not a palindrome number")