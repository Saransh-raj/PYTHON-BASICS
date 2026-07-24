# random 
import random
num5 = random.randint(1,11)
tries = 0

while True:
# guess the number 
    guess = int(input("Guess the number between 1 to 10 :- "))

    if num5 == guess:
        tries += 1
        print("Yes you are right....!")
        break
        
    elif num5 < guess:
        print("Go a little lower")
        tries += 1
        
    elif num5 > guess:
            print("Go a little higher")
            tries += 1
            
    else: 
        tries += 1
        print("Sorry...! you are wrong")