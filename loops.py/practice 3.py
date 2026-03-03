#Que.Reverse a Number (Without Using String)
#Write a program that :Write a Python program using a while loop that:
#Takes an integer input from user
# #Reverses the number
#Prints the reversed number

num = int(input("Enter number: "))
reverse = 0

while num > 0:
    last_digit = num % 10
    reverse = reverse * 10 + last_digit
    num = num // 10

print("Reversed number:", reverse)