def print_menu():
    """
    Prints the program menu to the console.
    :return: None
    """
    print('Menu:')
    print('a - Add a new name')
    print('d - Delete a name')
    print('p - Print all names')
    print('s - Search for a name.')
    print('q - Quit program.')
    print('Enter the letter next to the menu item you wish to use: ', end="")


# Initialize the band_roster to be empty.
band_roster = []

# Print the menu and ask for the first menu selectionl.
print_menu()
action = input()
print()

while action != 'q':
    if action == 'a':
        name = input("Enter a name you want to ADD: ")
        band_roster.append(name)
        print("Name added!")
    elif action == 'd':
        name = input("Enter a name you want to DELETE: ")
        if name in band_roster:
            band_roster.remove(name)
            print("Name removed!")
        else: print("There is no one with that name!")
    elif action == 'p':
        print("The roster consists of: ")
        i = 1
        for elem in band_roster:
            print (str(i) + ". " + elem)
            i += 1
    elif action == 's':
        name = input("Who do you want to find?: ")
        if name in band_roster:
            print("This person is in the roster!")
        else: print("There is no one with that name!")
    elif action == 'q':
        pass
    else:
        print('That was not a valid choice!  Try again.')

    print_menu()
    action = input()
    print()

print("Thanks for using this program!")
