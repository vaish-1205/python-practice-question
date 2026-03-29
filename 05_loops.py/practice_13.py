#Concept: while and for loop
#Write a Python program that:
#Takes a positive integer n from the user.
#For every number from 1 to n, do the following:
#Use a while loop to calculate the sum of digits of that number.
#Print only those numbers whose sum of digits is divisible by 3.
n = int(input("Enter the number: "))

for i in range(1, n+1):
    temp = i
    sum = 0

    while temp > 0:
        digit = temp % 10
        sum = sum + digit
        temp = temp // 10

    if sum % 3 == 0:
        print(i," -> digit sum=",sum)