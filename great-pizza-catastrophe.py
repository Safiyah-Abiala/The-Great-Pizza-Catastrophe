while True:
    Player = input("""
               !!!Welcome To The Great Pizza Catastrophe!!!
               Are you ready to start the adventure game? (yes/no): 
               """).lower()
    
    if Player == "yes":
        print("Game begins")
    elif Player == "no":
        print("Maybe another time. Goodbye")
        break


    print("""
        You're delivering pizza to a spooky mansion, 
        You knocked
        ....Knock..knock....... 
        you look around and there is a bat shaped pet door 
        and a glowing box labeled DO NOT OPEN at the doorstep
        ...Knock...Knock... 
        A pale man, Steve answers.
        There's a crying werewolf inside.
        """)

    Level1 = input("""
                Would you
                A. Hand over the pizza? 
                B. Demand a tip? 
                C. Pet the werewolf: 
                """).lower()

    if Level1 == "hand over the pizza":
        print("Steve collects the pizza angrily")
        
        Level2 = input("""
            What would you do?
            A. Throw cheese
            B. Apologize in spanish
            C. Do the Macarena: 
            """).lower()
        
        if Level2 == "throw cheese":
            print("Steve growls at you angrily and locks you in an abyss")
        elif Level2 == "apologize in spanish":
            print("""
                  Steeve hisses and slams the door on your face. 
                  You leave with a nosebleed
                  """)
        elif Level2 == "do the macarena":
            print("""Steve loves your dance. 
                  But you dance for hours before he lets you leave
                  """)
        else : 
            print("Invalid option. TRY AGAIN")
            
    elif Level1 == "demand a tip":
        print("Steve offers you strange items")
        
        Level2 = input(""" 
                    Which one would you pick
                    A. Rubber chicken
                    B. Glow in the dark fanny pack
                    C. Nephew Phil
                    """).lower()
        
        if Level2 == "rubber chicken":
            print("The chicken crows and chases you forever")
        elif Level2 == "glow in the dark fanny pack":
            print("""
                  There are dollar bills with bloodstains in it
                  You get arrested for murder while spending them.
                  And spend the rest of your life in jail
                  """)
        elif Level2 == "nephew Phill":
            print("""
                  You take Phill home and take care of him
                  CONGRATULATIONS YOU WIN!!!
                  """)
        else :
            print("Invalid option. TRY AGAIN")
            
    elif Level1 == "pet the werewolf":
        print("Steve lets you in and locks the door and you're stuck in the spooky mansion")
        
        Level2 = input("""
                    What would you do to leave the spooky mansion?
                    A. Pay in coupons
                    B. Challenge to a danceoff
                    C. Flee through the pet door
                    """).lower()
        
        if Level2 == "pay in coupons":
            print("""
                  You dont have enough coupons.
                  Steve slays you with a sword. DEAD!!!
                  """)
        elif Level2 == "challenge to a danceoff":
            print("""
                  You dance but Steeve wins and feeds you to the werewolf. DEAD!!!
                  """)
        elif Level2 == "flee through the pet door":
            print("""
                  You escape but sprained your ankle. 
                  CONGRATULATIONS!!!
                  """)
        else :
            print("Invalid option. TRY AGAIN")

    restart = input("""
                    Would you love to go again?
                    """).lower()
    if restart != "yes":
        print("Thanks for playing")
        break