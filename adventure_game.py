def adventure_game():

    print("You stand on a cracked path at a fork before an old oak forest.")
    direction_choice = input("Will you go left or right?").lower()
    
    while True:

        if direction_choice != "left" and direction_choice != "right":
            direction_choice = input("You must go 'left' or 'right'!").lower()
            continue
        else:
            break

    if direction_choice == "left":
        
        print("You head left, striding under thick branches until you come "
              "to a circular clearing. In the centre is an moss-covered "
              "sundial with a torch and a pair of sunglasses upon it.")

        item_choice = input("Will you take the torch or the "
                            "sunglasses?").lower()
        
        while True:

            if item_choice != "torch" and item_choice != "sunglasses":
                item_choice = input("You must take the 'torch' or the "
                                    "'sunglasses'!").lower()
                continue
            else:
                break

        if item_choice == "torch":
            print("You pick up the %s and proceed down the path on the opposite"
            " side of the clearing. The branches above thicken, blocking out the"
            " sun. You turn on the %s, just in time to see and step over a protruding"
            " root. After a few minutes, you exit the forest, and see ahead that your"
            " path meets up with another joining from the right."%(item_choice,
            item_choice))

        if item_choice == "sunglasses":
            print("You pick up the %s and proceed down the path on the opposite"
            " side of the clearing. The branches above thin out, glaring sunlight"
            " streaming through. You put on the %s, just in time to see and step"
            " over a raised paving slab. After a few minutes, you exit the forest,"
            " and see ahead that your path meets up with another joining from the"
            " right."%(item_choice,item_choice))       


    if direction_choice == "right":
        print("right")

adventure_game()