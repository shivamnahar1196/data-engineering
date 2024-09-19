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
  
  ### Example Table: `StudentCourses`
  
  | StudentID | StudentName | CourseID | CourseName      | Instructor     |
  |-----------|-------------|----------|------------------|-----------------|
  | 1         | Alice       | 101      | Math              | Prof. Smith     |
  | 1         | Alice       | 102      | Science           | Prof. Jones     |
  | 2         | Bob         | 101      | Math              | Prof. Smith     |
  | 3         | Charlie     | 103      | History           | Prof. Brown     |
  
  ### 1NF (First Normal Form)
  To satisfy 1NF, we need to ensure:
  - Each column has atomic values (no lists or multiple values in a single cell).
  - Each entry in a column has the same data type.
  
  **In our example:** 
  - Each cell contains atomic values (e.g., "Alice" in `StudentName`, "Math" in `CourseName`).
  - There are no multi-valued attributes.
  
  **Result:** The table is in 1NF.
  
  ### 2NF (Second Normal Form)
  To meet 2NF, we must:
  - Be in 1NF.
  - Ensure all non-key attributes are fully functionally dependent on the primary key.
  
  **Primary Key:** In this case, a composite key of (`StudentID`, `CourseID`) can be used. 
  
  **Non-key attributes:** `StudentName`, `CourseName`, `Instructor`.
  
  **Issues:**
  - `StudentName` is dependent only on `StudentID`, not on `CourseID`.
  - `CourseName` and `Instructor` are dependent only on `CourseID`.
  
  **To achieve 2NF, we need to split the table:**
  
  #### Students Table
  | StudentID | StudentName |
  |-----------|-------------|
  | 1         | Alice       |
  | 2         | Bob         |
  | 3         | Charlie     |
  
  #### Courses Table
  | CourseID | CourseName | Instructor     |
  |----------|------------|-----------------|
  | 101      | Math       | Prof. Smith     |
  | 102      | Science    | Prof. Jones     |
  | 103      | History    | Prof. Brown     |
  
  #### StudentCourses Table
  | StudentID | CourseID |
  |-----------|----------|
  | 1         | 101      |
  | 1         | 102      |
  | 2         | 101      |
  | 3         | 103      |
  
  ### 3NF (Third Normal Form)
  To be in 3NF, we must:
  - Be in 2NF.
  - Ensure there are no transitive dependencies (i.e., non-key attributes should not depend on other non-key attributes).
  
  **In our current structure:**
  - `Instructor` depends on `CourseID` (a non-key attribute).
  - This means `Instructor` is transitively dependent on `StudentID` through `CourseID`.
  
  **To achieve 3NF, we keep the tables as they are but need to ensure that `Instructor` is only in the `Courses` table.**
  
  ### Final Structure in 3NF
  
  #### Students Table
  | StudentID | StudentName |
  |-----------|-------------|
  | 1         | Alice       |
  | 2         | Bob         |
  | 3         | Charlie     |
  
  #### Courses Table
  | CourseID | CourseName | Instructor     |
  |----------|------------|-----------------|
  | 101      | Math       | Prof. Smith     |
  | 102      | Science    | Prof. Jones     |
  | 103      | History    | Prof. Brown     |
  
  #### StudentCourses Table
  | StudentID | CourseID |
  |-----------|----------|
  | 1         | 101      |
  | 1         | 102      |
  | 2         | 101      |
  | 3         | 103      |
  
  ### Summary
  1. **1NF:** Atomic values; all entries in a column are of the same type.
  2. **2NF:** Non-key attributes fully depend on the primary key (no partial dependency).
  3. **3NF:** No transitive dependencies among non-key attributes.
  
  This structure reduces redundancy and improves data integrity. Let me know if you need further clarification! 
  
---

### 2. Denormalization
  
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
