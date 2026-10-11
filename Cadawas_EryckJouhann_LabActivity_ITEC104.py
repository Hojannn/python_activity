#for clear function, for cleaner outputs in terminal
import os
def clear():
    os.system("cls" if os.name == "nt" else "clear")

#node class to create a node for the tree
class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None
        self.right = None
        
root = Node("College")
deptA = Node("Department A")
deptB = Node("Department B")
prog1 = Node("Program 1")
prog2 = Node("Program 2")
prog3 = Node("Program 3")
prog4 = Node("Program 4")

#tree class to create a tree and perform operations on it
class Tree:
    def __init__(self):
        self.root = root
    #creates the tree structure and connects the nodes together
    def create_tree(self):
        
        self.root.left = deptA
        self.root.right = deptB

        deptA.left = prog1
        deptA.right = prog2

        deptB.left = prog3
        deptB.right = prog4
    
    #displays the complete tree structure in a visual format
    def display_tree(self,):
        print("         COMPLETE TREE")
        print("-----------------------------------")
        print(f"""
        {self.root.data}
        ├── {self.root.left.data}
        │   ├── {self.root.left.left.data}
        │   └── {self.root.left.right.data}
        └── {self.root.right.data}
            ├── {self.root.right.left.data}
            └── {self.root.right.right.data}
              """)
        print("-----------------------------------")
    
    #displays the root
    def display_root(self):
        print(f"Root: {self.root.data}")
    
    #displays the leag of th trre
    def display_leaf(self, node):
        if node is None:
            return
        
        if node.left is None and node.right is None:
            print(node.data)
            
        self.display_leaf(node.left)
        self.display_leaf(node.right)
    
    #performs the preorder traversal of the tree and prints the order 
    def preOrder(self, node):
        if node is None:
            return
        print(node.data)
        self.preOrder(node.left)
        self.preOrder(node.right)
        
    #performs the inorder traversal of the tree and prints the order
    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node.data)
        self.inOrder(node.right)
    
    #performs the postorder traversal of the tree and prints the order
    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.data)
        
        
tree = Tree()
tree.create_tree()

#menu to display user options and perfiorm the chosen operatons
def menu():
    while True:
        print("========================")
        print("ORGANIZATION TREE SYSTEM")
        print("========================")
        print("1. Display Tree")
        print("2. Display Root")
        print("3. Display Leaf Nodes")
        print("4. Preorder Traversal")
        print("5. Inorder Traversal")
        print("6. Postorder Traversal")
        print("7. Exit")
        
        try: 
            choice = int(input("Enter your choice (1-7): "))
        except ValueError:
            clear()
            print("Error! Your choice must be numbers only (1-7).")
            continue
            
        if choice == 7:
            clear()
            print("Exiting the program.. Bye bro.")
            break
        
        elif choice == 1:
            clear()
            tree.display_tree()
            
        elif choice == 2:
            clear()
            tree.display_root()
        
        elif choice == 3:
            clear()
            print("Leaf Nodes: ")
            tree.display_leaf(tree.root)
        
        elif choice == 4:
            clear()
            print("Preorder Traversal: ")
            tree.preOrder(tree.root)
            
        elif choice == 5:
            clear()
            print("Inorder Traversal: ")
            tree.inOrder(tree.root)
            
        elif choice  == 6:
            clear()
            print("Postorder Traversal: ")
            tree.postOrder(tree.root)
        else:
            clear()
            print("Invalid Choice! Please choose from no.1-7")
            continue
            


if __name__ == "__main__":
    menu()
    
#pogi ako
