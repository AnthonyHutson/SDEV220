"""Author: Anthony Hutson
   Date Written: 11/5/2024
   Program Name: M03_Lab
   This program will prompt the user to enter a type of vehicle that the user wants to enter information 
   about. The user will then be prompted to enter information about the vehicle. After the information is
   entered, the program will displayed the information back to the user."""

#Super Class
class Vehicle():
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

#Subclass
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

#User input
user_vehicle = Vehicle(input("Enter the type of vehicle: "))
user_vehicle.year = input("Enter the year of your vehicle: ")
user_vehicle.make = input("Enter the make of your vehicle: ")
user_vehicle.model = input("Enter the model of your vehicle: ")
user_vehicle.doors = input("Does your vehicle have 2 doors or 4?: ")
user_vehicle.roof = input("Does your vehicle have a solid or a sun roof?: ")

#Presentation of user information
print(f"Vehicle type: {user_vehicle.vehicle_type}")
print(f"Year: {user_vehicle.year}")
print(f"Make: {user_vehicle.make}")
print(f"Model: {user_vehicle.model}")
print(f"Number of doors: {user_vehicle.doors}")
print(f"Type of roof: {user_vehicle.roof}")