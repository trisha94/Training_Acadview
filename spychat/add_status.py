from globals import status_message
updated_status_messages = None

def add_status(current_status_messages):
    if current_status_messages != None :
        print "Your current status is %s \n" %(current_status_messages)
    else :
        print "You don't have any status currently"

        #ask user from choosing from older messages
    default = raw_input("do you want to select from older messages 'Y/N'")
    if default.Upper=='N':
        new_status_message  = raw_input("What status message do you want to update")
        if (new_status_message>0) :
             # adding new status message to the list
                status_message.append(new_status_message)
                updated_status_message = new_status_message
                print "your status update is:" + new_status_message
                #current_status_messages = updated_status_message

        else :
            print "You did not provide any status message"
    if default.Upper == 'Y':
        msg_no = 1
        #print all older messages
        for message in status_message :
            print str(msg_no) +  "  " + message
            msg_no +1
#return updated_status_message