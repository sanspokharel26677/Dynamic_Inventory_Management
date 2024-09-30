"""
This file contains the Double-Ended Priority Queue implementation for efficiently retrieving both the lowest and highest-priced products.
"""

import heapq  # Import heapq for priority queue implementation

class DoubleEndedPriorityQueue:
    """
    Implements a Double-Ended Priority Queue for retrieving both the lowest and highest-priced products efficiently.
    """
    def __init__(self):
        self.min_heap = []  # Min-heap for getting the lowest-priced product
        self.max_heap = []  # Max-heap (negative values) for getting the highest-priced product

    def add_product(self, product):
        """
        Adds a product to both the min-heap and max-heap.
        """
        heapq.heappush(self.min_heap, (product['price'], product))
        heapq.heappush(self.max_heap, (-product['price'], product))  # Store negative prices for max-heap

    def get_lowest_price_product(self):
        """
        Retrieves the product with the lowest price from the priority queue.
        """
        if self.min_heap:
            return self.min_heap[0][1]  # Return the product with the lowest price
        return None

    def get_highest_price_product(self):
        """
        Retrieves the product with the highest price from the priority queue.
        """
        if self.max_heap:
            return self.max_heap[0][1]  # Return the product with the highest price (negative value adjusted)
        return None

    def remove_product(self, product):
        """
        Removes a product from both the min-heap and max-heap. 
        We must rebuild the heaps after removal to maintain heap properties.
        """
        try:
            self.min_heap.remove((product['price'], product))
            self.max_heap.remove((-product['price'], product))
            heapq.heapify(self.min_heap)  # Rebuild min-heap
            heapq.heapify(self.max_heap)  # Rebuild max-heap
        except ValueError:
            print(f"Product {product['id']} not found in heaps.")

# Example Usage:
# double_ended_pq = DoubleEndedPriorityQueue()
# double_ended_pq.add_product(product_data)
# lowest = double_ended_pq.get_lowest_price_product()
# highest = double_ended_pq.get_highest_price_product()

