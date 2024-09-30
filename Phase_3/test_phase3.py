# test_phase3.py

from heap_handler import HeapHandler
from avl_tree import AVLTree
from range_tree import RangeTree
from double_ended_priority_queue import DoubleEndedPriorityQueue

# Initialize necessary components for testing
avl_tree = AVLTree()
range_tree = RangeTree()
double_ended_pq = DoubleEndedPriorityQueue()
inventory = {}

# Test product addition to inventory, heap, AVL tree, and double-ended priority queue
def test_product_addition():
    print("Running: test_product_addition")
    product_id = 101
    name = "Test Product"
    category = "Test Category"
    price = 100.0
    quantity = 10

    avl_root = None
    avl_root = HeapHandler.add_product_with_heap(product_id, name, category, price, quantity, inventory, avl_tree, avl_root)
    double_ended_pq.add_product({'id': product_id, 'name': name, 'category': category, 'price': price, 'quantity': quantity})

    assert product_id in inventory, "Product not added to inventory."
    assert avl_root is not None, "Product not added to AVL tree."
    assert double_ended_pq.get_lowest_price_product() is not None, "Product not added to Double-Ended Priority Queue."

    print("Passed: test_product_addition")


# Test product update functionality
def test_product_update():
    print("Running: test_product_update")
    product_id = 101
    updated_name = "Updated Product"
    updated_category = "Updated Category"
    updated_price = 150.0
    updated_quantity = 20

    avl_root = None
    avl_root = HeapHandler.update_product_with_heap(product_id, updated_name, updated_category, updated_price, updated_quantity, inventory, avl_tree, avl_root)

    product = inventory.get(product_id)
    assert product['name'] == updated_name, "Product name not updated correctly."
    assert product['category'] == updated_category, "Product category not updated correctly."
    assert product['price'] == updated_price, "Product price not updated correctly."
    assert product['quantity'] == updated_quantity, "Product quantity not updated correctly."

    print("Passed: test_product_update")


# Test product deletion functionality
def test_product_deletion():
    print("Running: test_product_deletion")
    product_id = 101

    avl_root = None
    avl_root = HeapHandler.delete_product_with_heap(product_id, inventory, avl_tree, avl_root)

    assert product_id not in inventory, "Product not deleted from inventory."

    print("Passed: test_product_deletion")


# Test querying products by price range using AVL tree
def test_query_by_price_range():
    print("Running: test_query_by_price_range")

    # Add products to test the query
    product_id = 201
    avl_root = None
    avl_root = HeapHandler.add_product_with_heap(product_id, "Product 1", "Category 1", 50, 5, inventory, avl_tree, avl_root)
    avl_root = HeapHandler.add_product_with_heap(202, "Product 2", "Category 2", 150, 15, inventory, avl_tree, avl_root)
    avl_root = HeapHandler.add_product_with_heap(203, "Product 3", "Category 3", 250, 25, inventory, avl_tree, avl_root)

    result = avl_tree.get_products_in_range(avl_root, 100, 200)

    assert len(result) == 1, "Query by price range did not return the expected number of products."
    assert result[0]['price'] == 150, "Query by price range returned incorrect product."

    print("Passed: test_query_by_price_range")


# Test querying products by multiple parameters using Range Tree
def test_query_by_multiple_parameters():
    print("Running: test_query_by_multiple_parameters")

    # Add products to test the query
    product = {'id': 301, 'name': "Product 1", 'category': "Category 1", 'price': 100, 'quantity': 10}
    range_tree.root = range_tree.insert(range_tree.root, product, 'price')
    product = {'id': 302, 'name': "Product 2", 'category': "Category 2", 'price': 200, 'quantity': 20}
    range_tree.root = range_tree.insert(range_tree.root, product, 'price')
    product = {'id': 303, 'name': "Product 3", 'category': "Category 3", 'price': 300, 'quantity': 30}
    range_tree.root = range_tree.insert(range_tree.root, product, 'price')

    filters = {"price": (100, 250), "category": ("Category 1", "Category 2")}
    result = []
    range_tree.query_by_parameters(range_tree.root, filters, result)

    assert len(result) == 2, "Query by multiple parameters did not return the expected number of products."
    assert result[0]['category'] == "Category 1", "Query by multiple parameters returned incorrect product."
    assert result[1]['category'] == "Category 2", "Query by multiple parameters returned incorrect product."

    print("Passed: test_query_by_multiple_parameters")


# Test retrieving the lowest and highest priced product from Double-Ended Priority Queue
def test_lowest_and_highest_price_product():
    print("Running: test_lowest_and_highest_price_product")

    double_ended_pq.add_product({'id': 401, 'name': "Product 1", 'category': "Category 1", 'price': 50, 'quantity': 5})
    double_ended_pq.add_product({'id': 402, 'name': "Product 2", 'category': "Category 2", 'price': 500, 'quantity': 50})

    lowest_product = double_ended_pq.get_lowest_price_product()
    highest_product = double_ended_pq.get_highest_price_product()

    assert lowest_product['price'] == 50, "Lowest price product retrieval failed."
    assert highest_product['price'] == 500, "Highest price product retrieval failed."

    print("Passed: test_lowest_and_highest_price_product")


# Main block to run the tests
if __name__ == "__main__":
    test_product_addition()
    test_product_update()
    test_product_deletion()
    test_query_by_price_range()
    test_query_by_multiple_parameters()
    test_lowest_and_highest_price_product()

