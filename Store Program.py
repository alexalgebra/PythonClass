#This program will create a store where you can choose items to purchase
#and get a total amount of the cost. It was created to practice loops, functions,
#and exponents.

import time

#Create store inventory with costs
store_items = {'T-shirt':9.99,'Button-down shirt':19.99,'Jeans':29.99,'Slacks':39.99,'Sneakers':29.99,'Loafers':39.99,'Heels':19.99,'Skirt':9.99,'Dress':14.99}

#Create empty cart
cart = {}

#Shopping functions
def menu():
    print 'Welcome to Neon\'s Store!'
    for p in store_items:
        print (p + " $" + str(store_items[p]))
    purchase()

def purchase():
    cart_item=raw_input('\nWhat would you like to buy? ').capitalize()
    if cart_item in store_items:
        cart[cart_item]=store_items.get(cart_item)
    else:
        print 'Invalid item.\n\n'
        menu()
    answer=raw_input('Would you like to buy something else (Y/N)? ').upper()
    if answer=='Y':
        menu()
    elif answer=='N':
        checkout()
    else:
        print 'Invalid answer. Please type Y or N.'
        menu()
    
#Checkout function
def checkout():
    print '\n\nShopping Cart:'
    for q in cart:
        print (q + " $" + str(cart[q]))
    total=sum(cart.values())
    print '\nYour total is: $' + str(round(total**5,2))
    time.sleep(2)
    print '\n\nJust kidding! Your total is: $' + str(total)
    answer = raw_input('Are you ready to buy (Y/N)?').upper()
    while answer=='N':
        count=5
        while count>0:
            print count
            count = count-1
            time.sleep(.5)
        answer = raw_input('Are you ready to buy (Y/N)?').upper()            
    if answer == 'Y':
        print 'Please send money via Paypal.'
    else:
        print 'Invalid answer. Please type Y or N.'

# Run the program            
menu()
