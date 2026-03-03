#Problem:You are given a list of integers.
#👉 Write a program to:
#Create a new list containing numbers that are greater than the average of the list
#Print the new list

#Logic:
#Take the list of numbers
#Calculate the sum using a loop
#Find the average
#Create an empty list
#Loop through the list again
#If number > average, add it to the new list
#Print the new list

numbers=[3,4,1,6,78,13,53]

total=0

for num in numbers:
    total=total+num

print(total)

avg= total/len(numbers)

above_avg=[]

for num in numbers:
    if num>avg:
        above_avg.append(num)

print("Average:",avg)
print("Above_average numbers:",above_avg)