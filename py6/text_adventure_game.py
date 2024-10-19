import time

def print_pause(message):
    print(message)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked dragon is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

def cave(items):
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and you've already taken the sword. It's just an empty cave now.\n")
    else:
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword with you.\n")
        items.append("sword")
    print_pause("You walk back out to the field.\n")
    field(items)

def house(items):
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a dragon.")
    print_pause("Eep! This is the dragon's house!")
    print_pause("The dragon attacks you!\n")
    if "sword" in items:
        print_pause("You draw your new Sword of Ogoroth. The dragon takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the dragon. You are victorious!\n")
    else:
        print_pause("You feel under-prepared with only your dagger.")
        print_pause("You have been defeated!\n")
    play_again()

def field(items):
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    choice = input("(Please enter 1 or 2.)\n")
    if choice == '1':
        house(items)
    elif choice == '2':
        cave(items)
    else:
        field(items)

def play_again():
    choice = input("Would you like to play again? (y/n)\n").lower()
    if choice == 'y':
        play_game()
    elif choice == 'n':
        print_pause("Thanks for playing! See you next time.")
    else:
        play_again()

def play_game():
    items = []
    intro()
    field(items)

play_game()
