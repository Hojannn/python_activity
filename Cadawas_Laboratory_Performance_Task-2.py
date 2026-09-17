
products = ["Keyboard", "Mouse", "Monitor", "Printer", "Webcam"]

#main menu/display method
def main():

    while True:
        print("\n===================================")
        print("PRODUCT INVENTORY MANAGEMENT SYSTEM")
        print("===================================")
        print("1. Add Product")
        print("2. Insert Product")
        print("3. Update Product")
        print("4. Remove Product")
        print("5. Search Product")
        print("6. Display Products")
        print("7. Count Products")
        print("8. Show First and Last Product")
        print("9. Exit")
        print("===================================")

        try:
            choice = int(input("Enter Choice: "))

        except ValueError:
            print("Invalid choice. Please enter a number from 1-9.")
            continue

        if choice == 1:
            addProd()

        elif choice == 2:
            insertProd()

        elif choice == 3:
            updateProd()

        elif choice == 4:
            removeProd()

        elif choice == 5:
            searchProd()

        elif choice == 6:
            displayProd()

        elif choice == 7:
            countProd()

        elif choice == 8:
            showfnlProd()

        elif choice == 9:
            print("Goodbye Bro.")
            break

        else:
            print("Invalid choice. Please enter a number from 1-9.")

#add product function
def addProd():
    product = input("Enter product name: ").strip()

    if product == "":
        print("Product name cannot be empty.")
        return

    products.append(product)
    print(f"{product} has been added successfully.")

#insert product function
def insertProd():
    if len(products) == 0:
        print("The product list is empty.")
        return

    try:
        index = int(input("Enter index: "))

        if index < 0 or index > len(products):
            print("Invalid index.")
            return

        product = input("Enter product name: ").strip()

        if product == "":
            print("Product name cannot be empty.")
            return

        products.insert(index, product)
        print(f"{product} has been inserted at index {index}.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the index.")


#update product function
def updateProd():
    if len(products) == 0:
        print("The product list is empty.")
        return

    try:
        index = int(input("Enter index of product to update: "))

        if index < 0 or index >= len(products):
            print("Invalid index.")
            return

        product = input("Enter new product name: ").strip()

        if product == "":
            print("Product name cannot be empty.")
            return

        old_product = products[index]
        products[index] = product

        print(f"{old_product} has been updated to {product}.")

    except ValueError:
        print("Invalid input. Please enter a valid number for the index.")


#remove product function
def removeProd():
    if len(products) == 0:
        print("The product list is empty.")
        return

    print("Remove by:")
    print("1. Product Name")
    print("2. Index")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        product = input("Enter product name to remove: ").strip()

        if product == "":
            print("Product name cannot be empty.")
            return

        # Search without worrying about uppercase/lowercase
        found = False

        for i in range(len(products)):
            if products[i].lower() == product.lower():
                removed = products.pop(i)
                print(f"{removed} has been removed.")
                found = True
                break

        if not found:
            print("Product not found.")

    elif choice == "2":
        try:
            index = int(input("Enter index of product to remove: "))

            if index < 0 or index >= len(products):
                print("Invalid index.")
                return

            removed = products.pop(index)
            print(f"{removed} has been removed.")

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    else:
        print("Invalid choice.")


#search product function
def searchProd():
    product = input("Enter product to search: ").strip()

    if product == "":
        print("Product name cannot be empty.")
        return

    found = False

    for i in range(len(products)):
        if products[i].lower() == product.lower():
            print(f"{product} found at index {i}.")
            found = True
            break

    if not found:
        print("Product not found.")


#display products function
def displayProd():
    if len(products) == 0:
        print("The product list is empty.")
        return

    print("\n========== PRODUCT LIST ==========")

    # Traversal
    for i in range(len(products)):
        print(f"Index {i}: {products[i]}")

    print("==================================")


#count products function
def countProd():
    print(f"Total number of products: {len(products)}")


#show first and last product function
def showfnlProd():
    if len(products) == 0:
        print("The product list is empty.")
        return

    print(f"First product: {products[0]}")
    print(f"Last product: {products[-1]}")


#call menu/ main method
if __name__ == "__main__":
    main()

