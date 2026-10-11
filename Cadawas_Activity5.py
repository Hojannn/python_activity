from abc import ABC, abstractmethod
import os


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

class LibraryItem(ABC):
    def __init__(self, item_id, title, author):
        self.__item_id = item_id
        self.__title = title
        self.__author = author
        self.__available = True

    @property
    def item_id(self):
        return self.__item_id

    @item_id.setter
    def item_id(self, value):
        if value <= 0:
            raise ValueError("Item ID must be positive.")
        self.__item_id = value

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise TypeError("Title must be a string.")
        self.__title = value

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, value):
        if not isinstance(value, str):
            raise TypeError("Author must be a string.")
        self.__author = value

    @property
    def available(self):
        return self.__available

    @available.setter
    def available(self, value):
        self.__available = value

    @abstractmethod
    def display_information(self):
        pass

class Borrow(ABC):
    @abstractmethod
    def borrow(self):
        pass

    @abstractmethod
    def return_item(self):
        pass

class Book(LibraryItem, Borrow):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title, author)

    def display_information(self):
        return f"Type: Book\nID: {self.item_id}\nTitle: {self.title}\nAuthor: {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_item(self):
        if not self.available:
            self.available = True
            return True
        return False

class Magazine(LibraryItem, Borrow):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title, author)

    def display_information(self):
        return f"Type: Magazine\nID: {self.item_id}\nTitle: {self.title}\nAuthor: {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_item(self):
        if not self.available:
            self.available = True
            return True
        return False

class Thesis(LibraryItem, Borrow):
    def __init__(self, item_id, title, author):
        super().__init__(item_id, title, author)

    def display_information(self):
        return f"Type: Thesis\nID: {self.item_id}\nTitle: {self.title}\nAuthor: {self.author}"

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_item(self):
        if not self.available:
            self.available = True
            return True
        return False

class Member:
    def __init__(self, member_id, name, email):
        self._member_id = member_id
        self._name = name
        self._email = email
        self._borrowed_items = []

    @property
    def member_id(self):
        return self._member_id

    @property
    def name(self):
        return self._name

    @property
    def email(self):
        return self._email

    @property
    def borrowed_items(self):
        return self._borrowed_items

class Library:
    def __init__(self):
        self.items = []
        self.members = []

    def addBook(self):
        item_id = int(input("Enter Item ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        book = Book(item_id, title, author)
        self.items.append(book)

        print("Book added successfully!")

    def addMagazine(self):
        item_id = int(input("Enter Item ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        magazine = Magazine(item_id, title, author)
        self.items.append(magazine)

        print("Magazine added successfully!")

    def addThesis(self):
        item_id = int(input("Enter Item ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")

        thesis = Thesis(item_id, title, author)
        self.items.append(thesis)

        print("Thesis added successfully!")

    def display_all_items(self):
        clear()

        if not self.items:
            print("The library is empty for now.")
            return

        for item in self.items:
            print(item.display_information())

            if item.available:
                print("Status: Available")
            else:
                print("Status: Borrowed")

            print("-------------------------")

    def search_item(self):
        while True:
            try:
                src = int(input("Enter Item ID: "))
            except ValueError:
                print("The Item ID should only be a number.")
                continue

            for item in self.items:
                if item.item_id == src:
                    return item

            print("Item not found.")
            return None

    def create_member(self):
        clear()

        while True:
            try:
                member_id = int(input("Enter Member ID: "))
                name = input("Enter Name: ")
                email = input("Enter Email: ")
            except ValueError:
                print("Member ID must be a number.")
                continue

            member = Member(member_id, name, email)
            self.members.append(member)

            break

        print("You are now a member in the Library!")

    def borrow_item(self):
        clear()

        try:
            memId = int(input("Enter Member ID: "))
            itemId = int(input("Enter Item ID: "))
        except ValueError:
            print("Both Member ID and Item ID should be numbers.")
            return

        member = None
        item = None

        for mem in self.members:
            if mem.member_id == memId:
                member = mem
                break

        for i in self.items:
            if i.item_id == itemId:
                item = i
                break

        if member is None:
            print("Member not found.")
            return

        if item is None:
            print("Item not found.")
            return

        if item.borrow():
            member.borrowed_items.append(item)
            print("Item borrowed successfully!")
        else:
            print("Item is currently unavailable.")

    def return_item(self):
        clear()

        try:
            memId = int(input("Enter Member ID: "))
            itemId = int(input("Enter Item ID: "))
        except ValueError:
            print("Both Member ID and Item ID should be numbers.")
            return

        member = None
        item = None

        for mem in self.members:
            if mem.member_id == memId:
                member = mem
                break

        for i in self.items:
            if i.item_id == itemId:
                item = i
                break

        if member is None:
            print("Member not found.")
            return

        if item is None:
            print("Item not found.")
            return

        if item in member.borrowed_items:
            item.return_item()
            member.borrowed_items.remove(item)
            print("Item returned successfully!")
        else:
            print("You did not borrow this item.")

    def display_member(self):
        clear()

        if not self.members:
            print("No members found.")
            return

        print("Library Members")
        print("-------------------------")

        for member in self.members:
            print(f"Member ID: {member.member_id}")
            print(f"Name: {member.name}")
            print(f"Email: {member.email}")

            print("Borrowed Items:")

            if not member.borrowed_items:
                print("None")
            else:
                for item in member.borrowed_items:
                    print(f"- {item.title}")

            print("-------------------------")

library = Library()

def menu():
    while True:
        print("=========================")
        print("LIBRARY MANAGEMENT SYSTEM")
        print("=========================")
        print("1. Add Book")
        print("2. Add Magazine")
        print("3. Add Thesis")
        print("4. Display All Library Items")
        print("5. Search Library Item")
        print("6. Create Account")
        print("7. Borrow Item")
        print("8. Return Item")
        print("9. Display Member Information")
        print("10. Exit")

        try:
            choice = int(input("Enter your choice (1-10): "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 10.")
            continue

        if choice == 10:
            print("Exiting the program. Goodbye Bro!")
            break

        elif choice == 1:
            clear()
            library.addBook()

        elif choice == 2:
            clear()
            library.addMagazine()

        elif choice == 3:
            clear()
            library.addThesis()

        elif choice == 4:
            library.display_all_items()

        elif choice == 5:
            clear()
            item = library.search_item()

            if item:
                print("\nItem Found!")
                print(item.display_information())

        elif choice == 6:
            library.create_member()

        elif choice == 7:
            library.borrow_item()

        elif choice == 8:
            library.return_item()

        elif choice == 9:
            library.display_member()

        else:
            print("Invalid choice. Please enter a number between 1 and 10.")

if __name__ == "__main__":
    menu()