# Algorithms and Data Structures

- [Algorithms](#algorithms)
  - [Search Algorithms](#search-algorithms)
  - [Sorting Algorithms](#sorting-algorithms)
  - [Greedy Algorithms](#greedy-algorithms)
- [Data Structures](#data-structures)
  - [Arrays](#arrays)
  - [Linked Lists](#linked-lists)
  - [HashMaps | Hashed Tables | Dictionaries (Python)](#hashmaps--hashed-tables--dictionaries-python)
  - [Stacks](#stacks)
  - [Queues](#queues)
  - [Trees](#trees)
  - [Graphs](#graphs)

## Algorithms

### Search Algorithms
- **Binary Search**:
  - Used to find a specific element in a sorted list efficiently.
  - Inefficient: O(n) for linear search, incrementally guessing from start to end.
  - Efficient: O(log2(n)) for binary search, repeatedly dividing the search interval in half until the correct element is found.

- **Depth-First Search (DFS)**:
  - Begins at the root node and explores as far as possible along each branch before backtracking.
  - Utilizes a visited array to track already visited nodes.
  - Continues backtracking until all nodes are visited.
  - **Real-life example**: Solving a maze by systematically exploring paths until the exit is found.

- **Breadth-First Search (BFS)**:
  - Looks at every node at one level before going down to the next level.
  - Utilizes a visited array to track already visited nodes and a queue to keep track of neighbors.
  - Begins at the root node and adds it to the visited array and all its connected nodes to the queue, then continues to explore nodes level by level.
  - **Real-life example**: Chess algorithms predict the best move by exploring possible moves at each level of the game tree.
  - **Runtime**: O(V + E), where V is the number of vertices and E is the number of edges.

### Sorting Algorithms
- **Insertion Sort**:
  - Examines each element in the list, comparing it with the previous elements and shifting them to the right until the correct position for insertion is found.
  - Simple sorting algorithm suitable for small datasets or nearly sorted arrays.
  - **Runtime**:
    - Best case: O(n) when the list is already sorted.
    - Worst case: O(n^2) when the list is sorted in reverse order.
  
- **Merge Sort**:
  - A divide-and-conquer sorting algorithm that breaks the problem into smaller subproblems and solves them recursively.
  - Starts by splitting the array into halves recursively until each subarray consists of single elements.
  - Merges pairs of subarrays by comparing elements and placing them in sorted order.
  - **Runtime**: O(n log(n)) in both best and worst cases, making it efficient for large datasets.

- **Quick Sort**:
  - A complex sorting algorithm that follows the divide-and-conquer approach and is recursive.
  - Selects a pivot element and partitions the list into two sublists: one with elements greater than the pivot and the other with elements less than the pivot.
  - **Runtime**:
    - Best case: O(n log(n)).
    - Worst case: O(n^2).

### Greedy Algorithms
- A problem-solving approach that makes the locally optimal choice at each stage with the hope of finding a global optimum.
- **Real-life example**: Finding the shortest path in a weighted graph using Dijkstra's algorithm, selecting the vertex with the smallest distance from the source.

## Data Structures

### Arrays
- Read: O(1)
- Insertion: O(n)
- Deletion: O(n)
- Fast at reading but slow at insertion and deletion.
- Stored in a contiguous form of memory.

### Linked Lists
- Opposite of arrays.
- Do not have indexes.
- Read: O(n)
- Insertion: O(1)
- Deletion: O(1)
- Efficient for insertion and deletion but slow at reading.
- Each element has a pointer to the next element.

### HashMaps | Hashed Tables | Dictionaries (Python)
- Read: O(1)
- Insertion: O(1)
- Deletion: O(1)
- Similar to arrays but with named indexes (keys); unordered but provide fast lookup.

### Stacks
- Push: O(1) (add new element at top)
- Pop: O(1) (remove element at top)
- Peak: O(1) (see element at top)
- Follow the LIFO (Last In, First Out) principle.

### Queues
- Enqueue: O(1) (add new element to back)
- Dequeue: O(1) (remove element)
- Front: O(1) (see front element)
- Follow the FIFO (First In, First Out) principle.

### Trees
- Read/Search: O(log n)
- Insertion: O(log n)
- Deletion: O(log n)
- Nodes connected by edges; useful for hierarchical data.

  #### Binary Trees
  - Efficient searching of ordered values.
  - Follow a binary search property.

### Graphs
- Traversal/Search: O(V + E) (V: number of vertices, E: number of edges)
- Insertion: O(1)
- Deletion: O(1)
- Versatile models for connections; can include cycles and weights.
