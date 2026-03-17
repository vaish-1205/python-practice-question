# Concept:while loop
#Problem:Write a program that:
#1.Takes a number n
#2.Counts how many digits are in that number

n=int(input("enter the number:"))
if n==0:
    count=1
else:
    count=0
    while n>0:
     n=n//10
     count=count+1
print(count)

