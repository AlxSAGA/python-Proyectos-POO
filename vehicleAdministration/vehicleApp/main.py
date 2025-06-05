#!/usr/bin/env python3

# Libraries
from termcolor import colored as c  

# Custom Libraries
from .functions import ctrl_c, finish_program, clean_screen, main_menu, add_vehicle_instance

# Class Import 
from .classes import Vehicle, VehicleStorage 

# Main Function
def main():
    
   vehicle = VehicleStorage()

   print(c(f"\n[+] Welcome to the vehicle storage...", "cyan"))

   while True:
       main_menu()

       main_option = input(c(f"\n[+] ===>  ", "cyan"))

       if main_option == "1":

            add_vehicle_instance(vehicle)
       
       elif main_option == "2":

            print(vehicle)

       elif main_option == "3":
            
            registration = str(input(c("\n[+] Enter the registration?  ", "cyan")))
            vehicle.rent_vehicle(registration)

       elif main_option == "4":

            registration = str(input(c("\n[+] Enter the registration?  ", "cyan")))
            vehicle.return_vehicle(registration)

       elif main_option == "5":

           clean_screen()

       elif main_option == "0":

           finish_program()

       else:

           print(c(f"\n[-] Error: Option invalid...", "red"))

# Main flow of the program
if __name__ == "__main__":
    main()
