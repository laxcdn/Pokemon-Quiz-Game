from tkinter.messagebox import YES


print("Welcome to my Quiz!")

playing = input("Do you want to play? ")

if playing != "yes":
    quit()

print("Okay, let's start! ")
score = 0

answer = input("How many Gym Badges must a trainer collect before challenging the Elite Four? ")
if answer == "8":
    print("Thats correct!")
    score += 1
else:
    print("Looks like someone hasn't beaten pokemon yet! ")

answer = input("What type is  super effective against ghost? ")
if answer.lower() == "dark":
    print("Thats correct!")
    score += 1
else:
    print("Sorry, thats not the right answer. ")

answer = input("Which pokemon is a pure steel type? ")
if answer.lower() == "registeel":
    print("Thats correct!")
    score += 1
else:
    print("Looks like you need to go out and collect more pokemon. ")

answer = input("What pokemon does Misty walk around with? ")
if answer.lower() == "togepi":
    print("Thats correct!")
    score += 1
else:
    print("Nope, sorry! ")

print("you got " + str(score) + " questions correct!")