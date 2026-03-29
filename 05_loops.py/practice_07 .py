#concept:Loops
#write a program to check if the number is prime using loop

n = int (input ("enter the number:"))

for i in range(2 ,n+1):
    j =2
    is_prime = True

    while i >j :
        if i % j==0:
            is_prime=False
            break
        j+=1

    if is_prime:
        print(i,"is prime")

