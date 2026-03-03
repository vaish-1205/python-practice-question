#Number Guessing Game (Limited Attempts) (while loop)
#problem 1:WRite a program that :
#Stores a secret number (for example: 27)
#Gives the user 5 attempts to guess the number.
#After each guess:
#If guess is too high → print "Too high"
#If guess is too low → print "Too low"
#If correct → print "Correct! You won." and stop the loop
#It also prints how many attempts were used when user wins.
#If the user fails after 5 attempts → print "Game Over"

secret = 27
count =0
while count<5:
    guess=int(input("enter the guess:"))
    count=count+1
    if guess>secret:
        print("too high")
    elif guess<secret:
        print("too low ")
    else:
        print(f"correct! you won in {count} attempts.")
        break
   
if count==5:
    print("Game over")