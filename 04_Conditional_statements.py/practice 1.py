#Problem:You are given a list of integers.
#1.Count how many numbers are positive, negative, and zero
#2.Print the counts separately



#Logic:
#Create list of numbers
#Create three counters: positive, negative, zero
#Loop through the list one number at a time
#If number > 0 → increase positive count
#Else if number < 0 → increase negative count
#Else → increase zero count
#Print all three counts

numbers = [2, -3, 0, 5, -1, 0, 4]

p=0
n=0
z=0

for num in numbers:
    if num >0:
        p=p+1
    elif num<0:
        n =n+1
    else:
        z=z+1
print("positive:",p)
print("negative:",n)
print("zero:",z)



