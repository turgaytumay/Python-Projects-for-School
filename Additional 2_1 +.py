from datetime import *

users = {"ahmet":"1122", "meryem":"3344"}
inventory={'asparagus':[10,5],'broccoli':[15,6],'carrots':[18,7],
 	'apples':[20,5],'banana':[10,8],'berries':[30,3],
 	'eggs':[50,2],'mixed fruit juice':[0,8],'fish sticks':[25,12],
 	'ice cream':[32,6], 'apple juice':[40,7], 'orange juice':[30,8],
'grape juice':[10,9]}
basket = []
basket_amount = []
total_price = 0




inventory_list = []
lel = inventory.keys()
inventory_list.append(lel)


print " ***** Welcome to Sehir Online Market ***** "
while True:
    print "Please log in by providing your user credentials:"
    name_entry = raw_input("User Name:")
    password_entry = raw_input("Password:")

    if users[name_entry] == password_entry:
        print "Successfully logged in!"
        user_name = name_entry
        while True:
            print "Welcome, " + user_name + "! Please choose one of the following options by entering \nthe corresponding menu number. "
            print """
                Please choose one of the following services:

                1- Search for a product
                2- See Basket
                3- Check Out
                4- Logout
                5- Exit

                """
            menu_entry = raw_input("Your Choice:")
            if menu_entry == "1":
                print """
                        Please choose one of the following services:

                        1- Eggs                 $5
                        2- Carrots              $6
                        3- Grape Juice          $7
                        4- Broccoli             $5
                        5- Ice Cream            $8
                        6- Orange Juice         $3
                        7- Asparagus            $2
                        8- Fish Sticks          $8
                        9- Apples               $12
                        10- Mixed Fruit Juice   $6
                        11- Berries             $7
                        12- Banana              $8
                        13- Apple Juice         $9

                        """
                product = raw_input("Please select which item you want to add to your basket (Enter 0 for main menu) :")
                if product != 0:

                    selected_product = inventory_list[0][int(product) - 1]
                    print "Adding " + str(selected_product)
                    while True:
                        Amount = int(raw_input("Enter Amount:"))
                        if Amount > 0 and Amount <= int(inventory[selected_product][-2]):
                            print "Added " + str(selected_product)
                            inventory[selected_product][-2] = inventory[selected_product][-2] - Amount
                            add_for_basket = selected_product, "price = $", inventory[selected_product][
                                -1], "total = $", Amount * int(inventory[selected_product][-1])
                            amount = "amount = ", Amount
                            total_price = total_price + Amount * int(inventory[selected_product][-1])
                            basket.append(str(add_for_basket))
                            basket_amount.append(str(amount))
                            break
                        elif Amount == 0:
                            print "Going back to main menu ..."
                            break
                        else:
                            print "Sorry! the amount exceeds the limit or invilid number, Please try again with smaller amount"
                            continue
                    continue
                elif int(product) <= 0 or int(product) >= 14:
                    print "Your search did not match any items. Please try something else (Enter 0 for main menu) :"
                    continue

            elif menu_entry == "2":
                for i in range(len(basket)):
                    print basket[int(i)], basket_amount[int(i)]
                    print " "
                print """
                                1- Update amount
                                2- Remove an item
                                3- Check out
                                4- Go back to main menu

                                """
                Option = raw_input("Please Choose an option:")
                if Option == "1":
                    change_amount_item = raw_input("Please select which item to change its amount:")
                    changed_amount = raw_input("Please type the new amount:")
                    basket_amount[int(change_amount_item) - 1] = "amount :", changed_amount
                    print "Your basket now contains:"
                    for i in range(len(basket)):
                        print basket[int(i)], basket_amount[int(i)]
                        print " "
                    continue
                elif Option == "2":
                    remove_basket = raw_input("Please select product to remove from your basket:")
                    basket.pop(int(remove_basket) - 1)
                    basket_amount.pop(int(remove_basket) - 1)
                    print "Your basket now contains:"
                    for i in range(len(basket)):
                        print basket[int(i)], basket_amount[int(i)]
                        print " "
                    continue
                elif Option == "3":
                    print """
                            ***** Sehir Online Market *****
                            *******************************
                                  4444034 sehir.edu.tr
                            -------------------------------
                                                        """
                    for i in range(len(basket)):
                        print basket[int(i)], basket_amount[int(i)]
                        print " "

                    print """
                            -------------------------------
                                                        """
                    print "                    Total $", total_price
                    print """
                            -------------------------------
                                                        """
                    print datetime.now()
                    print "                     Thank you for using our Market!"
                    continue
                elif Option == "3":
                    break
                else:
                    continue

            elif menu_entry == "3":
                print """
                                    ***** Sehir Online Market *****
                                    *******************************
                                          4444034 sehir.edu.tr
                                    -------------------------------
                                                                """
                for i in range(len(basket)):
                    print basket[int(i)], basket_amount[int(i)]
                    print " "

                print """
                                    -------------------------------
                                                                """
                print "Total $", total_price
                print """
                                    -------------------------------
                                                                """
                print datetime.now()
                print "Thank you for using our Market!"
                continue
            elif menu_entry == "4":
                break

            elif menu_entry == "5":
                exit()

            else:
                continue
        continue

    else:
        continue



