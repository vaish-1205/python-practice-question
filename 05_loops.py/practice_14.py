#Concept: Nested loops
#Write a Python program using for loops to print this pattern:
#    *
#   ***
#  *****
# *******
#*********
rows = 5
  #rows
for i in range(1, rows+1):
    
    # spaces
    for j in range(rows-i):
        print(" ", end="")
    
    # stars
    for k in range(2*i-1):
        print("*", end="")
        
    print()