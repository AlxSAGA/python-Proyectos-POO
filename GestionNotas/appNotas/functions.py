# Libraries
import sys, signal, os
from termcolor import colored as c

# Importing classes
from classes import NotesManager

# Custom Functions
def ctrl_c(signal, frame):
    print(c(f"\n\n[-] Finished...", "red"))
    sys.exit(1)

# ctrl_c
signal.signal(signal.SIGINT, ctrl_c)

def finish_program():
    print(c("\n\n[+] Program completed successfully...", "green"))
    sys.exit(0)
    
def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Menus
def main_menu():
    print(c(f"\n(1)addNote - (2)readNotes - (3searchNote) - (4)deleteNota - (5)cleanScreen - (0)finishProgram", "cyan"))


# User notes created
def user_notes(notes_manager):
    create_note = input(c(f"\n[+] Create a note?   ", "blue"))

    notes_manager.add_notes(create_note)

def get_notes(notes_manager):
    read_note = notes_manager.read_notes()

    print(c(f"\n--------------------\nYour notes\n--------------------\n", "blue"))
    for i, note in enumerate(read_note):
        print(c(f"{i}: {note}", "cyan"))

def search_words(notes_manager):
    search_word = str(input(c(f"\n[+] Enter a word?  ", "blue")))

    notes = notes_manager.search_notes(search_word)

    print(c(f"\n--------------------\nYour notes\n--------------------\n", "blue"))
    for i, note in enumerate(notes):
        print(c(f"\n{i}: {note}", "cyan"))

def delete_notes(notes_manager):
    index_note = int(input(c(f"\n[-] Enter the index of the note to be delete?  ", "blue")))

    notes_manager.delete_index_note(index_note)
