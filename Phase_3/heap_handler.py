"""
This file handles the heap-related operations in the Dynamic Inventory Management System.
It includes methods for adding products to the heap, updating, and deleting products.
Heap operations are used to track product prices efficiently.
"""

import heapq  # Import heapq to use heap functionality

class HeapHandler:
    """
    This class manages the heap and product-related operations.
    It ensures that product prices are tracked and updated efficiently using a min-heap.
    """
    price_heap = []  # Heap to track product prices

    @staticmethod
    def add_product_to_heap(product_id, price):
        """
        Adds a product's price and its ID to the heap for quick retrieval of the lowest price.
        """
        heapq.heappush(HeapHandler.price_heap, (price, product_id))  # Push the product's price and ID into the heap

    @staticmethod
    def get_lowest_price_product(inventory):
        """
        Retrieves the product with the lowest price from the heap.
        """
        if HeapHandler.price_heap:
            lowest_price, product_id = HeapHandler.price_heap[0]  # Peek at the lowest-priced product
            return inventory.get(product_id, None)  # Return the product details from the inventory
        return None  # If heap is empty, return None

    @staticmethod
    def remove_product_from_heap(product_id, price):
        """
        Removes a product from the heap based on its product ID and price.
        """
        try:
            HeapHandler.price_heap.remove((price, product_id))  # Remove the product from the heap
            heapq.heapify(HeapHandler.price_heap)  # Reorder the heap
        except ValueError:
            print(f"Product {product_id} with price {price} not found in heap.")

    @staticmethod
    def add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root):
        """
        Adds a product to the inventory, inserts its price into the heap, and adds it to the AVL tree for price range queries.
        """
        if product_id in inventory:  # Check if the product already exists in the inventory
            print(f"Error: Product with ID {product_id} already exists.")
            return avl_root  # If product exists, return the unchanged AVL root

        product = {'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity}  # Create the product dictionary
        inventory[product_id] = product  # Add the product to the inventory
        HeapHandler.add_product_to_heap(product_id, price)  # Add product to the heap

        avl_root = avl_tree.insert(avl_root, price, product)  # Insert the product into the AVL tree
        return avl_root  # Return the updated AVL root

    @staticmethod
    def update_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root):
        """
        Updates an existing product in the inventory and the heap, and updates the AVL tree if the price changes.
        """
        if product_id not in inventory:  # Check if the product exists
            print(f"Error: Product with ID {product_id} does not exist.")
            return avl_root  # Return the unchanged AVL root if the product does not exist

        current_price = inventory[product_id]['price']  # Get the current price of the product
        HeapHandler.remove_product_from_heap(product_id, current_price)  # Remove the product from the heap

        # Update product details based on user input
        if name:
            inventory[product_id]['name'] = name
        if category:
            inventory[product_id]['category'] = category
        if price is not None:
            inventory[product_id]['price'] = price
        if quantity is not None:
            inventory[product_id]['quantity'] = quantity

        HeapHandler.add_product_to_heap(product_id, price)  # Re-add the product to the heap with the updated price
        avl_root = avl_tree.insert(avl_root, price, inventory[product_id])  # Insert the updated product into the AVL tree
        return avl_root  # Return the updated AVL root

    @staticmethod
    def delete_product_with_heap(product_id, inventory, avl_tree, avl_root):
        """
        Deletes a product from the inventory, removes it from the heap, and updates the AVL tree accordingly.
        """
        if product_id in inventory:  # Check if the product exists in the inventory
            current_price = inventory[product_id]['price']  # Get the current price of the product
            HeapHandler.remove_product_from_heap(product_id, current_price)  # Remove the product from the heap
            del inventory[product_id]  # Delete the product from the inventory
            # Update AVL tree accordingly
            print(f"Product {product_id} deleted.")
        else:
            print(f"Product with ID {product_id} not found.")
        return avl_root  # Return the AVL root (can be updated later if AVL deletions are implemented)

