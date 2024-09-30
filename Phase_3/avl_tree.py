"""
This file contains the AVL Tree implementation used in the Dynamic Inventory Management System.
The AVL Tree is a balanced binary search tree that allows for efficient querying of products by price range.
"""

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

    def insert(self, root, price, product):
        """
        Inserts a product into the AVL tree and balances the tree if necessary.
        """
        if not root:  # If the root is None, create a new node
            #print(f"Inserting product with price {price} into AVL Tree")  # Debugging: Track insertion
            return AVLNode(price, product)
        
        # Insert based on price
        if price < root.price:
            root.left = self.insert(root.left, price, product)
        else:
            root.right = self.insert(root.right, price, product)

        # Update the height of the node
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Get the balance factor to check if the tree is balanced
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

        return root  # Return the root of the balanced subtree

    def get_products_in_range(self, root, low, high, result):
        """
        Retrieves all products from the AVL tree that fall within a given price range.
        """
        if not root:  # If the subtree is empty, return
            return

        # Debugging to track the traversal of the AVL tree
        #print(f"Visiting node with price: {root.price}")

        # If the current node's price is within the range, add it to the result
        if low <= root.price <= high:
            print(f"Product with price {root.price} is in range [{low}, {high}]")  # Debugging: Price is in range
            result.append(root.product)

        # Recur for the left and right subtrees based on the price range
        if low < root.price:
            self.get_products_in_range(root.left, low, high, result)

        if high > root.price:
            self.get_products_in_range(root.right, low, high, result)

    # Rotations to maintain AVL balance
    def rotate_left(self, z):
        """
        Performs a left rotation on the given node to balance the AVL tree.
        """
        y = z.right  # y becomes the new root
        T2 = y.left  # T2 becomes the right subtree of z
        y.left = z  # z becomes the left child of y
        z.right = T2  # T2 becomes the right child of z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # Update height of z
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))  # Update height of y
        return y  # Return the new root

    def rotate_right(self, z):
        """
        Performs a right rotation on the given node to balance the AVL tree.
        """
        y = z.left  # y becomes the new root
        T3 = y.right  # T3 becomes the left subtree of z
        y.right = z  # z becomes the right child of y
        z.left = T3  # T3 becomes the left child of z
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))  # Update height of z
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))  # Update height of y
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

