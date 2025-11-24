"""
Que :1. compulsory

Write a menu-driven Python program using Inheritance, Encapsulation, and Polymorphism (without abstraction) to manage 
different vehicle types for a logistics company.

The program must:

1.Create a Vehicle base class with a private registration number, brand, and fuel capacity.
2.Create child classes Car, Truck, and Motorbike that inherit from Vehicle.
3.Demonstrate Encapsulation using getter/setter for the private registration number.
4.Demonstrate Polymorphism by overriding calculate_fuel_efficiency() in each child class:

	a)Car → fuel_capacity × 15
	b)Truck → fuel_capacity × 8
	c)Motorbike → fuel_capacity × 35

5.Provide a menu with options to add vehicles or display all vehicles.
"""

class vehicle : 
    def __init__(self,registration_number,brand,fuel_capacity):
        self.__registration_number = registration_number
        self.brand =brand
        self.fuel_capacity = fuel_capacity
        
    # encap : 
    def get_reg_num(self):
        return self.__registration_number 
    
    def set_new_reg_num(self,new_reg_num):
        self.__registration_number= new_reg_num
    
    # method overriding: 
    def calculate_fuel_efficiency(self):
        return 0 
    
    def show(self):
        print(f"registration number: {self.__registration_number} ")
        print (f"brand: {self.brand}") 
        print (f"fuel capacity: {self.fuel_capacity}")

class car(vehicle):
    def __init__(self, registration_number, brand, fuel_capacity,passenger_capacity):
        super().__init__(registration_number, brand, fuel_capacity)
        self.passenger_capacity = passenger_capacity
        
    def calculate_fuel_efficiency(self):
        return self.fuel_capacity * 15
        
    def show(self):
        super().show()# vehicle.show()
        print(f"passenger capacity: {self.passenger_capacity}")

class truck(vehicle):
    def __init__(self, registration_number, brand, fuel_capacity,cargo_capacity):
        super().__init__(registration_number, brand, fuel_capacity)
        self.cargo_capacity = cargo_capacity
    
    def calculate_fuel_efficiency(self):
        return self.fuel_capacity * 8

    def show(self):
        super().show()# vehicle.show()
        print(f"cargo capacity: {self.cargo_capacity}")

class motorbike(vehicle):
    def __init__(self, registration_number, brand, fuel_capacity,seat_capacity):
        super().__init__(registration_number, brand, fuel_capacity)
        self.seat_capacity = seat_capacity
    
    def calculate_fuel_efficiency(self):
        return self.fuel_capacity * 35

    def show(self):
        super().show()# vehicle.show()
        print(f"seat capacity: {self.seat_capacity}")

vehicle =[]

while True :
    print("VEHICLE MANAGEMENT SYSTEM")
    print("1.add car")
    print("2.add truck")
    print("3.add motorbike")
    print("4.show all vehicles")
    print("5.exit")
    
    choice =int(input("enter the  choice : "))
    
    if choice ==1:
        print("add car")
        reg =input("enter the reg number : ")
        brand =input("enter the brand : ")
        fuel_capacity =int(input("enter the fuel capacity : "))
        passenger =int(input("enter the passenger capacity : "))
        vehicle.append(car(reg,brand,fuel_capacity,passenger))
        
    elif choice ==2:
        print("add truck")
        reg =input("enter the reg number : ")
        brand =input("enter the brand : ")
        fuel_capacity =int(input("enter the fuel capacity : "))
        cargo =int(input("enter the cargo capacity : "))
        vehicle.append(truck(reg,brand,fuel_capacity,cargo))
    
    elif choice ==3:
        print("add motorbike")
        reg =input("enter the reg number : ")
        brand =input("enter the brand : ")
        fuel_capacity =int(input("enter the fuel capacity : "))
        seat =int(input("enter the seat capacity : "))
        vehicle.append(motorbike(reg,brand,fuel_capacity,seat))
        
    elif  choice ==4 :
        print("==========ALL VEHICLES INFORMAITON ========")
        if not vehicle:
            print("no vehicles")
        else :
            for i in vehicle :
                i.show()
                print(f"fuel efficiency: {i.calculate_fuel_efficiency()}")
                
    elif choice ==5:
        print("exit")
        break
    
    else :
        print("invalid choice")  
