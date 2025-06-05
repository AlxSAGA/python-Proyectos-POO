#!/usr/bin/env python3

# Libraries
import sys, signal, os
from termcolor import colored as color 

# Class import 
from veterinariaAnimales import Animal, AnimalVeterinary

# Custom functions
def ctrl_c(signal, frame):
    print(color("\n\n[-] Finished...", "red"))
    sys.exit(1)

# ctrl_c
signal.signal(signal.SIGINT, ctrl_c)

def finish_program():
    print(color("\n\n[+] Program completed successfully..", "green"))
    sys.exit(0)

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

def animal_menu():
    print((color("\n[+] Select an option:  (1) Register pet - (2) Show Pets - (3) Return pets - (4) Clean Screen - (0) Exit", "cyan")))

def pet_menu():
    print(color("\n[+] Select an option:   (1) Register Dog - (2) Register Cat\n", "cyan"))

def register_pet(veterinary): # Instance veterinary:
    print(color("\n[+] Enter the following data...\n", "blue"))

    message_client_name = color("\n[+] Client name?  ", "cyan")
    message_pet_name = color("\n[+] Pet name?   ", "cyan")
    message_type_animal = color("\n[+] Type of pet?   ", "cyan")

    option_register_client = input(message_client_name).title()
    option_register_pet = input(message_pet_name).title()
    option_register_type = input(message_type_animal).title()

    animal = Animal(option_register_client, option_register_pet, option_register_type)
    
    veterinary.add_animal(animal)

    print(color("\n[+] pet successfully registered", "green"))
