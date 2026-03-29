#Concept: for Loop
#Write a program using a for loop to calculate the sum of numbers from 1 to n.

n=int(input("enter the number:"))
total=0
for i in range(1,n+1):
    print(i)
    sum=sum+i
print("total sum:",total)
