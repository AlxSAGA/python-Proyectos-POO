#!/usr/bin/env python3

# Import libraries
import pickle
from termcolor import colored as c

# Import classes
from notes import Notes

# Main Class 
class NotesManager:
    def __init__(self, notes_file='notes.pkl'):
        self.notes_file = notes_file

        try:

            with open(self.notes_file, 'rb') as file:
                self.file_content = pickle.load(file) # Deserializes the object from a file

        except FileNotFoundError as e:

            self.file_content = [] # If it not exist, it is an empty list

    def save_notes(self):

        try:

            with open(self.notes_file, 'wb') as file:
                pickle.dump(self.file_content, file) # We update notes in file
        except FileNotFoundError as e:
            
            print(e)

    def add_notes(self, create_note):
        self.file_content.append(Notes(create_note))
        self.save_notes()

    def read_notes(self):
        return self.file_content

    def search_notes(self, search_word):
        return [note for note in self.file_content if note.matching_word(search_word)] # Instance of the Notes class

    def delete_index_note(self, index_note):
        if index_note < len(self.file_content):
            
            del self.file_content[index_note]
            self.save_notes()

            print(c(f"\n[-] Note successfully deleted...", "green"))
        
        else:

            print(c(f"\n[-] The index does not exist...", "red"))
