#!/usr/bin/env python3

# Libraries
from termcolor import colored as color 

class Animal:

    def __init__(self, client_name, pet_name, animal):
        self.client_name = client_name
        self.pet_name = pet_name
        self.animal = animal
        self.fed_animal = False

    def __str__(self):
        message_client = color(f"{self.client_name}", "cyan")
        return f"[*] Client: ( {message_client} ), Pet: ({self.pet_name})({self.animal}) - {color('Happy','green') if self.fed_animal else color('Sad','red')}"

class AnimalVeterinary:

    def __init__(self, veterinary_name):

        self.veterinary_name = veterinary_name
        self.animals = []

    def add_animal(self, pet):

        self.animals.append(pet)

    def show_pets(self):

        for pets in self.animals:
            print(pets)

    def return_pet(self, name):
        
        for pets in self.animals:
            if pets.pet_name == name:
                self.animals.remove(pets)
                return
            
        print(color("\n[-] Unregistered pet...\n", "red"))
