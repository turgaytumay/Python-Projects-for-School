import time
import random


def game():
    point = 100
    print"Let's start with a new number "
    while True:
        print"Your Point: " + str(point)
        random_number = random.randint(1, 100)
        guess = raw_input("Guess the number:")
        if point == 0 or point < 0:
            print "<Your Point is ZERO> \n<Game Over>"
            time.sleep(0.5)
            break
        elif int(guess) == random_number:
            print "Congratulations, that's right you got +25 points"
            point = point + 25
            time.sleep(0.5)
            continue

        elif int(guess) <= random_number/2:
            print "The number you guess is too low, you loss 10 points"
            point = point - 10
            time.sleep(0.5)
            continue

        elif int(guess) < random_number and int(guess) > random_number/2:
            print "The number you guess is too low, you loss 5 points"
            point = point - 5
            time.sleep(0.5)
            continue

        elif int(guess) >= random_number*2:
            print "The number you guess is too high, you loss 10 points"
            point = point - 10
            time.sleep(0.5)
            continue

        elif int(guess) > random_number and int(guess) < random_number*2:
            print "The number you guess is too high, you loss 5 points"
            point = point - 5
            time.sleep(0.5)
            continue




print """
    ***** Welcome to "Guess the Number" Game V.0.3*****

    1- Login

    2- Sign Up (Limited to 1 user)

    3- Description
    """
id = []
while True:
    entry = raw_input("Please press 1 or 2 or 3 \n>>>")
    print " "
    print " "
    time.sleep(0.5)

    if entry == "2":
        if len(id) < 2:
            name = raw_input("Please enter your user name \n>>>")
            id.append(name)
            print " "
            print " "
            print " "
            time.sleep(0.5)

            password = raw_input("Please enter your user password \n>>>")
            id.append(password)
            print " "
            print "Going back to main menu...  "
            print " "
            time.sleep(0.5)
            continue
        else:
            print "You have already signed up, you cant sign up more than 1 user! \nGoing back to main menu... "
            print " "
            time.sleep(0.5)
            continue

    elif entry == "1":

        if len(id) == 0:
            print "Warning! There is no users :( \nPlease sign up first Going back to main menu... "
            print " "
            print " "
            time.sleep(0.5)
            continue

        elif len(id) != 0:
            login_name = raw_input("User Name:")
            login_password = raw_input("Password:")
            if login_name == id[0] and login_password == id[1]:
                game()
                continue
            else:
                print "Invilid name or password \n Going back to main menu"
                continue
        else:
            continue

    elif entry == "3":
        print """This project is "ENGR 101 - Introduction to Programming" course's mini project 01.\nThe project is a game played by one player by sign up and login system.\nThe player should assume the randomly generated number and accordingly he/she will earn or lose points.
        """
        continue

