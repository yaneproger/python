
def user_interface():
    entered_data = None
    while entered_data != '4' or entered_data >= '5':
        print("Menu 3 :\n"
              "1.Add contact\n"
              "2.find contact\n"
              "3.print contacts\n"
              "4.exit\n")
        # command = input("Select menu number : ")
        entered_data = input("Select menu number 5 : ")

        while entered_data not in ("1", "2", "3", "4"):
            print("Wrong input")
        else:
            # entered_data = input("Select your search type 4 :")
            match entered_data:
                case '1':
                    input_data()
                case '2':
                    search_data()
                case '3':
                    print_data()
                case '4':
                    print('Game over')

                    