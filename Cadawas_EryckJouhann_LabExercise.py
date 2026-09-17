#4

class FoodItem:
    def __init__(self, item_id, name, price):
        self.item_id = item_id
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.items = []
        
    def add_item(self, item):
            self.items.append(item)
            return "Order added successfully"
    
    def remove_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                self.items.remove(item)
                return "Item has been removed"
        
        return "Item not found"
    
    def calculate_total(self):
        total = 0

        for item in self.items:
            total += item.price
        
        if total > 500:
            total *= 0.10
            
        return total
    
    def display_order(self):
        print(f"ORDER #{self.order_number}")
        print("========================")
        for item in self.items:
            print(f"{item.name} ₱{item.price}")
        print("------------------------")
        print(f"TOTAL ₱: {self.calculate_total()}")
           
           
order = Order(1001)

# burger = FoodItem(1, "burger", 120)
# fries = FoodItem(2, "fries", 80)
# softDrink = FoodItem(3, "Soft Drink", 50)

# order = Order(1001)
# order.add_item(burger)
# order.add_item(fries)
# order.add_item(softDrink)
# order.display_order()

#5
vehicles = []
class Vehicle:
    def __init__(self, plate_number, vehicle_type, hours_parked):
        self.plate_number = plate_number
        self.vehicle_type = vehicle_type
        self.hours_parked = hours_parked

    def calculate_fee(self):
        if self.vehicle_type == "motorcycle":
            first_hour = 20
            add_hour = 10

        elif self.vehicle_type == "car":
            first_hour = 40
            add_hour = 20

        elif self.vehicle_type == "van":
            first_hour = 50
            add_hour = 25
        else:
            return 0

        if self.hours_parked <= 1:
            return first_hour
        else:
            extra_hours = self.hours_parked - 1
            return first_hour + (extra_hours * add_hour)

    def display_vehicle(self):
        total_fee = self.calculate_fee()
        print("PARKING RECEIPT")
        print("================")
        print(f"Plate Number: {self.plate_number}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Parking Fee: {str(total_fee)}")

class SmartDevice:
    def __init__(self, device_name, device_type, status):
        self.device_name = device_name
        self.device_type = device_type
        self.status = status

    def turn_on(self):
        self.status = "ON"

    def turn_off(self):
        self.status = "OFF"

    def display_status(self):
        print(f"{self.device_name} : {self.status}")


class SmartLight(SmartDevice):
    pass


class SmartFan(SmartDevice):
    pass


class SmartAircon(SmartDevice):
    def __init__(self, device_name, device_type, status, temperature):
        super().__init__(device_name, device_type, status)
        self.temperature = temperature

    def set_temperature(self, temperature):
        self.temperature = temperature

    def increase_temperature(self):
        self.temperature += 1

    def decrease_temperature(self):
        self.temperature -= 1

    def display_status(self):
        print(f"{self.device_name} : {self.status} ({self.temperature}°C)")

def menu1():
    while True:
        print("SYSTEM 4: Food Ordering System")
        print("==============================")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Calculate Total")
        print("4. Display Order")
        print("5. Exit")
    
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue 
            
        if choice == 1:
            while True:
                try:
                    item_id = int(input("Enter item ID: "))
                except ValueError:
                    print("Invalid input. Please enter a valid item ID.")
                    continue
               
                name = input("Enter item name: ")
                
                try:
                    price = float(input("Enter item price: "))
                except ValueError:
                    print("Invalid input. Please enter a valid item price.")
                    continue

                item = FoodItem(item_id, name, price)
                order.add_item(item)
                print("Item added successfully.")
                break
        
        elif choice == 2:
            try:
                item_id = int(input("Enter item ID to remove: "))
            except ValueError:
                print("Invalid input. Please enter a valid item ID.")
                continue
            result = order.remove_item(item_id)
            print(result)
        
        elif choice == 3:
            total = order.calculate_total()
            print(f"Total amount: ₱{total}")
        
        elif choice == 4:
            order.display_order()
            
        
        elif choice == 5:
            print("Exiting Food Ordering System..")
            break
        else:
            print("Invalid choice, Choose from options 1-5")
            continue

def menu2():
    # This list represents the parking lot
    vehicles = []

    while True:
        print("SYSTEM 5: Parking Fee Calculator")
        print("================================")
        print("1. Add Vehicle / Calculate Parking Fee")
        print("2. Display All Parking Receipts")
        print("3. Calculate Total Collection")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            plate_number = input("Enter plate number: ")
            vehicle_type = input(
                "Enter vehicle type (motorcycle/car/van): "
            ).lower()

            try:
                hours_parked = float(input("Enter hours parked: "))
            except ValueError:
                print("Invalid input. Please enter a valid number of hours.")
                continue

            vehicle = Vehicle(
                plate_number,
                vehicle_type,
                hours_parked
            )

            vehicles.append(vehicle)

            fee = vehicle.calculate_fee()

            print(f"\nParking Fee: ₱{fee}")
            print("Vehicle added to the parking lot.\n")

        elif choice == 2:
            if len(vehicles) == 0:
                print("\nNo vehicles currently parked.\n")
            else:
                print("\nALL PARKING RECEIPTS")
                print("====================")

                for vehicle in vehicles:
                    vehicle.display_vehicle()

        elif choice == 3:
            total_collection = 0

            for vehicle in vehicles:
                total_collection += vehicle.calculate_fee()

            print(f"\nTotal Collection: ₱{total_collection}\n")

        elif choice == 4:
            print("Exiting parking fee system...")
            break

        else:
            print("Invalid choice. Please select 1-4.\n")
            

def menu3():
    light = SmartLight("Living Room Light", "Light", "ON")
    fan = SmartFan("Bedroom Fan", "Fan", "OFF")
    aircon = SmartAircon("Air Conditioner", "Aircon", "ON", 24)

    while True:
        print("\nSMART HOME")
        print("==========")
        print("1. Display Devices")
        print("2. Turn Device ON")
        print("3. Turn Device OFF")
        print("4. Set Aircon Temperature")
        print("5. Increase Aircon Temperature")
        print("6. Decrease Aircon Temperature")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            print("\nSMART HOME")
            print("==========")
            light.display_status()
            fan.display_status()
            aircon.display_status()

        elif choice == 2:
            print("\n1. Living Room Light")
            print("2. Bedroom Fan")
            print("3. Air Conditioner")

            device = input("Turn ON which device? ")

            if device == "1":
                light.turn_on()
            elif device == "2":
                fan.turn_on()
            elif device == "3":
                aircon.turn_on()
            else:
                print("Invalid device.")

        elif choice == 3:
            print("\n1. Living Room Light")
            print("2. Bedroom Fan")
            print("3. Air Conditioner")

            device = input("Turn OFF which device? ")

            if device == "1":
                light.turn_off()
            elif device == "2":
                fan.turn_off()
            elif device == "3":
                aircon.turn_off()
            else:
                print("Invalid device.")

        elif choice == 4:
            try:
                temperature = float(input("Enter temperature: "))
                aircon.set_temperature(temperature)
                print(f"Temperature set to {aircon.temperature}°C")
            except ValueError:
                print("Invalid temperature.")

        elif choice == 5:
            aircon.increase_temperature()
            print(f"Temperature: {aircon.temperature}°C")

        elif choice == 6:
            aircon.decrease_temperature()
            print(f"Temperature: {aircon.temperature}°C")

        elif choice == 7:
            print("Exiting Smart Home...")
            break

        else:
            print("Invalid choice.")
            
def mainMenu():
    while True:
        print("LABORATORY ACTIVITY")
        print("-------------------")
        print("Choose from the Following Systems:")
        print("1. Food Ordering")
        print("2. Parking Fee")
        print("3. Smart Home Device")
        print("4. Exit")
    
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input, choice must be a number.")
        
        if choice == 4:
            print("Exiting the system. Bye bro")
            break
        elif choice == 1:
            menu1()
        elif choice == 2:
            menu2()
        elif choice == 3:
            menu3()
        else:
            print("Invalid Input, please choose from 1-4")
            
if __name__ == "__main__":
    mainMenu()