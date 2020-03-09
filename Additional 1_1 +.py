from swampy.TurtleWorld import *
import random
world = TurtleWorld()

def finish():
    while True:
        son = raw_input("Do you want to play again this game ?")
        if son == "yes":
            world.clear()
            game()
        elif son == "no":
            exit()

def game():
    print "****** Welcome to Sehir Minesweeper ******"
    print " "
    print "<-----First Turtle----->"

    # First turtle
    while True:
        n1 = raw_input("Please type the name of the first Turtle:")
        n1_1 = str(n1)
        if n1 == " ":
            print "ERROR: Name cannot ve empty!"
            continue

        else:
            n1 = Turtle()
            while True:
                c1 = raw_input("Please choose turtle color for " + n1_1 + "(red, blue, green):")
                c1_1 = str(c1)
                if c1 == "green" or c1 == "blue" or c1 == "red":
                    n1.set_color(c1)
                    Turtle.set_delay(n1, 0)
                    pu(n1)
                    bk(n1, 180)
                    bk(n1, 10)
                    pd(n1)
                    lt(n1, 90)
                    fd(n1, 23)
                    for i in range(2):
                        rt(n1, 90)
                        fd(n1, 622)
                        rt(n1, 90)
                        fd(n1, 106)
                    bk(n1, 23)
                    rt(n1, 90)
                    pu(n1)
                    fd(n1, 10)
                    pd(n1)

                    for i in range(30):
                        for i in range(4):
                            lt(n1, 90)
                            fd(n1, 4)
                        pu(n1)
                        fd(n1, 20)
                        pd(n1)

                    pu(n1)
                    bk(n1, 600)
                    pd(n1)
                    print n1_1 + " is ready to go!"
                    break

                elif c1_1 != "green" or c1_1 != "blue" or c1_1 != "red":
                    print "ERROR: black is not a valid color, please select one of red , blue or green colors:"
                    continue
            break

    # Second turtle
    while True:
        n2 = raw_input("Please type the name of the second Turtle:")
        n2_1 = str(n2)
        if n2 == " ":
            print "ERROR: Name cannot ve empty!"
            print " "
            continue

        elif n1_1 == n2_1:
            print "ERROR! " + n1_1 + " is already taken, please enter another name!"
            print " "
            continue

        else:
            n2 = Turtle()
            while True:
                c2 = raw_input("Please choose turtle color for " + n2_1 + "(red, blue, green):")
                c2_1 = str(c2)
                if c1_1 == c2_1:
                    print "ERROR! " + c1_1 + " color is already taken, select another color!"
                    continue

                elif c2_1 == "green" or c2_1 == "blue" or c2_1 == "red":
                    n2.set_color(c2)
                    Turtle.set_delay(n2, 0)
                    pu(n2)
                    bk(n2, 180)
                    rt(n2, 90)
                    fd(n2, 63)
                    lt(n2, 90)
                    pd(n2)

                    for i in range(30):
                        for i in range(4):
                            lt(n2, 90)
                            fd(n2, 4)
                        pu(n2)
                        fd(n2, 20)
                        pd(n2)

                    pu(n2)
                    bk(n2, 600)
                    pd(n2)
                    print n2_1 + " is ready to go!"
                    break

                elif c2_1 != "green" or c2_1 != "blue" or c2_1 != "red":
                    print "ERROR! black is not a valid color, please select one of red , blue or green colors:"
                    continue
            break
    print "Deploying bombs randomly"

    l = list(range(2, 29))
    bomb = 1
    r = []
    s = 0
    for i in range(5):
        random1 = random.choice(l)
        l.remove(random1)
        r.append(random1)

        b = "b" + str(bomb)
        c = "c" + str(bomb)

        b = Turtle()
        c = Turtle()

        Turtle.set_delay(b, 0)
        Turtle.set_delay(c, 0)

        b.set_color("black")
        c.set_color("black")

        pu(b)
        bk(b, 180)
        f = int(random1) * 20
        fd(b, f)

        pu(c)
        bk(c, 180)
        rt(c, 90)
        fd(c, 63)
        lt(c, 90)
        f = int(random1) * 20
        fd(c, f)

        bomb = bomb + 1

    print "Lets start the game with coin toss"
    while True:
        toss = random.randint(0, 2)
        if toss == 0:
            print n1_1 + " won the toss, " + n1_1 + " starts first."
            toss_won = n1_1
            toss_lose = n2_1
            turtle_won = n1
            turtle_lose = n2
            break
        elif toss == 1:
            print n2_1 + " won the toss, " + n2_1 + " starts first."
            toss_won = n2_1
            toss_lose = n1_1
            turtle_won = n2
            turtle_lose = n1
            break


    dice_won = 0
    dice_lose = 0


    # dice_won_1 - dice_won_c1 < 31 and dice_won_2 - dice_won_c2 < 31

    while True:
        while int(dice_won) < 30 and int(dice_won) != r[0] and int(dice_won) != r[1] and int(dice_won) != r[2] and int(
                dice_won) != r[3] and int(dice_won) != r[4]:
            raw_for_dice = raw_input("Please press ENTER to roll the dice " + toss_won)
            dice_roll = random.randint(1, 6)
            print "Dice Result: " + str(dice_roll)

            if int(dice_won) + dice_roll > 30:
                rest_won = 30 - dice_won
                fd_dice = rest_won * 20
                fd(turtle_won, fd_dice)
                dice_won = dice_won + rest_won
                print toss_won + " has won"
                finish()
                print dice_won
                break

            elif dice_roll == 6 and dice_won + dice_roll < 30:
                fd_dice = dice_roll * 20
                fd(turtle_won, fd_dice)
                dice_won = dice_won + dice_roll
                continue
            elif dice_roll != 6 and dice_won + dice_roll < 30:
                fd_dice = dice_roll * 20
                fd(turtle_won, fd_dice)
                dice_won = dice_won + dice_roll
                break


        while int(dice_lose) < 30 and int(dice_lose) != r[0] and int(dice_lose) != r[1] and int(dice_lose) != r[
            2] and int(dice_lose) != r[3] and int(dice_lose) != r[4]:
            raw_for_dice = raw_input("Please press ENTER to roll the dice " + toss_lose)
            dice_roll = random.randint(1, 6)
            print "Dice Result: " + str(dice_roll)

            if dice_lose + dice_roll > 30:
                rest_lose = 30 - dice_lose
                fd_dice = rest_lose * 20
                fd(turtle_lose, fd_dice)
                dice_lose = dice_lose + rest_lose
                print toss_lose + " has won"
                finish()
                print dice_lose
                break

            elif dice_roll == 6 and dice_lose + dice_roll < 30:
                fd_dice = dice_roll * 20
                fd(turtle_lose, fd_dice)
                dice_lose = dice_lose + dice_roll
                continue
            elif dice_roll != 6 and dice_lose + dice_roll < 30:
                fd_dice = dice_roll * 20
                fd(turtle_lose, fd_dice)
                dice_lose = dice_lose + dice_roll
                break

        if int(dice_won) == r[0] or int(dice_won) == r[1] or int(dice_won) == r[2] or int(dice_won) == r[3] or int(dice_won) == r[4]:
            print toss_won + " is eliminated"
            while True:
                while int(dice_lose) < 30 and int(dice_lose) != r[0] and int(dice_lose) != r[1] and int(dice_lose) != r[
                    2] and int(dice_lose) != r[3] and int(dice_lose) != r[4]:
                    raw_for_dice = raw_input("Please press ENTER to roll the dice " + toss_lose)
                    dice_roll = random.randint(1, 6)
                    print "Dice Result: " + str(dice_roll)

                    if dice_lose + dice_roll > 30:
                        rest_lose = 30 - dice_lose
                        fd_dice = rest_lose * 20
                        fd(turtle_lose, fd_dice)
                        dice_lose = dice_lose + rest_lose
                        print toss_lose + " has won"
                        finish()
                        print dice_lose
                        break

                    elif dice_roll == 6 and dice_lose + dice_roll < 30:
                        fd_dice = dice_roll * 20
                        fd(turtle_lose, fd_dice)
                        dice_lose = dice_lose + dice_roll
                        continue
                    elif dice_roll != 6 and dice_lose + dice_roll < 30:
                        fd_dice = dice_roll * 20
                        fd(turtle_lose, fd_dice)
                        dice_lose = dice_lose + dice_roll
                        break
                if int(dice_lose) == r[0] or int(dice_lose) == r[1] or int(dice_lose) == r[2] or int(dice_lose) == r[3] or int(dice_lose) == r[4]:
                    print "also eliminated"
                    break
            # print toss_lose + " has won"
        elif int(dice_lose) == r[0] or int(dice_lose) == r[1] or int(dice_lose) == r[2] or int(dice_lose) == r[3] or int(dice_lose) == r[4]:
            print toss_lose + " is eliminated"
            while True:
                while int(dice_won) < 30 and int(dice_won) != r[0] and int(dice_won) != r[1] and int(dice_won) != r[
                    2] and int(
                    dice_won) != r[3] and int(dice_won) != r[4]:
                    raw_for_dice = raw_input("Please press ENTER to roll the dice " + toss_won)
                    dice_roll = random.randint(1, 6)
                    print "Dice Result: " + str(dice_roll)

                    if int(dice_won) + dice_roll > 30:
                        rest_won = 30 - dice_won
                        fd_dice = rest_won * 20
                        fd(turtle_won, fd_dice)
                        dice_won = dice_won + rest_won
                        print toss_won + " has won"
                        finish()
                        print dice_won
                        break

                    elif dice_roll == 6 and dice_won + dice_roll < 30:
                        fd_dice = dice_roll * 20
                        fd(turtle_won, fd_dice)
                        dice_won = dice_won + dice_roll
                        continue
                    elif dice_roll != 6 and dice_won + dice_roll < 30:
                        fd_dice = dice_roll * 20
                        fd(turtle_won, fd_dice)
                        dice_won = dice_won + dice_roll
                        break
                if int(dice_won) == r[0] or int(dice_won) == r[1] or int(dice_won) == r[2] or int(dice_won) == r[3] or int(dice_won) == r[4]:
                    print "also eliminated"
                    break
            # print toss_won + " has won"

game()

finish()
def finish():
    while True:
        son = raw_input("Do you want to play again this game ?")
        if son == "yes":
            world.clear()
            game()
        elif son == "no":
            exit()

wait_for_user()