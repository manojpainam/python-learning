'''
===========================
Queue Data Structure
===========================

A Queue is a linear data structure that follows the FIFO (First In, First Out)
principle. The element that is inserted first is removed first.

Real-world Example:
------------------
Imagine a queue at a movie theater.
The person who joins the queue first gets the ticket first.

Another Example:
----------------
Suppose the NSE (National Stock Exchange) generates live stock price updates.

Without a Queue:
- NSE sends data directly to financial websites like Yahoo Finance, Google Finance, etc.
- If the API format changes, every consumer application must also update its code.
- This creates a tightly coupled architecture because producers and consumers depend
  directly on each other.

With a Queue:
- NSE pushes stock price updates into a Queue.
- Financial websites read data from the Queue whenever they are ready.
- New consumers can subscribe without requiring any changes to the producer.
- This creates a loosely coupled architecture and improves scalability.

Architecture:
Producer  --->  Queue  --->  Consumer

FIFO:
-----
First In, First Out
Example: A movie theater queue where the first person in line gets served first.
'''


# Queue implementation using a Python list
stock_price = []

# Insert elements at the beginning of the list
stock_price.insert(0, 131.19)
stock_price.insert(0, 131.78)
stock_price.insert(0, 132)

# Remove elements from the end (FIFO behavior)
print(stock_price.pop())
print(stock_price.pop())
print(stock_price.pop())

# If there are no elements, pop() raises an IndexError.
# print(stock_price.pop())


# Queue implementation using collections.deque
from collections import deque

q = deque()

# Insert elements from the left side
q.appendleft(2)
q.appendleft(9)
q.appendleft(90)

# Remove elements from the right side (FIFO)
print(q.pop())
print(q.pop())
print(q.pop())

# Calling pop() on an empty deque raises an IndexError.
# q.pop()


# Queue implementation using a custom class
class Queue:
    def __init__(self):
        # deque provides efficient O(1) enqueue and dequeue operations.
        self.buffer = deque()

    def enqueue(self, value):
        # Add an element to the rear of the queue.
        self.buffer.appendleft(value)
    
    def dequeue(self):
        # Remove and return the oldest element from the queue.
        return self.buffer.pop()
    
    def is_empty(self):
        # Returns True if the queue contains no elements.
        return len(self.buffer) == 0
    
    def size(self):
        # Returns the number of elements currently in the queue.
        return len(self.buffer)
    

pq = Queue()

pq.enqueue({
    "company" : "HDFC bank",
    "time" : "08 Jul, 10:30 AM",
    "price" : "130.0"
})

pq.enqueue({
    "company" : "HDFC bank",
    "time" : "08 Jul, 10:31 AM",
    "price" : "130.4"
})

pq.enqueue({
    "company" : "HDFC bank",
    "time" : "08 Jul, 10:32 AM",
    "price" : "135.99"
})

print(pq.buffer)