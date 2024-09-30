
"""
This is the main file for the Dynamic Inventory Management System.

It provides a command-line interface (CLI) to manage an inventory of products, 
allowing users to perform various operations such as adding, updating, deleting, 
and querying products. The system supports querying by both price range (using 
an AVL Tree) and multiple parameters (using a Range Tree).

The system tracks product prices using both a Min-Heap and a Double-Ended 
Priority Queue for efficient retrieval of the lowest and highest-priced products.

Key features of this system:
1. Add, update, delete, and display products in the inventory.
2. Query products by price range using an AVL Tree.
3. Query products by multiple parameters (price, category, quantity) using a Range Tree.
4. Get the lowest-priced product via both Min-Heap and Double-Ended Priority Queue.
5. Get the highest-priced product via Double-Ended Priority Queue.
6. Time and memory tracking for large dummy product initialization.
7. Execution time tracking for most operations, including queries.

The system also includes functions to initialize large dummy products for stress testing 
and plot execution time and memory usage for these operations.
"""

import time  # Import time module for timing operations
from heap_handler import HeapHandler  # Import heap handler class
from avl_tree import AVLTree  # Import AVL tree class
from range_tree import RangeTree  # Import range tree class
from double_ended_priority_queue import DoubleEndedPriorityQueue  # Import double-ended priority queue
from utils import time_it, memory_it, plot_execution_times, plot_memory_usage  # Utility functions for timing and memory
import sys

# Increase the recursion limit to handle deep recursive calls when initializing large data
sys.setrecursionlimit(500000)

# Global Hash Table for Product Storage (using Python dictionary)
inventory = {}

# Initialize the AVL Tree and the root node of the AVL tree
avl_tree = AVLTree()
avl_root = None

# Initialize Range Tree
range_tree = RangeTree()

# Initialize Double-Ended Priority Queue
double_ended_pq = DoubleEndedPriorityQueue()

# Define a global product counter for large dummy product initialization
product_counter = 1

# CLI interface for the inventory system
def display_menu():
    """
    Displays the available menu options for interacting with the inventory management system.
    """
    print("\n--- Dynamic Inventory Management System ---")
    print("1. Add a new product")
    print("2. Update an existing product")
    print("3. Delete a product")
    print("4. Get the product with the lowest price (Heap)")
    print("5. Get the product with the lowest price (Double-Ended Priority Queue)")
    print("6. Get the product with the highest price (Double-Ended Priority Queue)")
    print("7. Query products by price range (AVL Tree)")
    print("8. Query products by multiple parameters (Range Tree)")
    print("9. Display all products")
    print("10. Exit")


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
        product = {'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity}
        avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)
        range_tree.root = range_tree.insert(range_tree.root, product, 'price')  # Insert product into Range Tree
        double_ended_pq.add_product(product)  # Add product to Double-Ended Priority Queue

    print("Dummy products initialized successfully!")


def run_inventory_management():
    """
    Runs the inventory management system with a command-line interface (CLI).
    """
    global avl_root
    while True:
        display_menu()  # Show the menu options
        choice = input("Enter your choice (1-10): ")  # Get user choice

        if choice == '1':  # Add a new product
            try:
                product_id = int(input("Enter product ID: "))
                name = input("Enter product name: ")
                category = input("Enter product category: ")
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))

                # Create a product dictionary
                product = {'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity}

                start_time = time.time()  # Start the timer just before the actual operation
                avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)  # Add product to AVL tree
                range_tree.root = range_tree.insert(range_tree.root, product, 'price')  # Insert into Range Tree
                double_ended_pq.add_product(product)  # Add product to Double-Ended Priority Queue
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
                avl_root = HeapHandler.update_product_with_heap(product_id, name=name, category=category, price=price, quantity=quantity, inventory=inventory, avl_tree=avl_tree, avl_root=avl_root)  # Update product in AVL Tree
                # Update product in Range Tree and Double-Ended Priority Queue as needed
                end_time = time.time()  # End the timer

                print("Product updated successfully!")
                print(f"Time taken for Update product operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter valid data types.")

        elif choice == '3':  # Delete a product
            try:
                product_id = int(input("Enter product ID to delete: "))

                start_time = time.time()  # Start the timer just before the actual operation
                product = inventory.get(product_id)  # Get the product from inventory
                if product:
                    avl_root = HeapHandler.delete_product_with_heap(product_id, inventory, avl_tree, avl_root)  # Delete product from AVL Tree
                    double_ended_pq.remove_product(product)  # Remove from double-ended priority queue
                    # No need to remove from range tree since we're not maintaining deletion support in the range tree
                else:
                    print("Product not found.")
                end_time = time.time()  # End the timer

                print("Product deleted successfully!")
                print(f"Time taken for Delete product operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter a valid product ID.")

        elif choice == '4':  # Get the product with the lowest price (Heap)
            start_time = time.time()  # Start the timer for heap-based query
            lowest_price_product = HeapHandler.get_lowest_price_product(inventory)  # Get product from heap
            end_time = time.time()  # End the timer
            time_taken = end_time - start_time

            if lowest_price_product:
                print(f"Lowest priced product (Heap): {lowest_price_product['name']} at ${lowest_price_product['price']}")
            else:
                print("No products available in the inventory.")
            print(f"Time taken for Get lowest price operation (Heap): {time_taken:.6f} seconds")

        elif choice == '5':  # Get the product with the lowest price (Double-Ended Priority Queue)
            start_time = time.time()  # Start the timer for double-ended priority queue-based query
            lowest_price_product = double_ended_pq.get_lowest_price_product()  # Get product from double-ended priority queue
            end_time = time.time()  # End the timer
            time_taken = end_time - start_time

            if lowest_price_product:
                print(f"Lowest priced product (Double-Ended Priority Queue): {lowest_price_product['name']} at ${lowest_price_product['price']}")
            else:
                print("No products available in the inventory.")
            print(f"Time taken for Get lowest price operation (Double-Ended Priority Queue): {time_taken:.6f} seconds")

        elif choice == '6':  # Get the product with the highest price (Double-Ended Priority Queue)
            start_time = time.time()  # Start the timer for double-ended priority queue-based query
            highest_price_product = double_ended_pq.get_highest_price_product()  # Get product from double-ended priority queue
            end_time = time.time()  # End the timer
            time_taken = end_time - start_time

            if highest_price_product:
                print(f"Highest priced product: {highest_price_product['name']} at ${highest_price_product['price']}")
            else:
                print("No products available in the inventory.")
            print(f"Time taken for Get highest price operation: {time_taken:.6f} seconds")

        elif choice == '7':  # Query products by price range (AVL Tree)
            try:
                low_price = float(input("Enter the lower bound of the price range: "))
                high_price = float(input("Enter the upper bound of the price range: "))

                start_time = time.time()  # Start the timer just before the actual query operation
                result = avl_tree.get_products_in_range(avl_root, low_price, high_price)  # Query AVL tree using avl_root
                end_time = time.time()  # End the timer

                if result:
                    for product in result:
                        print(f"ID: {product['id']}, Name: {product['name']}, Price: {product['price']}")
                else:
                    print("No products found in this price range.")
                
                print(f"Time taken for Query products by price range operation: {end_time - start_time:.6f} seconds")
            except ValueError:
                print("Invalid input! Please enter valid price values.")

        elif choice == '8':  # Query products by multiple parameters (Range Tree)
            try:
                low_price = float(input("Enter the lower bound of the price range: "))
                high_price = float(input("Enter the upper bound of the price range: "))
                category = input("Enter category (leave blank to skip): ")
                quantity_low = int(input("Enter minimum quantity (leave blank to skip): ") or 0)
                quantity_high = int(input("Enter maximum quantity (leave blank to skip): ") or 1000)

                filters = {
                    "price": (low_price, high_price),
                    "category": (category, category) if category else None,
                    "quantity": (quantity_low, quantity_high)
                }

                result = []

                # Start timing the query operation
                start_time = time.time()

                range_tree.query_by_parameters(range_tree.root, {k: v for k, v in filters.items() if v}, result)

                # End timing the query operation
                end_time = time.time()
                time_taken = end_time - start_time

                # Display results
                if result:
                    for product in result:
                        print(f"ID: {product['id']}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Quantity: {product['quantity']}")
                else:
                    print("No products found for the given parameters.")
                
                # Print the execution time
                print(f"Time taken for Query products by multiple parameters operation: {time_taken:.6f} seconds")

            except ValueError:
                print("Invalid input! Please enter valid values.")

        elif choice == '9':  # Display all products in the inventory
            if inventory:
                for product_id, product in inventory.items():
                    print(f"ID: {product_id}, Name: {product['name']}, Category: {product['category']}, Price: {product['price']}, Quantity: {product['quantity']}")
            else:
                print("Inventory is empty!")

        elif choice == '10':  # Exit the program
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")


@memory_it("Memory taken to initialize products", collect_data=True)
@time_it("Time taken to initialize products")
def initialize_large_dummy_products(num_products):
    """
    Initializes large dummy products for stress testing with time and memory tracking.
    """
    global avl_root, product_counter  # Now product_counter is defined

    for _ in range(num_products):
        product_id = product_counter
        name = f"Product_{product_id}"
        category = "Category_1" if product_id % 2 == 0 else "Category_2"
        price = float(product_id * 10)  # Incremental price for each product
        quantity = product_id % 100 + 1  # Random quantity between 1 and 100

        product = {'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity}
        avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)
        range_tree.root = range_tree.insert(range_tree.root, product, 'price')
        double_ended_pq.add_product(product)

        product_counter += 1


if __name__ == "__main__":
    # Step 1: Define input sizes for stress testing
    input_sizes = [10, 100,1000] # this also takes comma separated values like [10,100,1000]

    # Step 2: Initialize lists to store execution times and memory usages
    execution_times = []
    memory_usages = []

    # Step 3: Measure both time and memory usage for each input size
    for size in input_sizes:
        start_time = time.time()

        # Measure memory usage using the memory_it decorator
        memory_used = initialize_large_dummy_products(size)

        end_time = time.time()
        time_taken = end_time - start_time

        # Append both time and memory usage results
        execution_times.append(time_taken)
        memory_usages.append(memory_used)

        # Print results to the console
        print(f"Input size {size}: Time taken = {time_taken:.6f} seconds, Memory used = {memory_used:.6f} MiB")

    # Step 4: Plot and save the graph for execution times
    plot_execution_times(input_sizes, execution_times, "initialize_large_dummy_products")

    # Step 5: Plot and save the graph for memory usage
    plot_memory_usage(input_sizes, memory_usages, "initialize_large_dummy_products")

    # Step 6: Start the inventory management system (CLI)
    run_inventory_management()

