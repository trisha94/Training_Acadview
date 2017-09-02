#take input from user
from add_status import add_status
from add_friend import add_friend
def start_chat(name,age,rating,status):
    from globals import current_status_message
    #validation user details
    error_message =  None #Variable for storing error
    if not (age<12 and age >50):
        error_message = "Invalid age. Provide correct age"
        print error_message
    else :
        welcome_message = "Authentication completed. Welcome Name :" +  name + "\n Age:" + str(age) + "\nRating: " + str(rating)
        print welcome_message

        #display menu for user
        show_menu = True
        while show_menu :
            choices = "What do you want to do ?\n 1. Add a status update \n 2. Add a friend\n 3. Send a secret message\n 4.Read a secret message\n 5.Read chat from user \n 6.Exit application"
            menu_choice = int(raw_input(choices))
            if (menu_choice == 1):
                current_status_message =  add_status(current_status_message)
            elif (menu_choice == 2):
                number_of_friends = add_friend()
                print "You have %s no of friends"
            elif (menu_choice == 3):
            elif (menu_choice == 4):
            elif (menu_choice == 5):
            elif (menu_choice == 6):
                #close application
                show_menu = False
            else :
                print ' Wrong choice try again '


