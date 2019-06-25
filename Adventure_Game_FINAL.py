import time
import random

badguys = ["pirates", "thiefs", "terrorists"]

badguys = random.choice(badguys)

items = []


def print_pause(text):
    print(text)
    time.sleep(1)


def intro_display():
    print_pause("You have just woken up from a dream.")
    print_pause("You were kidnapped by " + badguys +
                " and find yourself in a priosioners' room of a big ship.")
    print_pause("The window is opened and"
                " you have a poor diving mask in your hand.")
    print_pause("It is night, everybody is sleeping "
                "and you have a chance to scape. \n")


def sea():
    print_pause("Enter 1 to jump off the ship\n"
                "Enter 2 to get in the basement\n")
    user_choice1 = input("What would you like to do? \n"
                         "(Please enter 1 or 2.) \n")
    if user_choice1 == '1':
        if "Gun and oxygen cylinder" in items:
            print_pause("You load the gun, put the oxygen cilinder"
                        " in yourself and jumped overboard.")
            print_pause("The " + badguys +
                        " woke up with the noise.")
            print_pause("You are now submerse and "
                        "breathing through the oxygen cylinder.")
            print_pause("They search everywhere in the sea,"
                        "but they can't see you.")
            print_pause("You wait for a while and catch them by surprise."
                        " You start shooting them and defeat your enemies")
            print_pause("Finally you free the other prisioners and "
                        "start sailing towards home. YOU WON =) ")
        else:
            print_pause("You jumped into the sea, but"
                        " the " + badguys +
                        " woke up with the noise.")
            print_pause("They are armed and looking for the water, "
                        " but you are submerse, they did not see you yet.")
            print_pause("It would be very difficult to "
                        "swim without doing noise. \n")
            user_choice2 = ''
            while user_choice2 != '1' and user_choice2 != '2':
                user_choice2 = input("Would you like to (1) swim crawl"
                                     " as fast as you can or (2) hide yourself"
                                     "in the ship hull and get back by"
                                     " its window. \n")
                if user_choice2 == '1':
                    print_pause("You start swim as fast as you can,"
                                " but the noise is inevitable...")
                    print_pause("The " + badguys +
                                " hear you swimming.")
                    print_pause("They start shooting you.")
                    print_pause("Unfortunately you got hitted "
                                "and die immediately.")
                    print_pause("GAME OVER =(")
                    play_again()
                elif user_choice2 == '2':
                    prisioner_room()
    elif user_choice1 == '2':
        basement()


def prisioner_room():
    print_pause("You get back to the prisioners'room. \n")
    sea()


def basement():
    print_pause("You silenty get in the ship's basement.")
    if "Gun and oxygen cylinder" in items:
        print_pause("The pirates go back to sleep.")
        print_pause("But wait... You've been here before, and "
                    "gotten all the good stuff. "
                    "It's just a basement full of dirty rats.")
        prisioner_room()
    else:
        print_pause("You find a waterproof gun and"
                    "an oxygen dive cylinder!")
        print_pause("You take both items.")
        print_pause("Now you are prepared for the sweet scape.")
        print_pause("You get back to the prisioners' "
                    "room and the window still opened. \n")
        items.append("Gun and oxygen cylinder")
        sea()


def play_again():
    play_again = input("Would you like to play again? (yes) or (no) ").lower()
    if 'no' in play_again:
        print_pause("OK, goodbye!")
    elif 'yes' in play_again:
        print_pause("Great! Let's go. \n")
        if('Gun and oxygen cylinder' in items):
            items.remove('Gun and oxygen cylinder')
            adventure_game()


def adventure_game():
    intro_display()
    sea()
    play_again()


adventure_game()
