login = {"ahmet":[123, 500, {}], "ayse":[456, 500, {}]}
courses = {"physics":4, "mathematics":3, "programming":3}

# id_keys_1 = login_1.keys()
# password_values_1 = login_1.values()

while True:
    print "*****Welcome to Course Management System*****\nPlease provide login information"
    id_login = raw_input("ID:")
    password_login = raw_input("Password:")

    id_keys = login.keys()
    password_values = login.values()

    for_login_id = id_login in id_keys
    for_login_password = str(password_login) in str(password_values[0])

    if id_login == "admin" and password_login == "sehir123":
        print "Welcome Admin!"
        while True:
            print "\nWhat do you want to do ?\n "
            print "1-List courses\n2-Create a course\n3-Delete a course\n4-Show students registered a course\n5-Users Budget Menu\n6-List Users\n7-Create User\n8-Delete User\n9-Exit\n"
            adminmenu_item = raw_input("Your choice:")
            if adminmenu_item == "1":
                courses_keys = courses.keys()
                courses_values = courses.values()
                print "*** Offered Courses ***\n \nCourse name---Credit"
                n = 0
                for i in range(len(courses)):
                    print str(n+1) +"-"+ str(courses_keys[n]) +"---"+ str(courses_values[n])
                    n = n + 1
                continue
            elif adminmenu_item == "2":
                while True:
                    add_course = raw_input("What is the name of the course that you want to add ?:")
                    add_course_credit = raw_input("\nHow many credits this course has ?:")
                    print "\n" + add_course + " will added with 4 credits."
                    add_course_sure = raw_input("Are you sure ?[Y/N]:")
                    if add_course_sure == "y" or add_course_sure == "Y":
                        courses[add_course]=int(add_course_credit)
                        print add_course + " has been added to courses with "+ add_course_credit +" credits.\n"
                        break
                    elif add_course_sure == "n" or add_course_sure == "N":
                        print "this course wouldn't be added\n"
                        break
                    else:
                        print "please type yes for Y or no for N\n"
                        continue
                continue
            elif adminmenu_item == "3":
                while True:
                    courses_keys = courses.keys()
                    courses_values = courses.values()
                    print "\nCourse name---Credit"
                    n = 0
                    for i in range(len(courses)):
                        print str(n + 1) + "-" + str(courses_keys[n]) + "---" + str(courses_values[n])
                        n = n + 1
                    delet_course = raw_input("Which course do you want to delete ?:")
                    if int(delet_course) <= len(courses) and int(delet_course) > 0:
                        b = int(delet_course) - 1
                        a = str(courses_keys[b])
                        courses.pop(a)
                        print str(courses_keys[b]) + " has been deleted and money has been transferred back to student accounts."
                        break
                    else:
                        print "\nplease type valid number!\n"
                        continue

                continue
            elif adminmenu_item == "4":
                while True:
                    courses_keys = courses.keys()
                    courses_values = courses.values()
                    show_course = raw_input("Which course do you want to show ?:")
                    show_course_trueorfalse = show_course in courses.keys()
                    if show_course_trueorfalse == False:
                        print "This course doesn't exist, please provide a valid input."
                        continue
                    elif show_course_trueorfalse == True:
                        pass
                continue
            elif adminmenu_item == "5":
                print "User---Money"
                user_list = login.keys()
                n = 0
                for i in range(len(user_list)):
                    print str(n + 1) + "-" + str(user_list[n]) + "---" + str(login.get(user_list[n])[1])
                    n = n + 1
                while True:
                    print "\n1-Add money to user\n2-Subtract money from user\n3-Back to admin menu"
                    admin_menu_budget = raw_input("\nWhat do you want to do ?:")
                    if admin_menu_budget == "1":
                        while True:
                            user_list = login.keys()
                            n = 0
                            for i in range(len(user_list)):
                                print str(n + 1) + "-" + str(user_list[n])
                                n = n + 1
                            selected_person = raw_input("Which user do you want add money to their account")
                            a = int(selected_person) - 1
                            selected_person_1 = str(user_list[a])
                            selected_person_1_budget = int(login.get(user_list[a])[1])

                            amount_of_money = raw_input("How much money do you want to add ?")
                            print amount_of_money + " will be added to " + selected_person_1
                            amount_of_money_sure = raw_input("Are you sure ?[y/n]")
                            if amount_of_money_sure == "y":
                                login.get(user_list[a])[1] = login.get(user_list[a])[1] + int(amount_of_money)
                                break
                            elif amount_of_money_sure == "n":
                                continue
                            else:
                                continue
                        continue
                    elif admin_menu_budget == "2":
                        while True:
                            user_list = login.keys()
                            n = 0
                            for i in range(len(user_list)):
                                print str(n + 1) + "-" + str(user_list[n])
                                n = n + 1
                            selected_person = raw_input("Which user do you want subtract money to their account")
                            a = int(selected_person) - 1
                            selected_person_1 = str(user_list[a])
                            selected_person_1_budget = int(login.get(user_list[a])[1])

                            amount_of_money = raw_input("How much money do you want to subtract ?")
                            print amount_of_money + " will be subtract to " + selected_person_1
                            amount_of_money_sure = raw_input("Are you sure ?[y/n]")
                            if amount_of_money_sure == "y":
                                login.get(user_list[a])[1] = login.get(user_list[a])[1] - int(amount_of_money)
                                break
                            elif amount_of_money_sure == "n":
                                continue
                            else:
                                continue
                        continue
                    elif admin_menu_budget == "3":
                        print "Going back to admin menu."
                        break
                    else:
                        print "Please type valid number!"
                        continue
                continue
            elif adminmenu_item == "6":
                id_keys = login.keys()
                print "Current User:"
                n = 0
                for i in range(len(id_keys)):
                    print str(n+1) + "-" + id_keys[n]
                    n = n + 1
                continue
            elif adminmenu_item == "7":
                new_user_name = raw_input("What is the name of user that you want to create ?")
                new_user_password = raw_input("What is the password for account ?")
                new_user_budget = raw_input("How much money do you want user to have ?")
                print "The new user has been added successfully!"
                login[new_user_name] = [int(new_user_password), int(new_user_budget), {}]
                continue
            elif adminmenu_item == "8":
                id_keys = login.keys()
                print "Current User:"
                n = 0
                for i in range(len(id_keys)):
                    print str(n + 1) + "-" + id_keys[n]
                    n = n + 1
                delete_user = raw_input("Which user do you want to delete:")
                a = int(delete_user) - 1
                delete_user_1 = str(id_keys[a])
                login.pop(delete_user_1)
                print delete_user_1 + "is deleted!"
                continue
            elif adminmenu_item == "9":
                print "Exiting admin menu."
                break
            else:
                print "Please type valid number!"
                continue
        continue

    elif for_login_id == False or for_login_password == False:
        print "Invalid id or password please try again\n "
        continue

    elif for_login_id == True and for_login_password == True:
        print "Welcome " + id_login + "! Successfully logged in!\n "
        while True:
            print "What do you want to do ?\n "
            print "1-Add course to my courses\n2-Delete a course from my courses\n3-Show my courses\n4-Budget Menu\n5-Exit"
            user_menu = raw_input("Your choice:")
            if user_menu == "1":
                while True:
                    courses_keys = courses.keys()
                    courses_values = courses.values()
                    print "*** Offered Courses ***\n \nCourse name---Credit"
                    n = 0
                    for i in range(len(courses)):
                        print str(n + 1) + "-" + str(courses_keys[n]) + "---" + str(courses_values[n])
                        n = n + 1

                    courses_keys = courses.keys()
                    courses_values = courses.values()

                    add_course_student = raw_input("Which course do you want to take(Enter 0 to go to main menu)?:")

                    a = int(add_course_student) - 1
                    selected_course = str(courses_keys[a])
                    selected_course_value = int(courses_values[a])
                    logined_user = login.get(id_login)[2].keys()


                    for_addcourse_student = str(selected_course) in str(logined_user)

                    logined_user_budget = login.get(id_login)[1]

                    if int(add_course_student) <= len(courses) and int(add_course_student) > 0 and for_addcourse_student == False and logined_user_budget < selected_course_value*100:
                        print "You don't have enough money in your account. Please deposit money, or choose a course with lesser credit"
                        continue
                    elif int(add_course_student) <= len(courses) and int(add_course_student) > 0 and for_addcourse_student == True:
                        print "This course is already in your profile. Please choose another course."
                        continue
                    elif add_course_student == "0":
                        print "Returning to student menu!"
                        break
                    elif int(add_course_student) <= len(courses) and int(add_course_student) > 0 and for_addcourse_student == False and logined_user_budget >= selected_course_value*100:
                        login.get(id_login)[1] = logined_user_budget - selected_course_value*100
                        login.get(id_login)[2][selected_course] = int(selected_course_value)
                        print login.get(id_login)[2]
                        print selected_course + " has been successfully added to your courses."
                        break
                    else:
                        print "Please type valid number!"
                        continue
                continue
            elif user_menu == "2":
                while True:
                    logined_user = login.get(id_login)[2].keys()
                    logined_user_value = login.get(id_login)[2].values()
                    courses_keys = courses.keys()
                    courses_values = courses.values()
                    print "*** Offered Courses ***\n \nCourse name---Credit"
                    n = 0
                    for i in range(len(logined_user)):
                        print str(n + 1) + "-" + str(logined_user[n]) + "---" + str(logined_user_value[n])
                        n = n + 1

                    courses_keys = courses.keys()
                    courses_values = courses.values()

                    delete_course_student = raw_input("Which course do you want to remove?:")
                    a = int(delete_course_student) - 1
                    selected_course = str(logined_user[a])
                    selected_course_value = int(logined_user_value[a])

                    print "You have chosen: " + str(selected_course)
                    print str(selected_course_value*100) + "$ will be returned to your account."

                    delete_course_student_sure = raw_input("Are you sure that you want to remove this course ?[y/n]")

                    logined_user = login.get(id_login)[2].keys()

                    for_deletecourse_student = str(selected_course) in str(logined_user)

                    logined_user_budget = login.get(id_login)[1]

                    if int(delete_course_student) <= len(logined_user) and int(delete_course_student) >= 0 and for_deletecourse_student == True and delete_course_student_sure == "y":
                        login.get(id_login)[2].pop(selected_course)
                        login.get(id_login)[1] = logined_user_budget + selected_course_value * 100
                        print selected_course + " has been successfully added to your courses."
                        break
                    else:
                        print "Please type valid number!"
                        continue
                continue
            elif user_menu == "3":
                logined_user = login.get(id_login)[2].keys()
                logined_user_value = login.get(id_login)[2].values()
                print "*** Offered Courses ***\n \nCourse name---Credit"
                n = 0
                for i in range(len(logined_user)):
                    print str(n + 1) + "-" + str(logined_user[n]) + "---" + str(logined_user_value[n])
                    n = n + 1
                continue
            elif user_menu == "4":
                print "----- BUDGET MENU -----"
                user_budget = login.get(id_login)[1]
                print "Your budget is:" + str(user_budget)
                while True:
                    print "1-Add money\n2-Go to main menu\n"
                    budgetmenu = raw_input("What do you want to do ?:")
                    if budgetmenu == "1":
                        add_money_tobudget = raw_input("Aamount of money:")
                        login.get(id_login)[1] = login.get(id_login)[1] + int(add_money_tobudget)
                        print "Your budget has been updated."
                        break
                    elif budgetmenu == "2":
                        print "Going to student menu"
                        break
                continue
            elif user_menu == "5":
                break
        continue