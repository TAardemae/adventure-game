import time
import random

enemies = ['pirate', 'dragon', 'wicked fairie', 'troll', 'gorgon']


def print_pause(message_to_print, pause):
    print(message_to_print)
    time.sleep(pause)


def intro(enemy):
    print_pause('You find yourself standing in an open field, filled with '
                'grass and yellow wildflowers.', 2)
    print_pause('Rumor has it that a ' + enemy + ' is somewhere around '
                'here, and has been terrifying the nearby village.', 2)
    print_pause('In front of you is a house.', 2)
    print_pause('To your right is a dark cave.', 2)
    print_pause('In your hand you hold your trusty (but not very '
                'effective) dagger.\n', 2)


def field(items, enemy):
    print_pause('Enter 1 to knock on the door of the house.', 1)
    print_pause('Enter 2 to peer inside the cave.', 1)
    print_pause('What would you like to do?', 1)
    field_decision(items, enemy)


def field_decision(items, enemy):
    decision = input('(Please enter 1 or 2.)\n')
    if decision == '1':
        house(items, enemy)
    elif decision == '2':
        cave(items, enemy)
    else:
        field_decision(items, enemy)


def house(items, enemy):
    print_pause('You approach the door of the house.', 1)
    print_pause('You are about to knock when the door opens and out '
                'steps a ' + enemy + '.', 1)
    print_pause("Eep! This is the " + enemy + "'s house! ", 1)
    print_pause('The ' + enemy + ' attacks you!', 1)
    if 'sword' not in items:
        print_pause('You feel a bit under-prepared for this, what with '
                    'only having a tiny dagger.', 1)
        house_decision(items, enemy)
    else:
        house_decision(items, enemy)


def house_decision(items, enemy):
    response = input('Would you like to (1) fight or (2) run away?\n')
    if response == '1':
        fight(items, enemy)
    elif response == '2':
        print_pause("You run back into the field. Luckily, you don't "
                    "seem to have been followed.\n", 1)
        field(items, enemy)
    else:
        house_decision(items, enemy)


def cave(items, enemy):
    print_pause('You peer cautiously into the cave.', 1)
    if 'sword' in items:
        print_pause("You've been here before, and gotten all the good "
                    "stuff. It's just an empty cave now.", 1)
        print_pause('You walk back out to the field.\n', 1)
        field(items, enemy)
    else:
        print_pause('It turns out to be only a very small cave.', 1)
        print_pause('Your eye catches a glint of metal behind a rock.', 1)
        print_pause('You have found the magical Sword of Ogoroth!', 1)
        print_pause('You discard your silly old dagger and take the '
                    'sword with you.\n', 1)
        items.append('sword')
        field(items, enemy)


def fight(items, enemy):
    if 'sword' in items:
        print_pause('As the ' + enemy + ' moves to attack, you unsheathe '
                    'your new sword.', 1)
        print_pause('The Sword of Ogoroth shines brightly in your hand as '
                    'you brace yourself for the attack.', 1)
        print_pause('But the ' + enemy + ' takes one look at your shiny '
                    'new toy and runs away!', 1)
        print_pause('You have rid the town of the ' + enemy + '. You '
                    'are victorious!', 1)
        play_again_decision(items, enemy)
    else:
        print_pause('You do your best...', 1)
        print_pause('but your dagger is no match for the ' + enemy + '.', 1)
        print_pause('You have been defeated!', 1)
        play_again_decision(items, enemy)


def play_again_decision(items, enemy):
    response = input('Would you like to play again? (y/n)\n')
    if response == 'y':
        print_pause('Excellent! Restarting the game ...', 1)
        play_game()
    elif response == 'n':
        print_pause('Thanks for playing! See you next time.', 1)
    else:
        play_again_decision(items, enemy)


def play_game():
    items = []
    enemy = random.choice(enemies)
    intro(enemy)
    field(items, enemy)


play_game()
