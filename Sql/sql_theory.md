### 1. Normalization
  
  **Normalization** is the process of organizing a database to reduce redundancy and improve data integrity. It involves dividing large tables into smaller, related tables and defining relationships between them. 
  
  #### Key Goals:
  - **Eliminate Redundancy**: Avoid storing the same data in multiple places.
  - **Ensure Data Integrity**: Make sure that data dependencies make sense.
  
  #### Normal Forms:
  Normalization typically involves several "normal forms" (1NF, 2NF, 3NF, etc.), each with specific rules:
  - **1NF (First Normal Form)**: Each column must contain atomic (indivisible) values, and each entry in a column must be of the same data type.
  - **2NF (Second Normal Form)**: Meet 1NF and ensure that all non-key attributes are fully functionally dependent on the primary key.
  - **3NF (Third Normal Form)**: Meet 2NF and ensure that all attributes are only dependent on the primary key (no transitive dependency).
  
  **Example**:
  Before normalization:
  ```plaintext
  OrderID | CustomerName | Product
  ------------------------------------
  1       | John Doe     | Apples
  1       | John Doe     | Oranges
  2       | Jane Smith   | Bananas
  ```
  
  After normalization (creating separate tables):
  - **Customers Table**: 
    ```plaintext
    CustomerID | CustomerName
    ---------------------------
    1          | John Doe
    2          | Jane Smith
    ```
  - **Orders Table**: 
    ```plaintext
    OrderID | CustomerID | Product
    --------------------------------
    1       | 1          | Apples
    1       | 1          | Oranges
    2       | 2          | Bananas
    ```
  
  ### Denormalization
  
  **Denormalization** is the process of combining normalized tables back into larger tables. This is often done to improve read performance by reducing the number of joins needed in queries.
  
  #### Key Goals:
  - **Improve Query Performance**: Fewer joins can lead to faster query times.
  - **Simplify Queries**: Makes it easier to write queries that need data from multiple tables.
  
  **Example**:
  After denormalization, you might end up with:
  ```plaintext
  OrderID | CustomerName | Product
  ------------------------------------
  1       | John Doe     | Apples
  1       | John Doe     | Oranges
  2       | Jane Smith   | Bananas
  ```
  
  ### Summary
  
  - **Normalization** focuses on reducing redundancy and ensuring data integrity by splitting data into smaller, related tables.
  - **Denormalization** aims to improve performance and simplify data access by combining tables, which can introduce some redundancy.
  
  Both processes have their place in database design, and the choice between them depends on specific application needs and performance considerations!
