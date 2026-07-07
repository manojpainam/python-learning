'''
===========================
Linked List
===========================

A Linked List is a linear data structure that stores elements as individual
nodes instead of storing them in contiguous memory like an array.

Why do we need a Linked List?
-----------------------------
Arrays have a few drawbacks:

1. Inserting an element at the beginning or in the middle requires shifting
   all the following elements one position to the right.

2. Deleting an element from the beginning or middle requires shifting the
   remaining elements one position to the left.

3. Arrays use contiguous memory (all elements are stored one after another).
   If the array becomes full, the system allocates a larger block of memory
   and copies all existing elements to the new location.

How does a Linked List solve this?
----------------------------------
- A linked list stores each element (called a node) at any available memory
  location (not necessarily contiguous).

- Each node contains:
    1. The actual data.
    2. A reference (pointer) to the next node.

- Since nodes are connected using references, inserting or deleting nodes
  at the beginning does not require shifting other elements.

Time Complexity
---------------
Insert at beginning      : O(1)
Delete at beginning      : O(1)
Insert at end            : O(n)   (without a tail pointer)
Delete at end            : O(n)

Doubly Linked List
------------------
A doubly linked list stores:
    - Reference to the next node.
    - Reference to the previous node.

This allows traversal in both forward and backward directions.
'''


# Represents a single node in the linked list
class Node:

    # Constructor to initialize a node
    def __init__(self, data=None, next=None):

        # Stores the actual value
        self.data = data

        # Stores the reference to the next node
        self.next = next


# Represents the Linked List
class LinkedList:

    def __init__(self):

        # Initially the linked list is empty,
        # so the head points to None.
        self.head = None

    # Insert a new node at the beginning of the linked list
    def insert_at_begining(self, data):

        # Create a new node.
        # Its next pointer should point to the current head.
        node = Node(data, self.head)

        # Update the head to the newly created node.
        self.head = node

    # Utility function to print the linked list
    def print(self):

        # Check if the linked list is empty
        if self.head is None:
            print("Linked list is empty")
            return

        # Start traversal from the head node
        itr = self.head

        # Stores the string representation of the linked list
        llstr = ''

        # Traverse until we reach the last node
        while itr:

            # Append current node's data
            llstr += str(itr.data) + "-->"

            # Move to the next node
            itr = itr.next

        # Print the complete linked list
        print(llstr)

    # Insert a new node at the end of the linked list
    def insert_at_end(self, data):

        # If the linked list is empty,
        # the new node becomes the head.
        if self.head is None:
            self.head = Node(data, None)
            return

        # Start from the head node
        itr = self.head

        # Move until we reach the last node
        while itr.next:
            itr = itr.next

        # Link the last node to the newly created node
        itr.next = Node(data, None)

    # Insert multiple values into the linked list
    def insert_values(self, list_data):

        # Remove all existing nodes
        self.head = None

        # Insert each value one by one at the end
        for data in list_data:
            self.insert_at_end(data)


# Driver code
if __name__ == '__main__':

    # Create an empty linked list
    ll = LinkedList()

    # Insert nodes at the beginning
    # ll.insert_at_begining(5)
    # ll.insert_at_begining(67)

    # Insert multiple values
    ll.insert_values(["banana", "mango", "cherry"])

    # Print the linked list
    ll.print()