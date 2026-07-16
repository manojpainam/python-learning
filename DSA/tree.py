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

"""
Tree Traversal:
Traversal means visiting each node of a tree exactly once.

There are two main types of tree traversal:

1. Breadth First Search (BFS)
   - Visits all nodes level by level.
   - Also called Level Order Traversal.

2. Depth First Search (DFS)
   - Explores as deep as possible before backtracking.

DFS has three types:
    1. Preorder  : Root -> Left -> Right
    2. Inorder   : Left -> Root -> Right
    3. Postorder : Left -> Right -> Root
"""

# ---------------- Preorder Traversal ----------------
# Root -> Left -> Right

def preorder_traversal(node):
    if node is None:
        return

    print(node.data, end=", ")
    preorder_traversal(node.left)
    preorder_traversal(node.right)


# ---------------- Inorder Traversal ----------------
# Left -> Root -> Right

def inorder_traversal(node):
    if node is None:
        return

    inorder_traversal(node.left)
    print(node.data, end=", ")
    inorder_traversal(node.right)


# Example usage
print("Preorder Traversal:")
preorder_traversal(root)

print("\n\nInorder Traversal:")
inorder_traversal(root)


# ---------------- Postorder Traversal ----------------
# Left -> Right -> Root

def postorder_traversal(node):
    if node is None:
        return

    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.data, end=", ")


print("\n\nPostorder Traversal:")
postorder_traversal(root)

#Linear data structure : data will stored in a line 12, 13, 15
#example : linked list, arrays, vectors

#hirarchial data structure : data will be stored in tree  or levels of example : files in a computer
#example : Trees

'''
Trees are connetced by node. Topmost node is called root and connecting nodes in between are called branches
'''

'''
Terms which are used in tree (Binary Trees) -
                        Generic tree :-
                                Parent - top most or root element is called parent
                                child - from 1 level when we have different noes then it is called child. child can also be parent to the its further children
                        Binary Tree - 
                                Binary Trees will have at max 2 children at each nodes
                                binary in computer science is base 2 which means that the node can have (0, 1, 2)

                                top most element is know as root
                                leaf nodes - means nodes which will have the 0 children
                        Branches - the connections between the nodes is known as branches
                        siblings child - which will have the nodes at the same level
                        levels - as it is hirarchial data structures the nodes are in the form of levels
                        height - height = total levels of the tree
                        subtree - it is a small part of a tree

                        solution - try to calculate the solution for the left sub tree and then right subtree and combined entire tree which makes easier for breaking down the problem


'''
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None
    
    def add_children(self, child):
        child.parent = self
        self.children.append(child)

def build_product_tree():
    root = TreeNode("Electronics")
    laptop = TreeNode("Laptop")
    laptop.add_children(TreeNode("Mac"))
    laptop.add_children(TreeNode("Dell insprion"))
    laptop.add_children(TreeNode("HP pivilion"))

    mobile = TreeNode("Mobile")
    mobile.add_children(TreeNode("Iphone"))
    mobile.add_children(TreeNode("Samsung"))
    mobile.add_children(TreeNode("Vivo"))
    mobile.add_children(TreeNode("Nothing"))
    

    tv = TreeNode("Telivisions")
    tv.add_children(TreeNode("Samsung"))
    tv.add_children(TreeNode("Sony"))
    tv.add_children(TreeNode("LG"))

    root.add_children(laptop)
    root.add_children(mobile)
    root.add_children(tv)

    return root

if __name__ == '__main__':
    root = build_product_tree()
    pass

