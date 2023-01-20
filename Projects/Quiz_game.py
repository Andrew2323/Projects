print("Welcome to my Computer Quiz")

playing = input("Do you want to Play my game? ")

if playing.lower() != "yes":
    quit()
print("lets play")
score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("you are correct!")
    score += 1
else:
    print("Sorry that is incorrect")

answer = input("What does GPU stand for?")
if answer.lower() == "graphics processing unit":
    print("you are correct!")
    score += 1
else:
    print("Sorry that is incorrect")

answer = input("What does RAM stand for?")
if answer.lower() == "random access memory":
    print("you are correct!")
    score += 1
else:
    print("Sorry that is incorrect")

if score == 1:
    print("you got " + str(score) + " question correct!")
else:
    print("you got " + str(score) + " questions correct!")
