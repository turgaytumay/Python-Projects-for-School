from swampy.TurtleWorld import *
import random
world = TurtleWorld()


def game():
    # First turtle
    print "      Hello There ! "
    print "<-----First Turtle----->"

    n1 = raw_input("What is the name of first Turtle ?")
    n1 = Turtle()
    pu(n1)
    bk(n1, 150)
    pd(n1)
    print "Good Name"

    while True:
        c1 = raw_input("Please select a color for your turtle red-blue-yellow ?")
        if c1 == "yellow" or c1 == "blue" or c1 == "red":
            n1.set_color(c1)
            break

        elif c1 != "yellow" or c1 != "blue" or c1 != "red":
            print "this color is not a valid color !"
            continue

    # Second Turtle
    print "<-----Second Turtle----->"
    while True:
        n2 = raw_input("What is the name of the second Turtle ?")
        if str(n1) == str(n2):
            print "This name have been taken . please take another name !"
            continue


        else:
            n2 = Turtle()
            pu(n2)
            lt(n2, 60)
            bk(n2, 30)
            rt(n2, 60)
            bk(n2, 135)
            pd(n2)
            break
    while True:
        c2 = raw_input("Please select a color for your second turtle red-blue-yellow ?")
        if c2 == "yellow" or c2 == "blue" or c2 == "red":
            n2.set_color(c2)
            break

        elif c2 != "yellow" or c2 != "blue" or c2 != "red":
            print "this color is not a valid color !"
            continue
    # h
# create loop for race.
    Turtle.set_delay(n1, 0.0009)
    Turtle.set_delay(n2, 0.0009)

    score = 0
    score1 = 0
    round = 0
    while score < 200 or score1 < 200:
        print "Turtles are ready to go !"

        print "Round:", round
        print "First Turtle's score :", score
        print "Second Turtle's score :", score1

        #   cember
        def cem():
            lt(n1, 90)
            for i in range(180):
                fd(n1, 0.3)
                rt(n1, 1)
            lt(n1, 90)

        # merdiven
        def mer():
            lt(n1, 90)
            fd(n1, int(wave1))
            rt(n1, 90)
            fd(n1, int(wave1))
            lt(n1, 90)
            fd(n1, int(wave1))
            rt(n1, 90)
            fd(n1, int(wave1))
            rt(n1, 90)
            fd(n1, int(wave1))
            lt(n1, 90)
            fd(n1, int(wave1))
            rt(n1, 90)
            fd(n1, int(wave1))
            lt(n1, 90)

        def duz():
            fd(n1, int(wave1))

        wave1 = raw_input("How many steps would you like to take for First Turtle ?")
        a = 100 - int(wave1)
        b = random.randint(0, 100)

        while True:
            if b < a:
                while True:
                    random1 = random.randint(0, 3)
                    if random1 == 0:
                        cem()
                        score = score + int(wave1)
                        break
                    elif random1 == 1:
                        mer()
                        score = score + int(wave1)
                        break
                    elif random1 == 2:
                        duz()
                        score = score + int(wave1)
                        break
                    elif random1 == 3:
                        print "First Turtle Failed ! "
                        break
            break

        def cem2():
            rt(n2, 90)
            for i in range(180):
                fd(n2, 0.3)
                lt(n2, 1)
            rt(n2, 90)

        def mer2():
            rt(n2, 90)
            fd(n2, int(wave2))
            lt(n2, 90)
            fd(n2, int(wave2))
            rt(n2, 90)
            fd(n2, int(wave2))
            lt(n2, 90)
            fd(n2, int(wave2))
            lt(n2, 90)
            fd(n2, int(wave2))
            rt(n2, 90)
            fd(n2, int(wave2))
            lt(n2, 90)
            fd(n2, int(wave2))
            rt(n2, 90)

        def duz2():
            fd(n2, int(wave2))

        wave2 = raw_input("How many steps would you like to take for Second Turtle ?")
        c = 100 - int(wave2)
        d = random.randint(0, 100)

        while True:
            if d < c:
                while True:
                    random2 = random.randint(0, 3)
                    if random2 == 0:
                        cem2()
                        score1 = score1 + int(wave2)
                        break
                    elif random2 == 1:
                        mer2()
                        score1 = score1 + int(wave2)
                        break
                    elif random2 == 2:
                        duz2()
                        score1 = score1 + int(wave2)
                        break
                    elif random2 == 3:
                        print "Second Turtle Failed ! "
                        break

            break

        round = round + 1



    while True:
        if score >= 200:
            print "First Turtle Win"
            pu(n1)
            pu(n2)
            bk(n1, int(score))
            bk(n2, int(score1))
            pd(n1)
            pd(n2)
            break

        elif score1 >= 200:
            print "Second Turtle Win"
            pu(n1)
            pu(n2)
            bk(n1, int(score))
            bk(n2, int(score1))
            pd(n1)
            pd(n2)
            break


game()
# finishing game or starting again.
def finish():
    while True:
        son = raw_input("Do you want to play again this game ?")
        if son == "yes":
            world.clear()
            game()
        elif son == "no":
            exit()
finish()
wait_for_user()
