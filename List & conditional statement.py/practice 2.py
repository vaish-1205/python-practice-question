#Problem:You are given a list of integers.
#1.Find the largest number in the list
#2.Find the smallest number in the list

#Logic:
#Take a list of numbers
#Assume the first number is the largest
#Assume the first number is the smallest
#Loop through each number in the list
#If the current number is greater than largest, update largest
#If the current number is smaller than smallest, update smallest
#After the loop, print largest and smallest

numbers = [12, 4, 56, 2, 89, 10]

l=numbers[0]  #first element of list
s=numbers[0]

for num in numbers:
    if num >l:
        l=num
    elif num<s:
        s= num

print("Largest:",l)
print("Smallest:",s)