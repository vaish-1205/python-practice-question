#Concept : Nested Loop
#Write a program using for loops to print this pattern:


for i in range(1,6):        #for printing rows
    for j in range(i):      #for printing stars
        print("*",end="")    
    print()      #moving to next line


    # OR


rows=int(input("enter number of rows:"))
for i in range(1,rows+1):
    for j in range(i):
        print("*", end="")
    print()