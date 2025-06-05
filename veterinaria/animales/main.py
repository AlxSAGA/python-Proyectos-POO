#!/usr/bin/env python3

# Libraries
from termcolor import colored as color

# Import custom functions
from functions import ctrl_c, finish_program, clean_screen
from functions import animal_menu, pet_menu, register_pet

# Import classes
from veterinariaAnimales import Animal, AnimalVeterinary

# Main function
def main():
    
    welcome_message = color("\n[+] Welcome to my pet vet\n", "cyan")
    veterinary = AnimalVeterinary(welcome_message)

    while True:
        animal_menu()

        option_animal_menu = input("\n\n===>   ")

        if option_animal_menu == "1":
            
            pet_menu()

            option_register = input("\n\n===>   ")

            if option_register == "1":

               register_pet(veterinary) # Instance veterinary
               
            elif option_register == "2":

                register_pet(veterinary) # Instance veterinary

            else:
                
                print(color("\n[-]Error: Invalid Option...\n"))

        elif option_animal_menu == "2":

            veterinary.show_pets()

        elif option_animal_menu == "3":
            
            pet_name = input("\n[+] Enter your pet's name?   ")
            veterinary.return_pet(pet_name)

        elif option_animal_menu == "4":
            
            clean_screen()

        elif option_animal_menu == "0":
            
            finish_program()

        else:
            
            print(color("\n[-] Error, Invalid Option...\n"))
    
# Main flow of the program
if __name__ == "__main__":
    main()
