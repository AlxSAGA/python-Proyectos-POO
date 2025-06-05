#!/usr/bin/env python3

# import custom functions
from functions import ctrl_c, finish_program, clean_screen, main_menu, user_notes, get_notes, search_words, delete_notes
from termcolor import colored as c

# Importing classes
from classes import NotesManager

# Main Function
def main():

    notes_manager = NotesManager() # Intance of the class

    print(c(f"\n------------------------------\nWelcome to alx management notes\n------------------------------\n", "cyan"))
    
    while True:
        main_menu()
        main_option = input(c("\n[+] Select an option:   ", "blue"))

        if main_option == "1":

            user_notes(notes_manager)

        elif main_option == "2":

            get_notes(notes_manager)

        elif main_option == "3":

            search_words(notes_manager)

        elif main_option == "4":

            delete_notes(notes_manager)

        elif main_option == "5":
            
            clean_screen()

        elif main_option == "0":
            
            finish_program()

        else:

            print(c(f"\n[-] Error: Invalid option...", "red"))

# Main flow of the program
if __name__ == "__main__":
    main()
