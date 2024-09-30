"""
This file contains the Range Tree implementation for multi-parameter querying.
The Range Tree allows for efficient querying by multiple parameters, such as price, category, quantity, etc.
"""

class RangeTreeNode:
    """
    Represents a node in the Range Tree, which stores product data and allows for querying by multiple parameters.
    """
    def __init__(self, product):
        self.product = product  # The product data stored in the node
        self.left = None  # Left child for lower values
        self.right = None  # Right child for higher values

class RangeTree:
    """
    Implements the Range Tree, a data structure that allows for querying products by multiple parameters.
    """
    def __init__(self):
        self.root = None  # Initialize the root of the Range Tree as None

    def insert(self, root, product, key):
        """
        Inserts a product into the Range Tree based on a specified key (e.g., price, category, etc.)
        """
        if not root:
            return RangeTreeNode(product)  # Create a new node if we're at a leaf
        
        # Decide where to insert based on the key value (e.g., price)
        if product[key] < root.product[key]:
            root.left = self.insert(root.left, product, key)
        else:
            root.right = self.insert(root.right, product, key)
        
        return root

    def query_range(self, root, low, high, key, result):
        """
        Queries the Range Tree for products within a given range on the specified key.
        """
        if not root:
            return
        
        # Check if the current product falls within the range
        if low <= root.product[key] <= high:
            result.append(root.product)

        # Recur for left and right subtrees based on the range
        if low < root.product[key]:
            self.query_range(root.left, low, high, key, result)
        
        if high > root.product[key]:
            self.query_range(root.right, low, high, key, result)

    def query_by_parameters(self, root, filters, result):
        """
        Queries the Range Tree based on multiple parameters (like price, category, etc.)
        Filters is a dictionary where keys are parameters and values are tuples of (low, high).
        """
        if not root:
            return
        
        # Check each filter (price, category, etc.)
        is_in_range = all(low <= root.product[key] <= high for key, (low, high) in filters.items())
        
        if is_in_range:
            result.append(root.product)
        
        # Recur for both left and right subtrees
        self.query_by_parameters(root.left, filters, result)
        self.query_by_parameters(root.right, filters, result)

# Example Usage:
# range_tree = RangeTree()
# root = range_tree.insert(None, product_data, "price")
# filters = {"price": (100, 500), "quantity": (1, 50)}
# result = []
# range_tree.query_by_parameters(root, filters, result)

