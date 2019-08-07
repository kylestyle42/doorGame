import random

def dividenum(x,y):
    return x/y

# print (dividenum(10,2))

def start():
    play_again = "yes"

    while play_again.lower() == "yes":
        intro()
        print("You escaped! ")
        play_again = input("Do you want to play again? ")

def choose_door(answer):
    choice = input("Enter #1, #2, #3, or #4: ")
    if choice != "1" and choice != "2" and choice != "3" and choice != "4":
        print("Not valid answer")
        return False
    elif int(choice) == answer:
        return True
    else:
        return False

def choose_door2(answer1, answer2, false_door):
    choice = input("Enter a number between #1 and #6: ")

    if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
        print("Not valid answer")
        return False
    elif int(choice) == answer1 or int(choice) == answer2:
        return True
    elif int(choice) == false_door:
        print("You chose the trap door! Back to level one.")
        intro()
        return True
    else:
        return False

def intro():
    print ("You enter a dark room with 4 doors. Choose which door to enter.")
    correct_door = random.randint(1, 4)
    while not choose_door(correct_door):
        print("Try Again: ")
    print("Correct!")
    level_two()

def level_two():
    print("You enter a dark room with 6 doors. 2 will allow you to escape, "
          "and 1 will send you back. Choose which door to enter.")
    correct_door = random.randint(1, 6)
    correct_door2 = random.randint(1, 6)
    false_door = random.randint(1, 6)

    while correct_door == correct_door2:
        correct_door2 = random.randint(1, 6)

    while false_door == correct_door or false_door == correct_door2:
        false_door = random.randint(1, 6)

    print(correct_door)
    print(correct_door2)
    print(false_door)

    while not choose_door2(correct_door, correct_door2, false_door):
        print("Try Again: ")


start()





