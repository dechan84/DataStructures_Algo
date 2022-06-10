# Big O is the measuring of time complexity when comparing codes that does the same output
# Best case scenario is omega, average is theta and worst case is omicron (O)
# Explaining O (n), this is also called proportional. Imagine a lineal function where n is x axis and
# number of operations is y axis, correlate previous explanation with the code below:

def print_items(n):
    for i in range(n):
        print (i)


print_items(10)

# Drop Constants concept on O(n), imagine if we have two loops doing the same thing, you cold assume that we
# have n +  n times of complexity or O(2n), we can simplify this by dropping the constant and we write it
# as O(n), correlate previous explanation with the code below:


def print_items2(n):
    for i in range(n):
        print (i)
    for j in range(n):
        print (j)


print_items2(10)

# O(n^2) simplifying concept: Imagine we have now a nested loop in this case it would be considered a
# time complexity of O(n^2), if we have another nested loop then you could think that is a n*n*n or O(n^3),
# but no, after two nested loops it will always be O(n^2), correlate previous explanation with the code
# below (that is a O(n^2))


def print_items3(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i, j, k)


print_items3(10)

# Drop non dominant concept: If in a method with nested loop we have another loop (outside of the nested) we
# could assume that we have O(n^2 + n) in here we need to analyze the case to see if n is big number, for
# example if we have n=10 then n^2 >> n so we can drop n and just leave it to O(n^2), correlate previous
# explanation with the code below


def print_items4(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)


print_items4(10)

# O(1) concept: This is also called constant time complexity or the most efficient line of code, because
# no matter how big the n is you will still do just one operation, this are considered specifically for
# code that are not into a loop, and no matter the quantity of 'n' you have in that operation it will always
# be O(1), correlate previous explanation with the code below


def print_items5(n):
    return n+n+n+n


print_items4(10)

# O(logn) concept: Imagine we have a sorted list filled from 1 to 8, we have to found where 1 is. To do it
# we assume the words case scenario and divide the list in 2 (1st time), we look to the right side and could not
# found the number, now we divide the left side in 2 (2nd time), we look to the right side and could not
# found the number, now we divide the left side in 2 (3rd time) and in a single operation we know where the
# number is. What we did was 2^3 times of search to found the value which equals to log 8, if the quantity of
# numbers in list is n then we have O(logn) time complexity, the second most efficient time after constant time.
# Example of this time complexity is found in some sort algorithm

# Different terms for inputs: This is interview question, imagine the drop constant example but instead of using
# n parameter as input we now have a & b, a for the first loop and b for the second loop, can we simplify
# this? no in this case we cant assume the same time complexity, now it would be O(a+b), the same apply for
# nested loops, if we have a and b as inputs, it wont be O(n^2) anymore but O(a*b). Remember we can only
# simplify or reduce if we have the same input(s) but not if they are diff


def print_items6(a, b):
    for i in range(a):
        print (i)
    for j in range(b):
        print (j)


def print_items7(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


# Big O on a list: We have two extreme cases, best case scenario is if we do a pop or an append on the last item
# that is only 1 operation, but if we want to remove the first item or insert a new one with index 0 then
# besides the pop and append operations we also need to redirect the new index for all the remaining number,
# this would mean we have an operation time of O(n).
# What happens if we remove or add items in the middle of the list? The complexity is still O(n) because
# we always consider the worst case scenario and we always drop constants.

# Lets analyze come terminology:
# O(n^2): Loop within a loop
# O(n) : is proportional
# O(log n): Divide and conquer
# O(1) : Constant

# Most basic data structures have space complexity of O(n)
# Go to https://www.bigocheatsheet.com/ interviewer love to ask about which method has better time space complex
# Everything depends on the situation

