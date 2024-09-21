# Dynamic Inventory Management System

## Overview
The **Dynamic Inventory Management System** is a Python-based project that allows for efficient management of product inventories. This system is designed to handle real-time product updates, price tracking, and querying features using several key data structures, such as a **Hash Table**, **Min-Heap**, and **AVL Tree**.

The system is accessed through a simple **command-line interface (CLI)**, enabling users to add, update, delete, and search for products efficiently. It also includes preloaded dummy data for testing purposes, allowing users to immediately interact with the system without needing to manually add products.

---

## Features
### 1. **Product Management**
- **Add New Products**: Users can add products with details like product ID, name, category, price, and quantity.
- **Update Existing Products**: Users can update the details of a product, including its price and quantity.
- **Delete Products**: Products can be deleted by their unique product ID.

### 2. **Price-Based Features**
- **Retrieve the Lowest Priced Product**: The system uses a min-heap to quickly find and retrieve the product with the lowest price.
- **Query Products by Price Range**: Users can query products within a specific price range using an AVL Tree, allowing efficient searches.

### 3. **Error Handling**
- The system includes robust error handling for invalid inputs, duplicate product IDs, and non-existent product updates/deletions.

### 4. **Preloaded Dummy Data**
- Upon starting, the system initializes with a set of preloaded dummy products, making it easy to test and demonstrate the system’s features without manual input.

---

## Limitations in the Current Phase
- **Limited Querying Features**: While the system supports querying by price range, it currently does not support more complex queries like filtering by category or combined filtering criteria (e.g., price and category).
- **No User Authentication**: The current system does not implement user roles or permissions. All users have full access to add, update, and delete products.
- **No Persistent Storage**: Data entered into the system is only stored in memory during runtime. Once the program is terminated, all product data is lost. This will be addressed in a future phase, possibly through database integration.
- **Basic User Interface**: The program uses a CLI for interaction, which is functional but not as user-friendly as a graphical user interface (GUI) might be.

---

## Running the Program
1. **Requirements**:
   - Python 3.x installed on your machine.
   - No external libraries are required aside from Python’s standard `heapq` module (which is pre-installed).

2. **Steps to Run**:
   - Save the provided Python code in a file (e.g., `inventory_management.py`).
   - Run the program from the terminal using:
     ```bash
     python3 inventory_management.py
     ```
   - The system will initialize with a set of dummy products, and you can interact with the CLI to test its features.

3. **Things to Keep in Mind**:
   - **Product IDs must be unique**: The system will prevent duplicate product IDs from being added.
   - **Correct Data Types**: When adding or updating products, ensure you input valid data types (e.g., integer for product ID, float for price). The system will catch invalid inputs, but providing the correct types will prevent any disruptions in the flow.
   - **Price Range Queries**: The price range query feature uses an AVL Tree, which ensures efficient searches. You can query for products by specifying a lower and upper price bound.

---

## Future Enhancements
- **Persistent Storage**: Future updates will include the ability to save product data in a database, allowing the system to retain information between sessions.
- **Advanced Query Features**: Additional query features such as filtering by category, combined filters, and sorting options.
- **Improved User Interface**: Possible implementation of a graphical user interface (GUI) for a more user-friendly experience.

---

## License
Free for now

