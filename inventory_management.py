"""
Dynamic Inventory Management System

This program implements a dynamic inventory management system using Python. 
It allows users to perform the following operations through a command-line interface (CLI):
1. Add a new product to the inventory.
2. Update an existing product's details such as name, category, price, and quantity.
3. Delete a product from the inventory.
4. Retrieve the product with the lowest price from the inventory.
5. Display all products currently in the inventory.
6. Query products within a specified price range using an AVL Tree.

Key Features:
- **Hash Table (Python Dictionary)**: 
  Used to store product information. Each product has a unique product ID, name, category, price, and quantity.
  
- **Min-Heap (using heapq module)**:
  Used to efficiently retrieve the product with the lowest price. 
  Products are stored in the heap based on their prices, allowing O(1) access to the lowest price.

- **AVL Tree**:
  A balanced binary search tree used to index products by their prices.
  It enables efficient queries for retrieving products that fall within a specified price range.

- **CLI Interface**:
  A menu-driven interface that allows users to interact with the system by entering options to perform the desired operations.

- **Error Handling**:
  The program includes robust error handling to:
  1. Validate user inputs (e.g., ensure correct data types).
  2. Handle cases where products with non-existing IDs are updated or deleted.
  3. Prevent duplicate product IDs from being added.
  4. Gracefully manage empty inventories.

- **Dummy Data Initialization**:
  When the program starts, a set of predefined dummy products are added to the inventory for demonstration purposes.

Usage:
- The program starts by initializing some dummy products and then enters a CLI loop where the user can interact with the system by choosing options from the menu.
- Each operation is accompanied by user prompts to input necessary data, and results are displayed back to the user in a clear format.

This implementation provides an efficient, scalable, and interactive solution for managing a dynamic inventory of products.
"""


import heapq  # Import for heap functionality

# Hash Table for Product Storage (using Python dictionary)
inventory = {}

# --- AVL Tree Code (with comments) ---

# Class definition for AVL Tree Nodes
class AVLNode:
    def __init__(self, price, product):
        """
        This class represents an AVL tree node, where each node stores a product's price as the key 
        and a reference to the product as the value.
        """
        self.price = price      # The product price used as the key for this node
        self.product = product  # The actual product stored in the node
        self.left = None        # Left child node (prices lower than this node's price)
        self.right = None       # Right child node (prices higher than this node's price)
        self.height = 1         # Height of the node, used to keep track of balance

# AVL Tree class
class AVLTree:
    def insert(self, root, price, product):
        """
        Inserts a product into the AVL tree, maintaining balance through rotations.
        This function adds the product in the correct location based on its price.
        
        Args:
        root (AVLNode): The root node of the AVL tree.
        price (float): The product price used as the key for insertion.
        product (dict): The product details to store at this node.

        Returns:
        AVLNode: The new root of the balanced tree.
        """
        if not root:  # If the root is None, create a new node
            return AVLNode(price, product)
        elif price < root.price:  # If the new price is less than the current node's price, go left
            root.left = self.insert(root.left, price, product)
        else:  # If the new price is greater than or equal to the current node's price, go right
            root.right = self.insert(root.right, price, product)

        # Update the height of the current node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Check the balance of the current node
        balance = self.get_balance(root)

        # Perform rotations if the tree is unbalanced
        if balance > 1 and price < root.left.price:  # Left-Left case
            return self.rotate_right(root)
        if balance < -1 and price > root.right.price:  # Right-Right case
            return self.rotate_left(root)
        if balance > 1 and price > root.left.price:  # Left-Right case
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and price < root.right.price:  # Right-Left case
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root  # Return the (possibly rotated) root of the subtree

    def get_products_in_range(self, root, low, high, result):
        """
        Finds all products in the AVL tree that fall within a specified price range.
        
        Args:
        root (AVLNode): The root of the current subtree.
        low (float): The lower bound of the price range.
        high (float): The upper bound of the price range.
        result (list): A list to collect products within the specified range.

        Returns:
        None
        """
        if not root:
            return

        # If the current node's price is within the range, add it to the result
        if low <= root.price <= high:
            result.append(root.product)

        # If the current node's price is greater than the lower bound, search the left subtree
        if low < root.price:
            self.get_products_in_range(root.left, low, high, result)

        # If the current node's price is less than the upper bound, search the right subtree
        if high > root.price:
            self.get_products_in_range(root.right, low, high, result)

    # Helper functions for AVL rotations
    def rotate_left(self, z):
        """
        Performs a left rotation on the given node to maintain AVL balance.
        """
        y = z.right  # Set y as z's right child
        T2 = y.left  # Store y's left subtree
        y.left = z  # Perform rotation
        z.right = T2  # Move T2 to z's right child
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y  # Return the new root of this subtree

    def rotate_right(self, z):
        """
        Performs a right rotation on the given node to maintain AVL balance.
        """
        y = z.left  # Set y as z's left child
        T3 = y.right  # Store y's right subtree
        y.right = z  # Perform rotation
        z.left = T3  # Move T3 to z's left child
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # Update heights
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y  # Return the new root of this subtree

    def get_height(self, node):
        """
        Returns the height of the given node, or 0 if the node is None.
        """
        if not node:
            return 0
        return node.height

    def get_balance(self, node):
        """
        Returns the balance factor of the given node.
        Balance factor is defined as the difference between the heights of the left and right subtrees.
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

# Initialize the AVL Tree
avl_tree = AVLTree()
avl_root = None  # Start with an empty AVL tree

# --- Heap and Hash Table Code ---

# Min-Heap to track product prices
price_heap = []

def add_product_to_heap(product_id, price):
    """
    Adds a product's price and its ID to the heap for quick retrieval of the product with the lowest price.
    """
    heapq.heappush(price_heap, (price, product_id))  # Push a tuple of (price, product_id) into the heap

def get_lowest_price_product():
    """
    Retrieves the product with the lowest price from the heap.
    """
    if price_heap:
        lowest_price, product_id = price_heap[0]  # Peek at the product with the lowest price
        return inventory.get(product_id, None)  # Get product details from the inventory using the product_id
    return None

def remove_product_from_heap(product_id, price):
    """
    Removes a product from the heap based on its product_id and price.
    """
    try:
        price_heap.remove((price, product_id))  # Remove the product from the heap
        heapq.heapify(price_heap)  # Reorder the heap
    except ValueError:
        print(f"Product {product_id} with price {price} not found in heap.")

# --- Hash Table and CLI Code ---

def add_product_with_heap(product_id, name, category, price, quantity):
    """
    Adds a product to the inventory and inserts the price into the min-heap and AVL tree.
    Also checks if the product id already exist. If it does, it won't add.
    """
    if product_id in inventory:
      print(f"Error: Product with ID {product_id} already exists.")
      return
    product = {'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity}
    inventory[product_id] = product  # Add product to the inventory (hash table)
    add_product_to_heap(product_id, price)  # Add product to the heap (min-heap for price tracking)

def update_product_with_heap(product_id, name=None, category=None, price=None, quantity=None):
    """
    Updates a product in the inventory and manages the heap and AVL tree for price changes.
    If the product_id does not exist, it returns an error.
    """
    if product_id not in inventory:
        print(f"Error: Product with ID {product_id} does not exist.")
        return

    current_price = inventory[product_id]['price']
    remove_product_from_heap(product_id, current_price)
    if name:
        inventory[product_id]['name'] = name
    if category:
        inventory[product_id]['category'] = category
    if price is not None:
        inventory[product_id]['price'] = price
    if quantity is not None:
        inventory[product_id]['quantity'] = quantity
    if price is not None:
        add_product_to_heap(product_id, price)
    print(f"Product {product_id} updated successfully!")

def delete_product_with_heap(product_id):
    """
    Deletes a product from the inventory and removes it from both the heap and AVL tree.
    """
    if product_id in inventory:
        current_price = inventory[product_id]['price']  # Get the product's current price
        remove_product_from_heap(product_id, current_price)  # Remove it from the heap
        del inventory[product_id]  # Remove the product from the inventory

# CLI interface
def display_menu():
    """
    Displays the available menu options for interacting with the system.
    """
    print("\n--- Dynamic Inventory Management System ---")
    print("1. Add a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Get the product with the lowest price")
    print("5. Display all products")
    print("6. Query products by price range (AVL Tree)")
    print("7. Exit")
    
def initialize_dummy_products():
    """
    Initializes the inventory with some dummy products for testing and demonstration purposes.
    Adds the products to the hash table, heap, and AVL tree.
    """
    global avl_root  # To modify the global avl_root

    # Define some dummy products
    dummy_products = [
        (101, "Laptop", "Electronics", 1200.99, 10),
        (102, "Smartphone", "Electronics", 799.99, 25),
        (103, "Headphones", "Accessories", 199.99, 50),
        (104, "Monitor", "Electronics", 299.99, 15),
        (105, "Keyboard", "Accessories", 49.99, 100)
    ]

    # Add each dummy product to the inventory, heap, and AVL tree
    for product_id, name, category, price, quantity in dummy_products:
        add_product_with_heap(product_id, name, category, price, quantity)  # Add to hash table and heap
        avl_root = avl_tree.insert(avl_root, price, inventory[product_id])  # Add to AVL tree

    print("Dummy products initialized successfully!")

def run_inventory_management():
    """
    Runs the inventory management system with a command-line interface (CLI).
    """
    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice (1-7): ")  # Get user choice

        if choice == '1':  # Add a new product
            try:
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                add_product_with_heap(product_id, name, category, price, quantity)  # Add product
                global avl_root
                avl_root = avl_tree.insert(avl_root, price, inventory[product_id])  # Add to AVL tree
            except ValueError:
                print("Invalid input! Please enter valid data types.")

        elif choice == '2':  # Update an existing product
            try:
                product_id = int(input("Enter product ID to update: "))
                name = input("Enter new product name (leave blank to skip): ")
                category = input("Enter new product category (leave blank to skip): ")
                price_input = input("Enter new product price (leave blank to skip): ")
                price = float(price_input) if price_input else None
                quantity_input = input("Enter new product quantity (leave blank to skip): ")
                quantity = int(quantity_input) if quantity_input else None
                update_product_with_heap(product_id, name=name, category=category, price=price, quantity=quantity)  # Update product
            except ValueError:
                print("Invalid input! Please enter valid data types.")

        elif choice == '3':  # Delete a product
            try:
                product_id = int(input("Enter product ID to delete: "))
                delete_product_with_heap(product_id)  # Delete product
            except ValueError:
                print("Invalid input! Please enter a valid product ID.")

        elif choice == '4':  # Get the product with the lowest price
            lowest_price_product = get_lowest_price_product()
            if lowest_price_product:
                print(f"Lowest priced product: {lowest_price_product['name']} at ${lowest_price_product['price']}")
            else:
                print("No products available in the inventory.")

        elif choice == '5':  # Display all products
            print("\n--- Current Inventory ---")
            if inventory:
                for product_id, product in inventory.items():
                    print(f"ID: {product_id}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Quantity: {product['quantity']}")
            else:
                print("Inventory is empty!")

        elif choice == '6':  # Query products by price range
            try:
                low_price = float(input("Enter the lower bound of the price range: "))
                high_price = float(input("Enter the upper bound of the price range: "))
                result = []
                avl_tree.get_products_in_range(avl_root, low_price, high_price, result)  # Query AVL tree
                if result:
                    print("\n--- Products in Price Range ---")
                    for product in result:
                        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")
                else:
                    print("No products found in this price range.")
            except ValueError:
                print("Invalid input! Please enter valid price values.")

        elif choice == '7':  # Exit the program
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")
       
if __name__ == "__main__":
	initialize_dummy_products()
	run_inventory_management()
	

