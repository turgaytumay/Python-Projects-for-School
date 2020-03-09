import random
import time
class User:
    def __init__(self,name=["Abbas","Busra", "Ellie", "Esma", "Omer", "John", "Mumin", "Ebru", "Betul"],balance={"Abbas":5.4,"Busra":3.0,"Ellie":0.2,"Esma":1.2,"Omer":6.4,"John":7.2,"Mumin":0.5,"Ebru":3.2,"Betul":2.4},phone={"Abbas":5577, "Busra":540, "Ellie":522, "Esma":544, "Omer":5551, "John":542, "Mumin":541, "Ebru":546, "Betul":5466},is_disqualified={"Abbas": False, "Busra": False, "Ellie": False, "Esma": False, "Omer": False, "John": False, "Mumin": False,"Ebru": False, "Betul": False}):
        self.name = name
        self.balance = balance
        self.phone = phone
        self.is_disqualified = is_disqualified
    def wrt_name(self,player):
        players = {5577:"Abbas", 540:"Busra", 522: "Ellie", 544: "Esma", 5551: "Omer", 542: "John", 541: "Mumin", 546: "Ebru", 5466: "Betul"}
        self.player = player
        user_1 = players[int(player)]
        print "Checking", players[int(player)], "..."
        print "Welcome", players[int(player)], "!"
        User().name.remove(str(players[int(player)]))
        game.play()
        game.distribute_prize(user_1)

class Answer:
    def __init__(self,text=["Black with White stripes.", "White with Black stripes.", "Black with Red stripes.", "Levent.","Altunizade.", "Maltepe."],is_correct={"White with Black stripes.": True, "Altunizade.": True, "Black with White stripes.": False,"Black with Red stripes.": False, "Levent.": False, "Maltepe.": False},answer_no=["ans 1.", "ans 2.", "ans 3."]):
        self.text = text
        self.is_correct = is_correct
        self.answer_no = answer_no
    def display(self,display_correctness,display_num_answering_users):
        pass

class Question:
    def __init__(self,question_text=["--- Q:What color are Zebras ? ---", "--- Q:Where was the old Campus of Sehir University ? ---"],answers=["Black with White stripes.", "White with Black stripes.", "Black with Red stripes.", "Levent.","Altunizade.", "Maltepe."],display_correctness=[" White with Black stripes. <--> Correct Answer"," Altunizade. <--> Correct Answer"]):
        self.question_text = question_text
        self.answers = answers
        self.display_correctness = display_correctness

    def show_added_question(self,added_question,added_answers,is_correct):
        print added_question[0]
        answer = Answer()
        ans = 0
        for i in range(3):
            print answer.answer_no[ans], added_answers[ans]
            ans = ans + 1
        print is_correct[0]
    def display(self,question_no,display_answers,display_correctness):
        answer = Answer()
        print self.question_text[question_no]
        ans = 0
        for i in range(3):
            print answer.answer_no[ans],self.answers[display_answers + ans]
            ans = ans + 1
        print " "
        if display_correctness == True:
            print self.display_correctness[question_no]
            print " "
        if display_correctness == False:
            pass

    def process_answers(self,users,current_user):
        pass

class Menu:

    def display(self,display_header):
        pass

    def add_menu_item(self,text,number):
        pass

class MenuItem:
    def __init__(self):
        self.text = ["1- Set prize for the next competition.","2- Display questions for next competition.","3- Add new question to the next competition.","4- Delete a question from the next competition.","5- See users data.","6- Log Out."]
        # self.number = number
    def display(self):
        men = 0
        for i in range(6):
            print self.text[men]
            men = men + 1
        print " "
        num = raw_input("Please type a number :")
        game.build_admin_menu(int(num))

class Game:
    def __init__(self,prize = 10000):
        self.prize = prize
    def play(self):
        answer = Answer()
        user = User()
        question = Question()
        men = MenuItem()
        players = len(user.name)
        print ""
        print "Competition will start soon .. be ready !"
        if Question().question_text[0] == "--- Q:Where was the old Campus of Sehir University ? ---":
            print "--------->Total Players:", players + 1, "<---------"
            question.display(0, 0, False)
            while True:
                ans1 = raw_input("Your answer:")
                time.sleep(1)
                if ans1 == str(2):
                    print "Correct answer!"
                    break
                else:
                    continue
            a_for_q2 = []
            b_for_q2 = []
            c_for_q2 = []

            for i in range(8):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a = random.choice(user.name)
                        a_for_q2.append(a)
                        break
                    elif ans1 == 1:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        b_for_q2.append(a)
                        break
                    else:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        c_for_q2.append(a)
                        break

            players = len(user.name)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Levent. False... Total answers:", len(b_for_q2)
            print "ans 2. Altunizade. True... Total answers:", len(a_for_q2) + 1
            print "ans 3. Maltepe. False... Total answers:", len(c_for_q2)
            print " "

            if len(question.answers) > 3:
                print "--------->Total Players:", players + 1, "<---------"
                question.display(1, 3, False)
                while True:
                    ans1 = raw_input("Your answer:")
                    time.sleep(1)
                    if ans1 == str(1):
                        print "Correct answer!"
                        break
                    else:
                        continue
                a_for_q3 = []
                b_for_q3 = []
                c_for_q3 = []

                for i in range(len(a_for_q2)):
                    ans1 = random.randint(1, 3)
                    while True:
                        if ans1 == 2:
                            a = random.choice(user.name)
                            a_for_q3.append(a)
                            break
                        elif ans1 == 1:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            b_for_q3.append(a)
                            break
                        else:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            c_for_q3.append(a)
                            break

                players = len(user.name)
                print "Evaluating the responses of the other competitors ....."
                time.sleep(1)
                print " "
                print answer.text[3], "True... Total answers:", len(a_for_q3) + 1
                print answer.text[4], "False... Total answers:", len(b_for_q3)
                print answer.text[5], "False... Total answers:", len(c_for_q3)
                print " "
                players = len(a_for_q3)

        elif len(question.answers) == 9:
            print "--------->Total Players:", players + 1, "<---------"
            question.display(0, 0, False)
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
                        a = random.choice(user.name)
                        a_for_q1.append(a)
                        break
                    elif ans1 == 1:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        b_for_q1.append(a)
                        break
                    else:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        c_for_q1.append(a)
                        break

            players = len(user.name)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "Black with White stripes. False... Total answers:", len(b_for_q1)
            print "White with Black stripes. True... Total answers:", len(a_for_q1) + 1
            print "Black with Red stripes. False... Total answers:", len(c_for_q1)
            print " "

            print "--------->Total Players:", players + 1, "<---------"
            question.display(1, 3, False)
            while True:
                ans1 = raw_input("Your answer:")
                time.sleep(1)
                if ans1 == str(2):
                    print "Correct answer!"
                    break
                else:
                    continue
            a_for_q2 = []
            b_for_q2 = []
            c_for_q2 = []

            for i in range(players):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 2:
                        a = random.choice(user.name)
                        a_for_q2.append(a)
                        break
                    elif ans1 == 1:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        b_for_q2.append(a)
                        break
                    else:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        c_for_q2.append(a)
                        break

            players = len(user.name)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "ans 1. Levent. False... Total answers:", len(b_for_q2)
            print "ans 2. Altunizade. True... Total answers:", len(a_for_q2) + 1
            print "ans 3. Maltepe. False... Total answers:", len(c_for_q2)
            print " "

            print "--------->Total Players:", players + 1, "<---------"
            question.display(2, 6, False)
            while True:
                ans1 = raw_input("Your answer:")
                time.sleep(1)
                if ans1 == str(1):
                    print "Correct answer!"
                    break
                else:
                    continue
            a_for_q3 = []
            b_for_q3 = []
            c_for_q3 = []

            for i in range(players):
                ans1 = random.randint(1, 3)
                while True:
                    if ans1 == 1:
                        a = random.choice(user.name)
                        a_for_q3.append(a)
                        break
                    elif ans1 == 2:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        b_for_q3.append(a)
                        break
                    else:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        c_for_q3.append(a)
                        break

            players = len(user.name)
            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print answer.text[3], "True... Total answers:", len(a_for_q3) + 1
            print answer.text[4], "False... Total answers:", len(b_for_q3)
            print answer.text[5], "False... Total answers:", len(c_for_q3)
            print " "
            players = len(a_for_q3)
        else:
            print "--------->Total Players:", players + 1, "<---------"
            question.display(0, 0, False)
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
                        a = random.choice(user.name)
                        a_for_q1.append(a)
                        break
                    elif ans1 == 1:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        b_for_q1.append(a)
                        break
                    else:
                        a = random.choice(user.name)
                        user.name.remove(a)
                        c_for_q1.append(a)
                        break

            players = len(user.name)

            print "Evaluating the responses of the other competitors ....."
            time.sleep(1)
            print " "
            print "Black with White stripes. False... Total answers:", len(b_for_q1)
            print "White with Black stripes. True... Total answers:", len(a_for_q1) + 1
            print "Black with Red stripes. False... Total answers:", len(c_for_q1)
            print " "

            if len(question.answers) > 3 and Question().question_text[1] != "--- Q:Where was the old Campus of Sehir University ? ---":
                print "--------->Total Players:", players + 1, "<---------"
                question.display(1, 3, False)
                while True:
                    ans1 = raw_input("Your answer:")
                    time.sleep(1)
                    if ans1 == str(1):
                        print "Correct answer!"
                        break
                    else:
                        continue
                a_for_q3 = []
                b_for_q3 = []
                c_for_q3 = []

                for i in range(players):
                    ans1 = random.randint(1, 3)
                    while True:
                        if ans1 == 1:
                            a = random.choice(user.name)
                            a_for_q3.append(a)
                            break
                        elif ans1 == 2:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            b_for_q3.append(a)
                            break
                        else:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            c_for_q3.append(a)
                            break

                players = len(user.name)
                print "Evaluating the responses of the other competitors ....."
                time.sleep(1)
                print " "
                print answer.text[3], "True... Total answers:", len(a_for_q3) + 1
                print answer.text[4], "False... Total answers:", len(b_for_q3)
                print answer.text[5], "False... Total answers:", len(c_for_q3)
                print " "
                players = len(a_for_q3)

            elif len(question.answers) > 3 and Question().question_text[1] == "--- Q:Where was the old Campus of Sehir University ? ---":
                print "--------->Total Players:", players + 1, "<---------"
                question.display(1, 3, False)
                while True:
                    ans1 = raw_input("Your answer:")
                    time.sleep(1)
                    if ans1 == str(2):
                        print "Correct answer!"
                        break
                    else:
                        continue
                a_for_q2 = []
                b_for_q2 = []
                c_for_q2 = []

                for i in range(players):
                    ans1 = random.randint(1, 3)
                    while True:
                        if ans1 == 2:
                            a = random.choice(user.name)
                            a_for_q2.append(a)
                            break
                        elif ans1 == 1:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            b_for_q2.append(a)
                            break
                        else:
                            a = random.choice(user.name)
                            user.name.remove(a)
                            c_for_q2.append(a)
                            break

                players = len(user.name)

                print "Evaluating the responses of the other competitors ....."
                time.sleep(1)
                print " "
                print "ans 1. Levent. False... Total answers:", len(b_for_q2)
                print "ans 2. Altunizade. True... Total answers:", len(a_for_q2) + 1
                print "ans 3. Maltepe. False... Total answers:", len(c_for_q2)
                print " "

            else:
                pass


    def build_admin_menu(self,num):
        question = Question()
        men = MenuItem()
        self.num = num
        if self.num == 1:
            prize_new = raw_input("Enter Prize:")
            game.prize = int(prize_new)
            time.sleep(1)
            men.display()
        elif num == 2:
            question = Question()
            if Question().question_text[0] ==  "--- Q:Where was the old Campus of Sehir University ? ---" :
                question.display(0, 0, True)
                if len(question.answers) > 3:
                    question.display(1, 3, True)
            elif Answer().text[5] == "Maltepe." :
                question.display(0, 0, True)
                question.display(1, 3, True)
                if len(question.answers) > 6:
                    question.display(2, 6, True)
            else:
                question.display(0, 0, True)
                if len(question.answers) > 3:
                    question.display(1, 3, True)

            time.sleep(1)
            men.display()
        elif num == 3:
            q = raw_input("Question:")
            ans_new1 = raw_input("Correct Answer :")
            ans_new2 = raw_input("Another Answer :")
            ans_new3 = raw_input("Another Answer :")
            Question().display_correctness.append(str(ans_new1) + " <--> Correct Answer")
            Question().question_text.append(q)
            Question().answers.append(ans_new1)
            Question().answers.append(ans_new2)
            Question().answers.append(ans_new3)
            men.display()
        elif num == 4:
            question.display(0, 0, False)
            question.display(1, 3, False)
            del_q = raw_input("Please type a number for deleting :")
            if del_q == "1":
                Question().display_correctness.pop(0)
                Question().question_text.pop(0)
                Question().answers.pop(0)
                Question().answers.pop(0)
                Question().answers.pop(0)
            if del_q == "2":
                Question().display_correctness.pop(1)
                Question().question_text.pop(1)
                Question().answers.pop(3)
                Question().answers.pop(3)
                Question().answers.pop(3)
            self.delet = del_q
            time.sleep(1)
            men.display()
        elif num == 5:
            user = User()
            players = 0
            for i in range(8):
                print user.name[players] + "<--->Balance:" + str(
                    user.balance[user.name[players]]) + "<--->PhoneNum:" + str(user.phone[user.name[players]])
                players = players + 1
            time.sleep(1)
            print " "
            men.display()
        elif num == 6:
            time.sleep(1)
            game.login()

    def show_admin_menu(self):
        men = MenuItem()
        men.display()

    def distribute_prize(self,player_1):
        print "lel"
        user = User()
        self.player_1 = player_1

        players = len(user.name) + 1
        prize_share = self.prize / players
        w = 0
        print "Winner", ".:", self.player_1, prize_share
        while True:
            if len(user.name) != 0:
                for i in range(len(user.name)):
                    print "Winner", ".:", user.name[0], prize_share
                    w = w + 1
                break
            else:
                continue

    def login(self):
        log = raw_input("Please type your phone number in order to sign in:")
        if log == "**":
            game.show_admin_menu()
        else:
            user = User()
            user.wrt_name(log)

# men = Menu()
game = Game()
game.login()