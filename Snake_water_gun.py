import random

# Snake Water Gun or Rock Paper Scissor

def gameWin(comp , you):

    # If two values are equal ,declare a tie!
    if comp == you :
        return None

    # Check for all possibilities when computer choose s.
    elif comp == "s":
        if you == "w":
            return False
        elif  you == "g":
            return True

    # Check for all possibilities when computer choose w.
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True

    # Check for all possibilities when computer choose g.
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("Comp turn :  Snake(s) , Water(w) and Gun(g)")
random_num = random.randint(1 , 3) 
if random_num == 1:
    comp = "s"      
elif random_num == 2:           
    comp = "w"
elif random_num == 3:
    comp = "g"
          
you = input("Your turn : Snake(s) , Water(w) and Gun(g)\n")

a = gameWin(comp , you)

print(f"Computer choose {comp}")
print(f"And You choose {you}")
if a == None:
    print("The game is tie!")
elif a :
    print("You win!")
else:
    print("You lose")