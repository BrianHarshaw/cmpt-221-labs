#I spent over an hour trying to figure out what was wrong with using a relative import in this form
#when the files are in the same directory, but since I can't figure it out I have had to use the vehicle.py
#file to run my tests instead of the test file that we were supposed to use
from .vehicle import *

#Instantiating a regular vehicle, a motorcycle, and a semi truck
v1 = Vehicle(20, 30, 0)
m1 = Motorcycle(15, 10, 0, False)
s1 = Semi(10, 50, 0, 1500)
#Showing the fuel states for all vehicles
print("All of the vehicles that have been initiated have no fuel.")
print("Vehicle 1's current fuel: ", v1.current_fuel)
print("Motorcycle 1's current fuel: ", m1.current_fuel)
print("Semi 1's current fuel: ", s1.current_fuel)

v1.add_fuel(15)
m1.add_fuel(10)
s1.add_fuel(35)

print("All of the vehicles have been given fuel.")
print("Vehicle 1's current fuel: ", v1.current_fuel)
print("Motorcycle 1's current fuel: ", m1.current_fuel)
print("Semi 1's current fuel: ", s1.current_fuel)

#Checking the odometer of all the cars before driving
print("Vehicle odometers before being driven.")
print("Vehicle 1's distance driven: ", v1.odometer)
print("Motorcycle 1's distance driven: ", m1.odometer)
print("Semi 1's distance driven: ", s1.odometer)

v1.drive_vehicle(250)
m1.drive_vehicle(130)
s1.drive_vehicle(320)
#Checking odometers after the vehicles have been drive
print("Vehicle odometers after being driven.")
print("Vehicle 1's distance driven: ", v1.odometer)
print("Motorcycle 1's distance driven: ", m1.odometer)
print("Semi 1's distance driven: ", s1.odometer)


