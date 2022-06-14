# A graph is a data structure that has a 'Vertex' or a Node, it can have multiple connections to another Vertex using
# an 'Edge', edge can be bidirectional or not. So basically a tree is like a graph with unidirectional edges and each
# nodes can only have two child instead of 'n' childs, and a LL is a tree with only 1 child per parent.
# Each edges also can have weights so the Vertex can decide which is the 'best route'
# Diagram sample: Vertex 1 has an unidirectional edge with Vertex 3,4 and 5, 4 and 5 has bidirectional edge
#           (1)---->(3)
#            |  \
#            |   \
#            v    v
#           (4)---(5)
# What is an adjacency matrix? Is a matrix that shows the connection weight between Vertex, some considerations:
# If all the vertex are not connecting to themselves then we will have a 45 degree angle oj just 0 in the matrix
# If every edge is bidirectional then we will have a mirror image of the sames values in the matrix separated
# by the 45 degree zeroes (assuming the vertex are not connecting to themselves)
# The value in each adjacency matrix bracket is based on the weight of the edge, if no weight is shown then is 1
# Example, lets create an adjacency matrix for the below diagram, all edges have int weights, and some are bi other uni
#       (a)----->(b)
#        |   3    |
#      1 |      2 |
#        v   4    |
#       (c)------(d)
# The adjacency matrix would be, note the 45 degree zeroes, and because the edges are not all bidirectional
# then there is no mirror from each side.
#           a  b  c  d
#        a  0  3  1  0
#        b  0  0  0  2
#        c  0  0  0  4
#        d  0  2  4  0
# Based on previous diagram we can also show another representation, the adjacency list (basically a dict), like this:
# adjacency_list = {
#                       'a':['b','c'],
#                       'b':['d'],
#                       'c':['d'],
#                       'b':['b','c']
#                  }
# Graph Big O analysis (V is vertex and E is edges):
# --Add vertex--: From the space complexity, an adjacency matrix is O(|V|^2) and for adjacency list is O(|V|+|E|),
# the reason is that in the matrix you need to fill the information for every vertex (connected or unconnected), thus
# requires to rewrite the matrix, in the list you only add the key and value info, for example imagine if we need to
# add another vertex f(assuming no connections) to the previous diagram, in the matrix we need to add all the rows
# and column necessary and filed with zeroes to represent the relationship between Vertex(which is basically O(n^2)),
# in the list we just add 'f':[], this is O(1).
# --Add edge--: If we just need to add the connections, for both matrix and list is only O(1)
# --Remove edge--: In the matrix case we just set the value of the edges we require to 0 accessing the matrix is quick,
# you just provide de index id by the vertex value, in the list is more difficult you don't have index, you need to
# go to all the keys and iterate all the connected vertex(which are the values of the key) until you found the value and
# remove them, because of the iteration then its O(|E|)
# --Remove vertex--: In the matrix we need to rewrite the entire matrix to remove the vertex, this is O(|V|^2), the
# list will only require to loop trougth all the available vertix and remove it, the loop in the values of each key and
# remove any vertex connection, this is O(|V|+|E|)

# Create Add Vertex method in class graph, we use the adjacency list because is more efficient.
# We dont need to create a Node class like in previous Data Struct because this doesnt have pointers, its basically a
# dict or hash table that we manage the vertex values(keys) with each of their edges(values)

class Graph:
    def __init__(self):
        # Create empty dict
        self.adj_list = {}
    # Method to add vertex
    def add_vertex(self, vertex):
        # We need to make sure that we don't have duplicates vertex in the graph
        if vertex not in self.adj_list.keys():
            # We create an empty list inside the value for key vertex
            self.adj_list[vertex] = []
            return True
        return False
    # Printing graph for testing purposes
    def print_graph(self):
        temp = []
        print('My Graph:\n')
        for vertex in self.adj_list:
            temp_str = str(self.adj_list[vertex])
            temp.append(vertex+':'+temp_str)
            print(vertex, ':', self.adj_list[vertex])
        return temp

    # Method to add edge, this method will automatically creates a bidirectional edge
    def add_edge(self, vertexs, vertexd):
        # We need to make sure that vertexS and vertexD already exist in the graph
        if vertexs in self.adj_list.keys() and vertexd in self.adj_list.keys():
            # Remember we want to append vertexd for future new values, not assign them
            self.adj_list[vertexs].append(vertexd)
            self.adj_list[vertexd].append(vertexs)
            return True
        return False
    # Method to remove edge, this method will automatically remove the bidirectional edge given vertex source and dest
    def remove_edge(self, vertexs, vertexd):
        # We need to make sure that vertexS and vertexD already exist in the graph
        if vertexs in self.adj_list.keys() and vertexd in self.adj_list.keys():
            # Second one with remove, we need to ignore the ValueError which comes when we try to remove
            # a edge that does not exist
            try:
                self.adj_list[vertexs].remove(vertexd)
                self.adj_list[vertexd].remove(vertexs)
            except ValueError:
                pass
            return True
        return False
    # Method to remove vertex, this method will automatically remove the index
    def remove_vertex(self, vertexs):
        # We need to make sure that vertexS exist in the graph
        if vertexs in self.adj_list.keys():
            # This is the efficient method, fist we found the values in the vertex we want to remove, logically
            # all those elements are also vertex that contains the value we want to remove too
            for i in self.adj_list[vertexs]:
                self.adj_list[i].remove(vertexs)
            del self.adj_list[vertexs]
            return True
        return False
