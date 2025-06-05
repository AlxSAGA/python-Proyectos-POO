#!/usr/bin/env python3

# Libraries
import sys, signal, os
from termcolor import colored as c 

# Class Import 
from classes import Vehicle, VehicleStorage

# Custom Funcions
def ctrl_c(signal, frame):
    print(c("\n\n[-] Finished...", "red"))
    sys.exit(1)

signal.signal(signal.SIGINT, ctrl_c)

def finish_program():
    print(c("\n\n[+] Program completed successfully...", "green"))
    sys.exit(0)

def clean_screen():
    os.system("cls" if os.name == "nt" else "clear")

# Menu Section
def main_menu():
    option_1 = c("(1)Add Vehicle", "blue")
    option_2 = c("(2)Show Vehicles", "blue")
    option_3 = c("(3)Rent a Vehiclle", "blue")
    option_4 = c("(4)Return the Vehicle", "blue")
    option_5 = c("(5)Clean Screen", "blue")
    option_0 = c("(0)Finish Program", "blue")
    print(c(f"\n[+] Select an option: {option_1} - {option_2} - {option_3} - {option_4} - {option_5} - {option_0}", "cyan"))

# Function to add the attributes of the vehicle instance
def add_vehicle_instance(vehicle):
    vehicle_registrarion = str(input(c("\n[+] Enter the vehicle registration number?   ", "blue")))
    vehicle_brand = str(input(c("[+] Enter the vehicle make?   ", "blue")))
    vehicle_model = str(input(c("[+] Enter the vehicle model?   ", "blue")))

    vehicle_storage = Vehicle(vehicle_registrarion, vehicle_brand, vehicle_model)
    vehicle.add_vehicle(vehicle_storage)
