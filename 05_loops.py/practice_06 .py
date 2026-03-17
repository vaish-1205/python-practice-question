# Concept: while loop:
#problem:Write a Python program using a while loop to check whether a number is an Armstrong number.


#what is armstrong number:A number is Armstrong if:
#sum of each digit raised to the power of total digits = original number

num=int(input("enter the number:"))
original=num
digits = 0
temp =num

#count digits
while temp >0:
    digits+=1
    temp =temp // 10

#calculate
temp = num
arm_sum =0

while temp> 0 :
    digit = temp%10
    arm_sum+=digit **digits
    temp = temp //10

if arm_sum==original:
    print("Armstrong number")
else:
    print("not Armstrong")