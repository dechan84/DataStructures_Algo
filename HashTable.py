# A hash table is basically a dictionary from Python, this data structure has two component
# a key and a value per element, how it works? Basically you provide a pair (key and value) to a module
# that will generate an address that will be used on memory, so every time you access that key the value
# stored at that same address previously generated will be retrieved, you cant provide an address to retrieve
# a value or key, only a key to get a value.
# Its possible that in the same address there can be more than one pair stored, this is called a 'collisions'
# There are multiple methods to avoid collisions
# Method 1 -Separate chaining: the hash table create a list inside the address and add each pair
# like an element of that list. Instead of a list we can also use a Linked List.
# Method 2 -Linear Probing: If the same address already has an element then the pair will look into the next address,
# if its not empty it will keep looking until it found an address without a pair
# In this section we are going to apply Method 1.
# Big O discussion:
# The Hash method requires O(1) to get the address based on a key,
# The get method of an Hash has the worst case scenario if all the values are stored in the same address, this
# would generate O(n) to walk trough the list inside the same address to get our value, however the idea of the
# hash method is that is efficient enough to generate our pseudo random address (within our mem range) that returns the
# minimum repeated address as possible, if we only have one value per address then the get method would be O(1).
# The dict in Python uses a very efficient Hash method that allows a very good distribution of the values in all the
# available address, is so good that is considered to have a get method of O(1)
# Interview Question! Assume we have two list, give a method that can show me if there are repeat values between
# both list.
# R/ There are two ways to solve it, the naive method is to do a nested loop and search for the value and compare
# each element between the list until the value is found, interviewer don't like this approach because is a O(n^2)
# The second method to solve it is using a dict, the first goes into a dict (key is the value, and value is True) there
# it goes our first loop, the second loop (which is not nested) check if the value is in the dict and return true.
# Code sample:
# def same_2_list(list1, list2):
#     dict = {}
#     for i in list1:
#         dict[1] = True
#     for j in list2:
#         if j in dict:
#             return True
#     return False
# This is a more efficient solution, uses O(n). For best results, gave the interviewer both answers and explain
# why the latest one is more efficient.

class HashTable:
    # The constructor will built the structure were we are going to store our pairs, in this case a list
    # To have an optimized hash table, the length of the list should be a prime number
    def __init__(self, size = 7):
        # We are creating a list of length = size (default is 7) and filled with none value
        self.data_map = [None]*size
    # This is the hash function, basically we want to generate a pseudo random address (which are the index
    # values of the list) using key as input, there are multiple ways to do this, in this example we use this
    # math equation that plays with the letters in the key and the length of the list
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            # This equation takes each letter of the key and convert them into Ascii, then multiply by 23 and do the
            # module of the value based on the length of the list. We use 23 because its a prime number (any prime
            # number is fine), the trick here is that when we do modulo of the length, any value resulting from this
            # will range from 0 to (length - 1)
            my_hash = (my_hash + ord(letter)*23) % len(self.data_map)
        return my_hash
    # Print method, this method will print the index and value, it will also return the hash table
    def print(self):
        # enumerate will return the index to the first parameter of the loop, it usually receives the length of
        # a data structure
        for index, value in enumerate(self.data_map):
            print("Index ", index, ":", value)
        return self.data_map
    # Method to set a key and value pair into the Hash Table
    def set_items(self, key, value):
        temp_list = [key, value]
        address = self.__hash(key)
        if self.data_map[address] is None:
            # We first initalize the node in that address with an empty list if it was previously None
            self.data_map[address] = []
        self.data_map[address].append(temp_list)
        return True
    # Get method, return the values using the same key, by the way if we have an efficient Hash method then we wont be
    # using the loop because we wont have repeated address, this is only done in case of a collision, efficient Hash
    # Tables uses O(1) with the get/lookup method, inefficient ones can take worst case scenario of O(n)
    def get(self, key):
        address = self.__hash(key)
        result = []
        if self.data_map[address] is not None:
            temp_list = self.data_map[address]
            for pair in temp_list:
                if key in pair:
                    result.append(pair[1])
            return result
        return None
    # Key method, return all the keys inside the HashTable
    def keys(self):
        # address = self.__hash(key)
        result = []
        for index1 in self.data_map:
            if index1 is not None:
                if len(index1) == 1:
                    if index1[0] not in result:
                        result.append(index1[0])
                else:
                    for index2 in index1:
                        if index2[0] not in result:
                            result.append(index2[0])
        return result


