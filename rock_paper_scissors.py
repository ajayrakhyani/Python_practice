import random

def game (comp, you):
    if comp == you:
        return None
    elif comp == 'r':
        if you == 'p':
            return True
        elif you == 's':
            return False
    
    elif comp == 'p':
        if you == 's':
            return True
        elif you == 'r':
            return False

    elif comp == 's':
        if you == 'r':
            return True
        elif you == 'p':
            return False


randomNo = random.randint(1, 3)

if randomNo == 1:
    comp = 'r'
elif randomNo == 2:
    comp = 'p'
elif randomNo == 3:
    comp = 's'


you = input ("Your turn: Select Rock(r), paper(p), scissor(s)\n")
print (f"You selected {you}")

print ("Computer's Turn")
print (f"Computer selected {comp}")

results = game(comp, you)

if results == None:
    print ("There is a tie")
elif results:
    print ("You Win!!!!")
else:
    print ("You lose :(")

