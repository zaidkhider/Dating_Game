while True:

    print('............Chapter 1.............')
    print("You are Ollie, a likeable young guy in search of love. Our story begins when Ollie comes across an attractive young woman on Tinder...")

    swipe_choice = input("Will you swipe left or right?: (1)Right (2)Left").lower().strip()


    if 'right' in swipe_choice or swipe_choice == '1':
        print("She swiped right, too! It's a match! Now don't screw this up...")
    else:
        print("Hmm, perhaps Ollie's standards are a little high... GAME OVER")
        print('END OF GAME!')
        break

    print ('..........Chapter 2.............')
    print ('She messages you and asks for a date! But she wants you to pick the type of restaurant.')

    food_choice = input("What kind of food will you choose?: (1)Italian (2)Curry (3)Pub grub").lower().strip()
    if 'italian' in food_choice or 1 in food_choice:
        print("Ah, molto bella!")
    elif 'curry' in food_choice or 2 in food_choice:
        print("Curry on a first date!? What were you thinking? GAME OVER!!")
    elif 'pub grub' in food_choice or 3 in food_choice:
        print ("Lovely jubbly.")
    else:
        print("EWWWWW, you've got the worst food taste! Ask someone else loser!")
        print("END OF GAME!")
        break

    print('.........Chapter 3..........')


    drunk_guess = input( "You meet at the restaurant and after an hour, everything seems to be going fine! However, you notice your date might have had a bit much to drink... what do you think? (Enter true or false)").lower().strip()

    print("Whatever you say! Oh no, now she's asking how old you think she is! Maybe she's had too much drink to really notice what you say...")
    age_guess = int(input("What age will you say?"))

    if age_guess < 30 or drunk_guess == 'true':
        print("She smiles and shrugs. 'I'll never tell!' Phew, that was a close one!")
    else:
        print("Uh, I think you might have miscalculated somewhere... GAME OVER")
        print ("END OF GAME")
        break

    print('.......Chapter 4.........')

    print("The rest of the evening goes wonderfully and soon, the bill arrives. Yikes! £100!?")

    pay_choice = input("What will you do?: (1)Say you left your wallet at home. (2)Offer to pay.").strip().lower()

    money_in_wallet = int(input("Wait... how much money do you actually have?"))

    if pay_choice == 'offer to pay' or pay_choice == 1 and money_in_wallet >= 100 :
        print ("How very gallant of you! She seems impressed...")
        print ("I'm yours!")
    else:
        print("Sorry, nobody likes a cheapskate.")
        print("END OF GAME")
        break

