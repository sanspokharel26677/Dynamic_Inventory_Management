from functools import lru_cache  # Added lru_cache from functools

class AVLNode:
    """
    This class represents a node in the AVL tree.
    Each node stores a product's price as the key and a reference to the product as the value.
    """
    def __init__(self, price, product):
        self.price = price  # Price is the key for this node
        self.product = product  # The actual product data
        self.left = None  # Left child (products with lower prices)
        self.right = None  # Right child (products with higher prices)
        self.height = 1  # Height of the node (used for balancing)

class AVLTree:
    """
    This class implements the AVL tree, a self-balancing binary search tree that stores products by price.
    It supports efficient insertion, deletion, and querying by price range.
    """
    
    @lru_cache(maxsize=256)  # Caches up to 256 unique price range queries
    def get_products_in_range(self, root, low_price, high_price):
        """
        Retrieves all products from the AVL tree that fall within a given price range.
        Uses caching to store results of previous queries.
        """
        return self._get_products_in_range_recursive(root, low_price, high_price)

    def _get_products_in_range_recursive(self, node, low, high):
        """
        Helper recursive method to retrieve products within a price range.
        """
        if not node:
            return []

        result = []

        # If node's price is within the range, include it
        if low <= node.price <= high:
            result.append(node.product)

        # Traverse left subtree if there's a chance of finding lower prices
        if low < node.price:
            result.extend(self._get_products_in_range_recursive(node.left, low, high))

        # Traverse right subtree if there's a chance of finding higher prices
        if high > node.price:
            result.extend(self._get_products_in_range_recursive(node.right, low, high))

        return result

    def insert(self, root, price, product):
        """
        Inserts a product into the AVL tree and balances the tree if necessary.
        """
        if not root:  # If the root is None, create a new node
            return AVLNode(price, product)
        
        # Insert based on price
        if price < root.price:
            root.left = self.insert(root.left, price, product)
        elif price > root.price:
            root.right = self.insert(root.right, price, product)
        else:
            # If the price is equal, you might decide how to handle duplicates
            return root

        # Update the height of the node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor to check if the tree is balanced
        balance = self.get_balance(root)

        # Perform rotations if the tree is unbalanced
        # Left Left Case
        if balance > 1 and price < root.left.price:
            return self.rotate_right(root)
        # Right Right Case
        if balance < -1 and price > root.right.price:
            return self.rotate_left(root)
        # Left Right Case
        if balance > 1 and price > root.left.price:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        # Right Left Case
        if balance < -1 and price < root.right.price:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root  # Return the root of the balanced subtree

    # Rotations to maintain AVL balance
    def rotate_left(self, z):
        """
        Performs a left rotation on the given node to balance the AVL tree.
        """
        y = z.right  # y becomes the new root
        T2 = y.left  # T2 becomes the right subtree of z
        y.left = z  # z becomes the left child of y
        z.right = T2  # T2 becomes the right child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # Return the new root

    def rotate_right(self, z):
        """
        Performs a right rotation on the given node to balance the AVL tree.
        """
        y = z.left  # y becomes the new root
        T3 = y.right  # T3 becomes the left subtree of z
        y.right = z  # z becomes the right child of y
        z.left = T3  # T3 becomes the left child of z

        # Update heights
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y  # Return the new root

    def get_height(self, node):
        """
        Returns the height of the given node.
        """
        if not node:
            return 0
        return node.height  # Return the height of the node

    def get_balance(self, node):
        """
        Returns the balance factor of the node to check if it is balanced.
        """
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)  # Calculate the balance factor

