#while  loop 
#problem:Write a Python program using a while loop that:
#Takes a number as input from the user
#Calculates the sum of its digits
#Prints the final sum
#print total digit

num=int(input("enter the number:"))
digit_sum=0
count=0
while num > 0:
    last_digit=num%10
    digit_sum=digit_sum+last_digit
    count=count+1
    num=num//10
print("sum of the digits:",digit_sum)
print("Total digits:",count)