from collections import deque
import os

def clear():
    os.system("cls" if os.name == "nt" else "clear")
class Queue:
    def __init__(self): 
        self.items = deque()

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            removed_request = self.items.popleft()
            print(f"Processed: {removed_request}")
            return removed_request
        else: 
            print("No requests available.")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            return "No requests available."
    
    def is_empty(self):
        return len(self.items) == 0 
    
    def display_request(self):
        if not self.is_empty():
            print("Pending Requests:")
            print("----------------")
            for i, request in enumerate(self.items, 1):
                print(f"{i}. {request}")
        else:
            print("Pending Requests:")
            print("----------------")
            print("None")
    
    def size(self):
        
        print(f"Requests waiting: {len(self.items)}")
        return len(self.items)
    
queue = Queue()
def menu():
    while True:
        print("=========================")
        print("REQUEST PROCESSING SYSTEM")
        print("=========================")
        print("1. Add Request")
        print("2. Process Request")
        print("3. Next Request")
        print("4. View Requests")
        print("5. Queue Size")
        print("6. Exit")

        try: 
            choice = int(input("Enter your choice (1-6): "))
        except ValueError:
            print("Invalid input. Please enter a number from 1-6.")
            continue

        if choice == 6:
            print("Exiting the program. Goodbye Bro!")
            break
        
        elif choice == 1:
            
            while True:
                req = input("Enter Requests (or type 'exit' to go back): ")
                if req.lower() == 'exit':
                    break
                queue.enqueue(req)
            clear()
                    
        elif choice == 2:
            
            queue.dequeue()
            input("\nPress Enter to continue...")
            clear()
            
        elif choice == 3:
            
            print(f"Next request: {queue.peek()}")
            input("\nPress Enter to continue...")
            clear()
            
        elif choice == 4:
            
            queue.display_request()
            input("\nPress Enter to continue...")
            clear()
            
        elif choice == 5:
            queue.size()
            input("\nPress Enter to continue...")
            clear()
        
if __name__ == "__main__":
    menu()