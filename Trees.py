# The basic element of a binary tree a Node that is forked in left and right, instead of next and prev like we sae
# in the LL and DLL cases. The ways is setup is that each Node can only point to two other Nodes.
# Some terminology:
# A 'Full Tree' is when every node either points to two other nodes or zero nodes. Example:
#              (1)
#              / \
#            (2) (3)
#            / \
#           (4)(5)
# A 'Perfect Tree' is when any level in tree that has any node is completely fill all the way across. Example:
#              (1)
#              / \
#            (2) (3)
# Any Perfect Tree is also Full Tree, but not the other way around.
# A 'Complete Tree' is when the nodes are all filled from left to right without gaps
# It doesnt need to be on the same level. Example:
#               (1)
#              /  \
#            (2)  (3)
#            / \   / \
#           (4)(5)(6)(7)
#           /
#         (8)
# Any Perfect Tree is also Complete Tree, but not the other way around.
# Example of a Full and Complete tree (but not perfect)
#               (1)
#              /  \
#            (2)  (3)
#            / \   / \
#          (4) (5)(6) (7)
#          / \
#        (8) (9)
# Parent and Child/Siblings, a Child Node share the same Parent, every node can only have 1 parent. a Child can also
# be a parent Node. A Node without children is called Leaf. Example:
#                                        (1)<- Parent
#                                        / \
#  Is a child to 1 but a father to 4 ->(3) (2) <- Child/Sibling to previous parent (2, 3 are also considered a leaf)
#                                      /
#                                    (4) <- Leaf (4 is also a child from 2)
# A Binary Search Tree (BST) is a binary tree where the child Nodes are sorted in a way that when the child is bigger
# than the parent it goes on the right side and if its less then it goes on the left side. If one of the sides is
# already occupied by a child Node then we compare it with that same child node until there are free node space.
# Example:
#               (10)
#               /  \
#             (5)  (12)
#             / \   / \
#           (4)(6)(11)(15)
# BST Big O analysis:
# To search on the BST we use the equation 2^x-1 (this equation means all possible elements to search in a tree),
# where x is the number of steps that you go from the main parent to the child or child level you want to,
# 1 becomes irrelevant when the tree gets bigger.
# For example, based on previous BST if we want the get the value 6 we have 2^3
# the conclusion is that in a BST the time complexity is 2^x which equals O(log n), this is very efficient and is
# achieved usually by divide and conquer method. This is easy when using a perfect tree to calculate time complexity
# which is the best case scenario.
# What is the worst case? A straight line tree like this where the tree never forks:
#               (10)
#                  \
#                 (12)
#                    \
#                    (15)
# This is basically a LL and requires O(n) of time complexity
# For the methods: lookup(), insert(), remove() a BST will take time complexity of O(log n)
# In LL, lookup() and remove() requires O(n) because they need to loop the list, if you want to insert a node
# in a LL you use append() which is the fastest. We are assuming that lookup and remove are related to the value
# and not to the index, because by index yes it is O(1)
# Interview question: If we want a data structure that allows us to add data very quickly but retrieval speed is not
# very important, which data structure would you choose between BST or LL? R/ LL because append is O(1), if retrieval
# of the data is more important then BST.

# BST constructor
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# BST Class
class BST:
    def __init__(self):
        # In the past data structures we always initialize the structure with a value, but that is not
        # necessary we can also create an empty structure, let use try creating this time an empty tree when class is
        # BST is called
        # new_node = Node(value)
        # self.root = new_node
        # root is the pointer to the first value of BST
        self.root = None

    # Method that insert node into a BST and sort when comparing to the root node
    def insert(self, value):
        new_node = Node(value)
        temp = self.root
        if self.root is None:
            self.root = new_node
            return True
        else:
            while temp is not None:
                # Its very important that we compare the value and not the whole node
                if new_node.value == temp.value:
                    return False
                elif new_node.value < temp.value:
                    if temp.left is None:
                        temp.left = new_node
                        temp = None
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        temp = None
                    else:
                        temp = temp.right
            return True

    # Method contains search for the value we want in a BST and returns True if exist
    def contains(self, value):
        # This part is not necessary if we already assigning temp to self.root and the while is not None!
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        return False
    # This method search for the minimum value in any tree(root) or subtree(parent), argument is a current_node
    # It returns a Node, if the tree is with only root element it will always return the current_node
    def minimumValue(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    # Tree traversal. Allow us to convert a tree into a list. Two methods exist to travel a BST.
    # Method 1: Breadth First Search (BFS). We need two list, first list is queue, second list is the result list.
    # Basically the queue is created where the first element is the root (level 0) later we move it to results
    # then we add the left and right element (both level 1) of the root to the queue, then we move the first element
    # on queue to results and add his respective childs left and right (level 2), then we do the same with the right
    # element (level 1) until we have move all the elements from tree to temp and then to results. Remember the
    # important part is to manage the queue
    def BFS(self):
        queue = []
        results = []
        current_node = self.root
        # Remember to always initialize the queue with the root, if we don't the while loop will never run
        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        return results
    # Another traversal method: Depth First Search, this method has 3 types (Preorder, postorder and Inorder).
    # First way DFS PreOrder: We first add the root into results, then search for the root.left
    # if value exist we add it, keep going left and add value if exist, if we reach None then we go
    # 1 step back and check the right if it exist we add it and the look for left again, we repeat this until we go
    # back to root, we then go to root.right if exist we add it and then go to his left and keep doing it until
    # we go back to root again, return results and remember we use recursion to accomplish this
    def DFS_pre(self):
        results = []
        # We can create a sub function inside DFS_pre for our recursive method too

        def traversal(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return results
    # Second way DFS PostOrder: Follows the same traversal than pre order but we only add the value when we search in
    # the node that node.left and node.right are None or when we have already traversed that node
    def DFS_post(self):
        results = []
        # We can create a sub function inside DFS_pre for our recursive method too

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
            results.append(current_node.value)
        traversal(self.root)
        return results
    # Third way DFS InOrder: Follows the same traversal than pre order but we only add the value after we found that
    # the node.left value is None, then we go to Node.right, all the numbers are written in numerical order
    def DFS_in(self):
        results = []
        # We can create a sub function inside DFS_pre for our recursive method too

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)
        traversal(self.root)
        return results






