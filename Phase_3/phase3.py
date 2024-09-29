"""
This is the main file of the Dynamic Inventory Management System.
It manages product additions, updates, deletions, and various queries through a Command-Line Interface (CLI).
The system supports operations using a Min-Heap, Hash Table (dictionary), and AVL Tree.

- Inventory is stored in a dictionary.
- AVL Tree is used for querying products by price range.
- A Heap is used to get the lowest-priced product quickly.

The user interacts with the system by selecting options through the CLI.
It also includes initialization of large dummy products with time and memory tracking, along with plotting.
"""

from heap_handler import HeapHandler  # Import heap handler class
from avl_tree import AVLTree  # Import AVL tree class
from utils import time_it, memory_it, plot_execution_times, plot_memory_usage  # Utility functions for timing and memory
import time  # Import time module to track operation time

# Global Hash Table for Product Storage (using Python dictionary)
inventory = {}

# Initialize the AVL Tree and the root node of the AVL tree
avl_tree = AVLTree()
avl_root = None

# CLI interface for the inventory system
def display_menu():
    """
    Displays the available menu options for interacting with the inventory management system.
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
        avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)

    print("Dummy products initialized successfully!")

   
# Global product counter to ensure unique IDs across multiple initializations
product_counter = 1

@time_it("Time taken to initialize products") 
@memory_it("Memory taken to initialize products", collect_data=True)
def initialize_large_dummy_products(num_products):
    """
    Initializes the inventory with a large number of dummy products for stress testing.
    Uses a global counter for unique product IDs to avoid duplicates across multiple runs.
    
    Args:
    num_products (int): The number of products to generate for the test.
    """
    global avl_root, product_counter  # Use the global product counter to assign unique IDs

    for _ in range(num_products):  # Iterate num_products times
        product_id = product_counter  # Use the global counter for unique product ID
        name = f"Product_{product_id}"
        category = "Category_1" if product_id % 2 == 0 else "Category_2"
        price = float(product_id * 10)  # Incremental price for each product
        quantity = product_id % 100 + 1  # Random quantity between 1 and 100

        # Add product to inventory, heap, and AVL tree
        avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)

        # Increment the global counter after each product is added
        product_counter += 1

    print(f"Initialized {num_products} products successfully!")
    

def run_inventory_management():
    """
    Runs the inventory management system with a command-line interface (CLI).
    """
    global avl_root
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
                
                start_time = time.time()  # Start the timer just before the actual operation
                avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)  # Add product and update avl_root
                end_time = time.time()  # End the timer
                print("Product added successfully!")
                print(f"Time taken for Add product operation: {end_time - start_time:.6f} seconds")
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
                
                start_time = time.time()  # Start the timer just before the actual operation
                avl_root = HeapHandler.update_product_with_heap(product_id, name=name, category=category, price=price, quantity=quantity, inventory=inventory, avl_tree=avl_tree, avl_root=avl_root)  # Update product and update avl_root
                end_time = time.time()  # End the timer
                print("Product updated successfully!")
                print(f"Time taken for Update product operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter valid data types.")

        elif choice == '3':  # Delete a product
            try:
                product_id = int(input("Enter product ID to delete: "))
                
                start_time = time.time()  # Start the timer just before the actual operation
                avl_root = HeapHandler.delete_product_with_heap(product_id, inventory, avl_tree, avl_root)  # Delete product
                end_time = time.time()  # End the timer
                print("Product deleted successfully!")
                print(f"Time taken for Delete product operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter a valid product ID.")

        elif choice == '4':  # Get the product with the lowest price
            start_time = time.time()  # Start the timer just before the actual operation
            lowest_price_product = HeapHandler.get_lowest_price_product(inventory)
            end_time = time.time()  # End the timer
            if lowest_price_product:
                print(f"Lowest priced product: {lowest_price_product['name']} at ${lowest_price_product['price']}")
            else:
                print("No products available in the inventory.")
            print(f"Time taken for Get lowest price operation: {end_time - start_time:.6f} seconds")

        elif choice == '5':  # Display all products in the inventory
            start_time = time.time()  # Start the timer just before the actual operation
            print("\n--- Current Inventory ---")
            if inventory:  # Check if inventory is not empty
                for product_id, product in inventory.items():
                    print(f"ID: {product_id}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Quantity: {product['quantity']}")
            else:
                print("Inventory is empty!")
            end_time = time.time()  # End the timer
            print(f"Time taken for Display products operation: {end_time - start_time:.6f} seconds")

        elif choice == '6':  # Query products by price range using AVL Tree
            try:
                low_price = float(input("Enter the lower bound of the price range: "))
                high_price = float(input("Enter the upper bound of the price range: "))
                
                start_time = time.time()  # Start the timer just before the actual query operation
                result = []
                avl_tree.get_products_in_range(avl_root, low_price, high_price, result)  # Query AVL tree
                end_time = time.time()  # End the timer
                
                if result:  # Check if products were found in the range
                    print("\n--- Products in Price Range ---")
                    for product in result:
                        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")
                else:
                    print("No products found in this price range.")
                
                print(f"Time taken for Query products by price range operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter valid price values.")

        elif choice == '7':  # Exit the program
            print("Exiting the system. Goodbye!")
            break  # Exit the loop

        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    # Step 1: Initialize some small dummy products for basic setup (no timing)
    # initialize_dummy_products()

    # Step 2: Define input sizes for stress testing
    input_sizes = [10]

    # Step 3: Initialize lists to store execution times and memory usages
    execution_times = []
    memory_usages = []

    # Step 4: Measure both time and memory usage for each input size
    for size in input_sizes:
        # Time measurement
        start_time = time.time()

        # Memory measurement using the `memory_it` decorator
        memory_used = initialize_large_dummy_products(size)  # Collect memory usage via the modified decorator

        end_time = time.time()
        time_taken = end_time - start_time

        # Append both time and memory usage results
        execution_times.append(time_taken)
        memory_usages.append(memory_used)

        # Print results to the console
        print(f"Input size {size}: Time taken = {time_taken:.6f} seconds, Memory used = {memory_used:.6f} MiB")

    # Step 5: Plot and save the graph for execution times
    plot_execution_times(input_sizes, execution_times, "initialize_large_dummy_products")

    # Step 6: Plot and save the graph for memory usage
    plot_memory_usage(input_sizes, memory_usages, "initialize_large_dummy_products")

    # Step 7: Start the inventory management system (CLI)
    run_inventory_management()

