#Problem:You are given a list of integers.
#👉 Write a program to:
#Create a new list that contains only even numbers
#Count how many odd numbers are there in the original list

#Logic:
#Take a list of numbers
#Create an empty list to store even numbers
#Create a variable to count odd numbers and initialize it to 0
#Loop through each number in the list
#If the number is divisible by 2, add that number to the even list
#Else, increase the odd counter by 1
#After the loop ends, print the even list and the odd count

numbers=[2,4,7,3,5,8,12]

e=[]
o=0

for num in numbers:
    if num%2==0:
        e.append(num)
    else:
        o=o+1
print("even:",e)
print("odd:",o)