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

#Tree implementation
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Create nodes
root = TreeNode("R")
nodeA = TreeNode("A")
nodeB = TreeNode("B")
nodeC = TreeNode("C")
nodeD = TreeNode("D")
nodeE = TreeNode("E")
nodeF = TreeNode("F")
nodeG = TreeNode("G")

# Build the tree
root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG


'''
The tree looks like this:

                R
              /   \
             A     B
            / \   / \
           C   D E   F
                  /
                 G

Root Node  : R

Leaf Nodes : C, D, E, G

Internal Nodes : R, A, B, F

Parent of G : F

Children of B : E, F
'''

print(root.right.left.data)   # E

'''
Types of Binary Trees
    1. Balanced Binary Tree

    A Binary Tree is balanced if, for every node, the height difference between its left and right subtrees is at most 1.

    Example:

        A
       / \
      B   C
     /     \
    D       E

    
2. Complete Binary Tree

    A Complete Binary Tree has:

    Every level completely filled except possibly the last.
    The last level is filled from left to right.

    Example:
    Complete
        A
      /   \
     B     C
    / \   /
   D   E F


   Not Complete
        A
      /   \
     B     C
      \   /
       E F
    Node D is missing while E exists.

3. Full Binary Tree

    A Full Binary Tree is one where every node has either:

    0 children
    2 children

    Example:
    Every node has 0 or 2 children.
        A
      /   \
     B     C
    / \   / \
   D  E  F  G

4. Perfect Binary Tree

    A Perfect Binary Tree satisfies:

    Every internal node has exactly 2 children.
    All leaf nodes are at the same level.
    Every level is completely filled

    Example : 
           A
         /   \
        B     C
       / \   / \
      D  E  F  G
'''