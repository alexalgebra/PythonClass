# Greet the user, get their name
def greeting():
    userName = raw_input("Welcome to the lottery! What's your name? ")
    print "Hi, " + userName + "!"

# Ensure the user is 18, if not, let them know when they can come back
def ageCheck():
    userAge = input("How old are you? ")
    if userAge >= 18:
        print "Great, you're old enough to play!"
    else:
        print "Sorry, you must be 18 to play."
        yearsLeft = 18-userAge
        print "Please come back in " + str(yearsLeft) + " years."

# Run the program
greeting()
ageCheck()
