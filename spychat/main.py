from spy_details  import spy_salutation,spy_name,spy_age,spy_rating,spy_is_online  #to import default details
from start_chat import start_chat
#Starting point of application
print "Let's get Started"
question =  "Do you want to continue as" + spy_salutation + " " + spy_name + "(Y/N)"
existing =  raw_input(question)
if(existing.Upper == "Y"):
    #User wants to continue as default user

    spy_name = spy_salutation + " " + spy_name

    # start chat application
    start_chat(spy_name,spy_age,spy_rating)

elif(existing.Upper=="N") :
    # User wants to continue as new user
    name = raw_input("What is your name?")
    print ("welcome " +name)
    if(len(name)>0): #check is the input is null or not
        spy_salutation = raw_input("What should I call you")
        spy_name = raw_input("What is your name")
        spy_age = raw_input("What is your age")
        spy_age = int(spy_age)
        spy_rating  = raw_input("Provide your rating")
        spy_rating = float(spy_rating)
        spy_is_online = True
        print("Hello" +spy_salutation)

