'''
=========================================
TREE DATA STRUCTURE
=========================================

Tree:
-----
A Tree is a non-linear hierarchical data structure that consists of nodes
connected by edges.

- The topmost node is called the Root.
- Each node can have zero or more child nodes.
- Nodes with no children are called Leaf Nodes.
- Every node (except the root) has exactly one parent.

Unlike a Linked List, where each node points to only one next node,
a Tree node can point to multiple child nodes.

--------------------------------------------------
Linear Data Structures
--------------------------------------------------
Data flows sequentially.

Examples:
- Arrays
- Linked Lists
- Stacks
- Queues

--------------------------------------------------
Non-Linear Data Structures
--------------------------------------------------
Data is organized hierarchically or in multiple directions.

Examples:
- Trees
- Graphs

==================================================
Where Trees are Used
==================================================

1. File Systems
   Example:
        C:
        ├── Users
        │   ├── Manoj
        │   └── Public
        └── Program Files

2. Organization Charts
        CEO
        ├── Manager 1
        │   ├── Employee A
        │   └── Employee B
        └── Manager 2

3. Databases
   - B-Trees and B+ Trees are used for indexing.
   - They allow fast searching, insertion, and deletion.

4. Routing Tables
   - Network routing algorithms often use tree-like structures.

5. Searching and Sorting
   - Binary Search Trees (BST)
   - AVL Trees
   - Red-Black Trees

6. Priority Queues
   - Implemented using Binary Heaps.

==================================================
Types of Trees
==================================================

1. Binary Tree
---------------
Each node has at most two children.

        A
       / \
      B   C
     / \
    D   E

2. Binary Search Tree (BST)
----------------------------
A Binary Tree where:

Left subtree values  < Parent
Right subtree values > Parent

Example:

        50
       /  \
     30    70
    / \    / \
   20 40 60 80

Searching is efficient because of the ordering.

3. AVL Tree
------------
An AVL Tree is a self-balancing Binary Search Tree.

For every node:

| Height(Left Subtree) - Height(Right Subtree) | <= 1

Whenever this condition is violated after insertion or deletion,
the tree performs rotations to restore balance.

==================================================
Trees vs Arrays vs Linked Lists
==================================================

Array
-----
Advantages:
- O(1) random access using index.

Disadvantages:
- Insertion and deletion are expensive because elements must be shifted.

Example:
[10, 20, 30, 40]

Insert 15 at index 1

Before:
10 20 30 40

After:
10 15 20 30 40

Elements after index 1 are shifted.

--------------------------------------------------

Linked List
-----------
Advantages:
- Fast insertion and deletion once the position is known.
- No shifting required.

Disadvantages:
- Random access is not possible.
- Must traverse from the head node.

--------------------------------------------------

Binary Search Tree
------------------
Advantages:
- Efficient searching, insertion, and deletion.
- Average Time Complexity:
    Search   -> O(log n)
    Insert   -> O(log n)
    Delete   -> O(log n)

Worst case (unbalanced tree):
    O(n)

Balanced trees like AVL Trees avoid this worst case.

'''