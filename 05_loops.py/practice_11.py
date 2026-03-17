#Concept: Nested Loop
#print reverse triangle

rows=int(input("enter the numbers of  row:"))
for i in range(rows,0,-1):
    for j in range(i):
        print("*", end="")
    print()