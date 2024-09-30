# Dynamic Inventory Management System - Phase 3

## Overview

This is the third phase of the **Dynamic Inventory Management System**. The system provides a command-line interface (CLI) for managing an inventory of products, supporting various operations like adding, updating, deleting, and querying products. The system also supports querying by price range (using an AVL Tree) and multiple parameters (using a Range Tree). Additionally, it incorporates time and memory tracking features, designed for large-scale data handling, and advanced testing capabilities.

## Key Features

1. **Product Management**: 
   - Add, update, delete, and display products in the inventory.
   - Products are stored in a hash table for quick lookups.

2. **Price Range Query (AVL Tree)**:
   - Query products within a specific price range using an AVL Tree.
   - The AVL Tree implementation includes caching via Python's `functools.lru_cache` to improve performance for repeated queries.

3. **Multi-Parameter Query (Range Tree)**:
   - Query products by multiple parameters such as price, category, and quantity using a Range Tree.

4. **Price Retrieval (Heap & Double-Ended Priority Queue)**:
   - Get the product with the lowest price via both a Min-Heap and a Double-Ended Priority Queue.
   - Get the product with the highest price via the Double-Ended Priority Queue.

5. **Stress Testing and Optimization**:
   - Time and memory tracking for initializing large dummy datasets.
   - Efficient memory and performance optimization strategies are incorporated.

6. **Testing Framework**:
   - Comprehensive set of test cases for evaluating the system’s performance and correctness.
   - Stress testing performed under large dataset conditions.

## How to Run

### Prerequisites
- Python 3.x
- Required libraries: `heapq`, `functools`, `time`, `matplotlib`, `memory_profiler`
- python3 phase3.py

### Running the Program

To run the main program:

1. Clone the repository to your local machine.
2. Navigate to the folder where the code resides.
3. Execute the following command in your terminal to run the inventory management system:


### Steps to Run the Tests

1.  **Ensure all necessary files are in the same directory**:
   - `phase3.py` (Main inventory management code)
   - `heap_handler.py` (Heap operations)
   - `avl_tree.py` (AVL tree implementation)
   - `range_tree.py` (Range tree implementation)
   - `double_ended_priority_queue.py` (Priority queue operations)
   - `utils.py` (Utility functions for time and memory tracking)
   - `test_phase3.py` (Test cases for the system)

2. **Install necessary libraries**:
   - Ensure that you have the required libraries installed. If not, you can install them by running:
   
   ```bash
   pip install memory-profiler matplotlib
3. Running the test cases
	To execute the test cases, run the test_phase3.py file using the following command in the terminal:
	python test_phase3.py or python3 test_phase3.py depending on your python configuration
4. Expected Output: The tests will display the results of each test case as either "Passed" or "Failed." A sample output looks like this:
	Running: test_product_addition
	Passed: test_product_addition
	Running: test_product_update
	Passed: test_product_update
	Running: test_product_deletion
	Product 101 deleted.
	Passed: test_product_deletion
	Running: test_query_by_price_range
	Passed: test_query_by_price_range
	Running: test_query_by_multiple_parameters
	Passed: test_query_by_multiple_parameters
	Running: test_lowest_and_highest_price_product
	Passed: test_lowest_and_highest_price_product
5. Handling Large Datasets:

	The system is designed to handle large datasets with efficient memory and execution time.
	For performance and stress testing, use phase3.py to generate large dummy products and track memory and time usage:

# License
:place holder for license


