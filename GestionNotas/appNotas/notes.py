#!/usr/bin/env python3

# Class notes
class Notes:
    def __init__(self, create_note):
        self.create_note = create_note

    def matching_word(self, search_word):
       return search_word in self.create_note

    def __str__(self):
        return self.create_note # Attribute of the temporary object created in add_notes.
