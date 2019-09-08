class Vehicle:
    miles_per_gallon = 0
    max_fuel = 0
    current_fuel = 0
    odometer = 0
    keys_in_ignition = False

    def __init__(self, mpg, max_fuel, odometer):
        self.miles_per_gallon = mpg
        self.max_fuel = max_fuel
        self.odometer = odometer

#Functions for the fuel gauge and tank
    def get_miles_per_gallon(self):
        return self.miles_per_gallon

    def add_fuel(self, amount):
        if self.max_fuel > amount + self.current_fuel:
            self.current_fuel = self.current_fuel + amount
#If the amount of fuel pumped exceeds the max, we resolve that the fuel tank would be filled
        else:
            self.current_fuel = self.max_fuel

#Odometer return function

    def get_miles_driven(self):
        return self.odometer

#Function to put the keys in the ignition or remove them

    def put_in_keys(self):
        self.keys_in_ignition = True

    def remove_keys(self):
        self.keys_in_ignition = False

#Functions handling the driving of the car

    def drive_vehicle(self, distance):
        if self.keys_in_ignition and distance/self.miles_per_gallon <= self.current_fuel:
            self.odometer = self.odometer + distance
            self.current_fuel = self.current_fuel - distance/self.miles_per_gallon
        else:
            print("In order to drive you need the keys and enough fuel!")

class Motorcycle(Vehicle):
    num_of_wheels = 2
    side_car = False

    def __init__(self, mpg, max_fuel, odometer, side_car):
        Vehicle.__init__(self, mpg, max_fuel, odometer)
        self.side_car = side_car

    def remove_side_car(self):
        self.side_car = False

    def add_side_car(self):
        self.side_car = True

#Semi meaning semi truck, or an eighteen wheeler
class Semi(Vehicle):
    num_of_wheels = 18
    max_load = 0
    current_load = 0

    def __init__(self, mpg, max_fuel, odometer, max_load):
        Vehicle.__init__(self, mpg, max_fuel, odometer)
        self.max_load = max_load

    def add_load(self, weight):
        if self.current_load + weight < self.max_load:
            self.current_load = self.current_load + weight

    def remove_load(self, weight):
        if weight <= self.current_load:
            self.current_load = self.current_load - weight




def main():
    # Instantiating a regular vehicle, a motorcycle, and a semi truck
    v1 = Vehicle(20, 30, 0)
    m1 = Motorcycle(15, 10, 0, False)
    s1 = Semi(10, 50, 0, 1500)
    # Showing the fuel states for all vehicles
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

    # Checking the odometer of all the cars before driving
    print("Vehicle odometers before being driven.")
    print("Vehicle 1's distance driven: ", v1.odometer)
    print("Motorcycle 1's distance driven: ", m1.odometer)
    print("Semi 1's distance driven: ", s1.odometer)

    #Demonstrating that the vehicles needs keys by trying to drive before inserting them
    v1.drive_vehicle(250)
    m1.drive_vehicle(130)
    s1.drive_vehicle(320)
    # Checking odometers after the vehicles weren't able to drive
    print("Vehicle odometers have not changed because keys were present.")
    print("Vehicle 1's distance driven: ", v1.odometer)
    print("Motorcycle 1's distance driven: ", m1.odometer)
    print("Semi 1's distance driven: ", s1.odometer)

    v1.put_in_keys()
    m1.put_in_keys()
    s1.put_in_keys()

    v1.drive_vehicle(250)
    m1.drive_vehicle(130)
    s1.drive_vehicle(320)
    # Checking odometers after the vehicles have been driven
    print("Vehicle odometers after being driven.")
    print("Vehicle 1's distance driven: ", v1.odometer)
    print("Motorcycle 1's distance driven: ", m1.odometer)
    print("Semi 1's distance driven: ", s1.odometer)
    #Checked all of the functions for the vehicle, now checking the specific functions for motorcycles and semis

    print("Motorcycle 11 has a side car.", m1.side_car)
    m1.add_side_car()
    print("Adding a side car to motorcycle 1.")
    print("Motorcycle 11 has a side car.", m1.side_car)

    print("The load on semi 1 is: ", s1.current_load , "out of a max load of: ", s1.max_load)
    print("Adding load to semi 1.")
    s1.add_load(300)
    print("The load on semi 1 is now: ", s1.current_load)

if __name__ == "__main__": main()