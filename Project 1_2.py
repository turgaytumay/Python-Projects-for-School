import random
import time
def hadi():
    print "Welcome to Sehir Hadi !"
    prize = 10000
    sl1 = 0
    sl2 = 0
    add = 0
    sorular = []
    q1 = "--- Q:What color are Zebras ? ---"
    cvp1 = "ans 1. Black with White stripes."
    cvp2 = "ans 2. White with Black stripes."
    cvp3 = "ans 3. Black with Red stripes."
    q2 = "--- Q:Where was the old Campus of Sehir University ? ---"
    cvp2_1 = "ans 1. Levent."
    cvp2_2 = "ans 2. Altunizade."
    cvp2_3 = "ans 3. Maltepe."
    sorular.append(q1)
    sorular.append(cvp1)
    sorular.append(cvp2)
    sorular.append(cvp3)
    sorular.append(q2)
    sorular.append(cvp2_1)
    sorular.append(cvp2_2)
    sorular.append(cvp2_3)

    people = {5.4: "Balance1", 5577: "Abbas", 3.0: "Balance2", 540: "Busra", 0.2: "Balance3", 522: "Ellie",1.2: "Balance4", 544: "Esma", 6.4: "Balance5", 5551: "omer", 7.2: "Balance6", 542: "John",0.5: "Balance7", 541: "Mumin", 3.2: "Balance8", 546: "Ebru", 2.4: "Balance9", 5466: "Betul"}
    phoneebru, phoneomer, balancemumin, balanceebru, balancebetul, phonebetul, balanceesma, phoneabbas, phonebusra, phoneellie, phoneesma, balanceabbas, balancebusra, balanceellie, phonejohn, balanceomer, phonemumin, balancejohn = people.values()
    people2 = [phoneabbas, balanceabbas, phonebusra, balancebusra, phoneellie, balanceellie, phoneesma, balanceesma,phoneomer, balanceomer, phonejohn, balancejohn, phonemumin, balancemumin, phoneebru, balanceebru,phonebetul, balancebetul]

    list_of_players = ["Abbas","Busra", "Ellie", "Esma", "Omer", "John", "Mumin", "Ebru", "Betul"]

    while True:
        c = raw_input("Please type your phone number in order to sign in:")

        if c == "**":
            while True:
                print " "
                print "1- Set prize for the next competition."
                print "2- Display questions for next competition."
                print "3- Add new question to the next competition."
                print "4- Delete a question from the next competition."
                print "5- See users data."
                print "6- Log Out."
                print " "
                adm = raw_input("Please type Number:")
                time.sleep(1)
                print " "
                print "Displaying data...."
                if adm == str(1):
                    prize1 = raw_input("enter prize :")
                    prize = int(prize1)
                    print " "
                    print "Setting prize..."
                    time.sleep(1)
                    print " "
                    print "Going back to the Admin menu..."
                    time.sleep(1)
                    continue

                elif adm == str(3):
                    q3 = raw_input("Type Question:")
                    ans3_1 = raw_input("Please type First answer and Correct answer:")
                    ans3_2 = raw_input("Please type Second answer:")
                    ans3_3 = raw_input("Please type Third answer:")
                    sorular.append(q3)
                    sorular.append(ans3_1)
                    sorular.append(ans3_2)
                    sorular.append(ans3_3)
                    add = 1
                    print "Question added"
                    time.sleep(1)
                    continue

                elif adm == str(4):
                    while True:
                        print sorular[0]
                        print sorular[1], "<-- False"
                        print sorular[2], "<-- True"
                        print sorular[3], "<-- False"
                        print " "
                        print sorular[4]
                        print sorular[5], "<-- False"
                        print sorular[6], "<-- True"
                        print sorular[7], "<-- False"
                        print " "
                        dlt = raw_input("Please type the number of the question to be deleted :")
                        if dlt == str(1):
                            sorular.pop(0)
                            sorular.pop(0)
                            sorular.pop(0)
                            sorular.pop(0)
                            sl1 = 1
                            print "Question have been deleted!"
                            time.sleep(1)
                            break
                        elif dlt == str(2):
                            sorular.pop(4)
                            sorular.pop(4)
                            sorular.pop(4)
                            sorular.pop(4)
                            sl2 = 1
                            print "Question have been deleted!"
                            time.sleep(1)
                            break
                        else:
                            continue


                    print " "
                    print "Going back to the Admin menu..."
                    time.sleep(1)

                elif adm == str(2):
                    while True:
                        if sl1 == 1:
                            print sorular[0]
                            print sorular[1], "<-- False"
                            print sorular[2], "<-- True"
                            print sorular[3], "<-- False"
                            print " "
                            while True:
                                if add == 1:
                                    print "--- Q", q3, "? ---"
                                    print "ans 1.", ans3_1, "<-- True"
                                    print "ans 2.", ans3_2, "<-- False"
                                    print "ans 3.", ans3_3, "<-- False"
                                    print " "
                                    break
                                else:
                                    break

                            break
                        elif sl2 == 1:
                            print sorular[0]
                            print sorular[1], "<-- False"
                            print sorular[2], "<-- True"
                            print sorular[3], "<-- False"
                            print " "
                            while True:
                                if add == 1:
                                    print "--- Q", q3, "? ---"
                                    print "ans 1.", ans3_1, "<-- True"
                                    print "ans 2.", ans3_2, "<-- False"
                                    print "ans 3.", ans3_3, "<-- False"
                                    print " "
                                    break
                                else:
                                    break
                            break
                        else:
                            print sorular[0]
                            print sorular[1], "<-- False"
                            print sorular[2], "<-- True"
                            print sorular[3], "<-- False"
                            print " "
                            print sorular[4]
                            print sorular[5], "<-- False"
                            print sorular[6], "<-- True"
                            print sorular[7], "<-- False"
                            print " "
                            while True:
                                if add == 1:
                                    print "--- Q", q3, "? ---"
                                    print "ans 1.", ans3_1, "<-- True"
                                    print "ans 2.", ans3_2, "<-- False"
                                    print "ans 3.", ans3_3, "<-- False"
                                    print " "
                                    break
                                else:
                                    break
                            break
                    print " "
                    print "Going back to the Admin menu..."
                    time.sleep(1)
                elif adm == str(5):
                    print " "
                    pp1 = 0
                    pp2 = 0
                    for i in range(9):
                        print list_of_players[pp1], ":", "Phone Number.", people2[pp2], "Balance.", people2[pp2 + 1]
                        pp1 = pp1 + 1
                        pp2 = pp2 + 2
                    print " "
                    print " "
                    print "Going back to the Admin menu..."
                    time.sleep(1)
                    continue

                elif adm == str(6):
                    break
                else:
                    continue

        else:
            for i in range(1):
                print "Checking", c, "..."
                print "Welcome", people[int(c)], "!"
                list_of_players.remove(people[int(c)])
                player1_name = str(people[int(c)])
            break
    print ""
    print "Competition will start soon .. be ready !"
    time.sleep(1)
    print ""

    players = len(list_of_players)

    while True:
        if sl1 == 1:
            print "--------->Total Players:", players + 1, "<---------"
            print sorular[0]
            print sorular[1]
            print sorular[2]
            print sorular[3]

            while True:
                ans1 = raw_input("Your answer:")
                time.sleep(1)
                if ans1 == str(2):
                    print "Correct answer!"
                    break
                else:
                    continue

            a_for_q1 = []
            b_for_q1 = []
            c_for_q1 = []

            for i in range(8):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a_for_q1.append(list_of_players)
                        break
                    elif ans1 == 1:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        b_for_q1.append(a)
                        break
                    else:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        c_for_q1.append(a)
                        break

            players = len(list_of_players)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Black with White stripes. False... Total answers:", len(b_for_q1)
            print "ans 2. White with Black stripes. True... Total answers:", len(a_for_q1) + 1
            print "ans 3. Black with Red stripes. False... Total answers:", len(c_for_q1)
            print " "
            break

        elif sl2 == 1:
            print "--------->Total Players:", players + 1, "<---------"
            print sorular[0]
            print sorular[1]
            print sorular[2]
            print sorular[3]

            while True:
                ans2 = raw_input("Your answer:")
                time.sleep(2)
                if ans2 == str(1):
                    print "Correct answer!"
                    break
                else:
                    continue

            a_for_q2 = []
            b_for_q2 = []
            c_for_q2 = []

            for i in range(len(list_of_players)):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a_for_q2.append(list_of_players)
                        break
                    elif ans1 == 1:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        b_for_q2.append(a)
                        break
                    else:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        c_for_q2.append(a)
                        break

            players = len(list_of_players)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Levent. False... Total answers:", len(b_for_q2)
            print "ans 2. Altunizade. True... Total answers:", len(a_for_q2) + 1
            print "ans 3. Maltepe. False... Total answers:", len(c_for_q2)
            print " "
            break
        else:
            print "--------->Total Players:", players + 1, "<---------"
            print sorular[0]
            print sorular[1]
            print sorular[2]
            print sorular[3]

            while True:
                ans1 = raw_input("Your answer:")
                time.sleep(1)
                if ans1 == str(2):
                    print "Correct answer!"
                    break
                else:
                    continue

            a_for_q1 = []
            b_for_q1 = []
            c_for_q1 = []

            for i in range(8):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a_for_q1.append(list_of_players)
                        break
                    elif ans1 == 1:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        b_for_q1.append(a)
                        break
                    else:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        c_for_q1.append(a)
                        break


            players = len(list_of_players)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Black with White stripes. False... Total answers:", len(b_for_q1)
            print "ans 2. White with Black stripes. True... Total answers:", len(a_for_q1) + 1
            print "ans 3. Black with Red stripes. False... Total answers:", len(c_for_q1)
            print " "

            print "--------->Total Players:", players + 1, "<---------"
            print sorular[4]
            print sorular[5]
            print sorular[6]
            print sorular[7]

            while True:
                ans2 = raw_input("Your answer:")
                time.sleep(1)
                if ans2 == str(2):
                    print "Correct answer!"
                    break
                else:
                    continue

            a_for_q2 = []
            b_for_q2 = []
            c_for_q2 = []

            for i in range(len(list_of_players)):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a_for_q2.append(list_of_players)
                        break
                    elif ans1 == 1:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        b_for_q2.append(a)
                        break
                    else:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        c_for_q2.append(a)
                        break

            players = len(list_of_players)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Levent. False... Total answers:", len(b_for_q2)
            print "ans 2. Altunizade. True... Total answers:", len(a_for_q2) + 1
            print "ans 3. Maltepe. False... Total answers:", len(c_for_q2)
            print " "
            break
        break


    # for q3
    while True:
        if add == 1:
            print "--------->Total Players:", players + 1, "<---------"
            print "--- Q.", q3
            print "ans 1.", ans3_1
            print "ans 2.", ans3_2
            print "ans 3.", ans3_3

            while True:
                ans3 = raw_input("Your answer:")
                time.sleep(1)
                if ans3 == str(1):
                    print "Correct answer!"
                    break
                else:
                    continue

            a_for_q3 = []
            b_for_q3 = []
            c_for_q3 = []

            for i in range(len(list_of_players)):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a_for_q3.append(list_of_players)
                        break
                    elif ans1 == 1:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        b_for_q3.append(a)
                        break
                    else:
                        a = random.choice(list_of_players)
                        list_of_players.remove(a)
                        c_for_q3.append(a)
                        break

            players = len(list_of_players)
            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print ans3_1, "True... Total answers:", len(a_for_q3) + 1
            print ans3_2, "False... Total answers:", len(b_for_q3)
            print ans3_3, "False... Total answers:", len(c_for_q3)
            print " "
            players = len(a_for_q3)
            break
        elif add != 1:
            players = len(a_for_q2)
            break


    print "---Total Winners:", int(players) + 1, "---"
    players = players + 1
    prize_share = prize / players
    w = 0
    print "Winner", ".:", player1_name, prize_share
    while True:
        if len(list_of_players) != 0:
            for i in range(len(list_of_players)):
                print "Winner", ".:", list_of_players[0], prize_share
                w = w + 1
            break
        else:
            continue
    # print "---Total distributed prize:", prize, "---"
    # print ""
    # print player1_name, "> ", prize, "Total Balance:", prize + player1_balance
    print "See you later :)"
    print "Going back to login page....."
    time.sleep(1)



hadi()
a = raw_input("Would you like to play again ? Y or N :")

while True:
    if a == "y":
        loop = 0
        while True:
            loop = loop + 1
            if loop > 0:
                hadi()
                continue
            else:
                hadi()
                continue
        break

    elif a == "n":
        exit()
        break



