#!/usr/bin/env python3

# Libraries
from termcolor import colored as c

# Main Class 
class Vehicle:
    
    def __init__(self, vehicle_registration, vehicle_brand, vehicle_model):
        self.vehicle_registration = vehicle_registration
        self.vehicle_brand = vehicle_brand
        self.vehicle_model = vehicle_model
        self.vehicle_available = True

    def rent_a_vehicle(self):
        if self.vehicle_available:
            self.vehicle_available = False
            print(c(f"\n[+] Vehicle with licence plate: ( {self.vehicle_registration} ), correctly authorized...", "green"))
        else:
            print(c(f"\n[-] Vehicle not available...", "red"))

    def return_the_vehicle(self):
        if not self.vehicle_available:
            self.vehicle_available = True
            print(c(f"\n[+] Vehicle with licence plate: ( {self.vehicle_registration} ), delivered correctly...", "green"))
        else:
            print(c(f"\n[+] Vehicle with licence plate: ( {self.vehicle_registration} ), is currently available...", "green"))

    def __str__(self):
        return c(f"[+] Vehicle: ({self.vehicle_brand} - {self.vehicle_model}), Registration: -> {self.vehicle_registration}, Available={self.vehicle_available}", "blue")
    
class VehicleStorage:

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def rent_vehicle(self, registration):
        for vehicle in self.vehicles:
            if vehicle.vehicle_registration == registration:
                vehicle.rent_a_vehicle()

    def return_vehicle(self, registration):
        for vehicle in self.vehicles:
            if vehicle.vehicle_registration == registration:
                vehicle.return_the_vehicle()

    
    def __str__(self):
        return '\n'.join(str(show_vehicle) for show_vehicle in self.vehicles)

# Section objects

