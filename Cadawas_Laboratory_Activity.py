class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        if not self.is_empty():
            removed_history = self.items.pop()
            print(f"\nRemoved: {removed_history}")
            return removed_history
        else:
            print("\nNo previous page available.\n")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return "\nNo current page available.\n"
        
    def view_history(self):
        if not self.is_empty():
            print("________________")
            print("Recent History:")
            print("________________")
            for i in range(len(self.items)-1, -1, -1):
                print(f"{self.items[i]}")
            print("________________\n")
        else:
            print("\nNo History Available.\n")
        
    def is_empty(self):
        return len(self.items) == 0

stack = Stack()

def menu():
    while True:
        print("==============================")
        print("       BROWSER HISTORY        ")
        print("==============================")
        print("1. Visit Page")
        print("2. Go Back")
        print("3. Current Page")
        print("4. View History")
        print("5. Exit")
        print("==============================")

        try:
            choice = int(input("Enter your choice (1-5): "))
        except ValueError:
            print("\nInvalid input. Please enter a number between 1 and 5.\n")
            continue
        
        if choice == 5:
            print("Exiting...")
            break
        
        elif choice == 1:
            while True:
                page = input("Enter the page URL (or type 'exit' to go back): ")
                if page.lower() == 'exit':
                    break
                else:
                    stack.push(page)
                    print(f"Visited: {page}")
                    
        elif choice == 2:
            stack.pop()
            
        elif choice == 3:
            page = stack.peek()
            print("\nChecking current page...")
            if page:
                print(f"Current page: {page}\n")
            else:
                print("No current page available.\n")
            
        elif choice == 4:
            stack.view_history()

if __name__ == "__main__":
    menu()


