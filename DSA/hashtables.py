'''
====================================
Hash Table
====================================

A Hash Table is a data structure that stores data as key-value pairs.

It is generally used when we want to access, insert, or search data very
quickly. In most cases, these operations take O(1) (constant) time.

Why do we need a Hash Table?
----------------------------
1. Searching in a Linked List is slow because we have to traverse one node
   after another until we find the required element.
   Time Complexity: O(n)

2. Searching in an Array/List is easy only if we already know the index.
   If we need to search for a value without knowing its index, we must
   check each element one by one.
   Time Complexity: O(n)

3. A Hash Table uses a hash function to calculate the index where the data
   should be stored, making searching much faster.

Building a simple Hash Table:
-----------------------------
1. Create an empty hash table (using a list, dictionary, or set).
2. Create a hash function.
3. Insert elements using the hash function.
4. Search for elements using the hash function.
5. Handle collisions when two values map to the same index.
'''

# Create an empty hash table
# Each position will later store one or more values.
#my_list = [None, None, None, None, None, None, None, None, None, None]
my_list = [[] for _ in range(10)]

# -----------------------------------
# Create a Hash Function
# -----------------------------------
'''
A hash function converts a value (such as a string) into an integer.

The returned integer is used as the index where the value will be stored
inside the hash table.

In this example:
1. Convert every character into its ASCII value using ord().
2. Add all ASCII values together.
3. Use the modulo (%) operator so the index stays within the size of
   the hash table (0 to 9).
'''

def hash_function(value):
    sum_of_chars = 0

    for char in value:
        sum_of_chars += ord(char)

    return sum_of_chars % 10


# -----------------------------------
# Insert an Element
# -----------------------------------
def add(name):
    index = hash_function(name)

    # Basic insertion (works only if there are no collisions)
    # my_list[index] = name

    # Collision handling:
    # Each index now stores a bucket (a list), so multiple values
    # can be stored at the same index.
    my_list[index].append(name)


# -----------------------------------
# Search for an Element
# -----------------------------------
def contains(name):
    index = hash_function(name)

    # Returns True if the value exists in the bucket,
    # otherwise returns False.
    return my_list[index] == name


# add('Pete')
# add('Jones')
# add('Lisa')
# add('Siri')

print(my_list)


# -----------------------------------
# Handling Collisions
# -----------------------------------
'''
A collision occurs when two different values produce the same hash index.

Example:
Suppose both "Pete" and "Stuart" produce the hash value 3.

If we simply do:
    my_list[3] = value

the new value will overwrite the old one, causing data loss.

To solve this problem, we use "Separate Chaining".

Instead of storing a single value at each index, we store a list (called a
bucket). Every value that hashes to the same index is added to that bucket.

Example:

my_list = [
    [], [], [], [], [], [], [], [], [], []
]

Now if both "Pete" and "Stuart" hash to index 3, the bucket becomes:

my_list[3] = ['Pete', 'Stuart']

This allows multiple values to exist at the same index without overwriting
each other.
'''

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')

print("After adding elements with collisions:", my_list)
print(my_list)