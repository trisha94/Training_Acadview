#practice place holders
name= 'Shaktiman'
roll_no= 42
result= 9.6
print "%s whose Roll Number is %d got %f in the last semester." % (name,roll_no, result)

#import statement
if (existing == "Y"):
    #Continue with the default user/details imported from the helper file.
else:
  spy_name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
  if len(spy_name) > 0:
    spy_salutation = raw_input("Should I call you Mr. or Ms.?: ")

    spy_age = raw_input("What is your age?")
    spy_age = int(spy_age)

    spy_rating = raw_input("What is your spy rating?")
    spy_rating = float(spy_rating)

    spy_is_online = True