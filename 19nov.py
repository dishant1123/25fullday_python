#abtraction  : 
"""
1. class ==> ABC  ==>abstrct base class  ==> from abc import ABC  

2. method /  function  ==> @abtractmethod 

class ==> abstract class  ==> no  object. 
method / function ==> no define in base class .

"""
"""from abc import ABC,abstractmethod

class vehicle(ABC):
    def __init__(self,name,model):
        self.name =name 
        self.model =model
    
    @abstractmethod
    def speed(self):
        pass 
    
class car(vehicle):
    def __init__(self, name, model,seat):
        super().__init__(name, model)  
        self.seat = seat
    
    def speed(self):
        print(f"car speed:200km/h")

class truck(vehicle):
    def __init__(self, name, model,cargo):
        super().__init__(name, model)
        self.cargo=cargo 
    
    def speed(self):
        print(f"truck speed:150km/h")
        
c=car("ford","mustang",4)
t=truck("ashok","a123",1500)

c.speed()
t.speed()

"""
"""
Problem Statement:
A company manages different types of vehicles for its delivery services — such as Cars, Trucks, and Motorbikes. 
Each vehicle has common features but also unique characteristics.

You are required to write a menu-driven Python program that uses:
- Abstraction to define a blueprint for all vehicles.
- Inheritance so that each type of vehicle inherits from a common parent.
- Encapsulation to protect sensitive attributes (e.g., vehicle's registration number).
- Polymorphism so that different vehicles implement their own calculate_fuel_efficiency() method.

Requirements:

1. Abstract Class Vehicle
   - Attributes:
     - _registration_number (private)
     - brand
     - fuel capacity
   - Methods:
     - Constructor to initialize attributes.
     - Getter and Setter for _registration_number.
     - Abstract method calculate_fuel_efficiency().
     - Normal method display_info() to print details.

2. Child Classes
   - Car
     - Additional attribute: passenger capacity
     - Implement calculate_fuel_efficiency() (formula: fuel capacity × 15 km/l).
   - Truck
     - Additional attribute: load_capacity (in tons)
     - Implement calculate_fuel_efficiency() (formula: fuel_capacity × 8 km/l).
   - Motorbike
     - Additional attribute: engine_cc
     - Implement calculate_fuel_efficiency() (formula: fuel_capacity × 35 km/l).

3. Menu Options
   - 1 → Add a new Car
   - 2 → Add a new Truck
   - 3 → Add a new Motorbike
   - 4 → Display all vehicles and their fuel efficiency (Polymorphism in action)
   - 5 → Exit

4. Encapsulation Requirement
   - _registration_number must be private and accessed only through getter/setter.

"""