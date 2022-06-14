# Pytest Framework for testing Graph Class and methods
# There is a fixture after each test is run that initialize the test again with an empty graph
class TestGraph:
    # Add vertex A with empty edges
    def test_addVertex(self):
        self.my_graph.add_vertex('A')
        a = self.my_graph.print_graph()
        assert a == ['A:[]']
    # Add vertex A and B and make a cnx from A to B
    def test_addEdge(self):
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_edge('A', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['B']", "B:['A']"]
    # Add vertex A and B and make a cnx from A to B, when A and B dont exist
    def test_addEdge_noVertex(self):
        a = self.my_graph.add_edge('A', 'B')
        assert a is False
    # Add vertex A and B and make a cnx from A to B, when only B exist
    def test_addEdge_1Vertex(self):
        self.my_graph.add_vertex('B')
        a = self.my_graph.add_edge('A', 'B')
        assert a is False
    # Remove edge between A and B
    def test_removeEdge(self):
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_edge('A', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['B']", "B:['A']"]
        self.my_graph.remove_edge('A', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:[]", "B:[]"]
    # Remove edge between A and B with multiple vertex, then remove B and C cnx
    def test_removeEdge_nVertex(self):
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_edge('A', 'B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_edge('A', 'C')
        self.my_graph.add_edge('C', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['B', 'C']", "B:['A', 'C']", "C:['A', 'B']", "D:[]"]
        self.my_graph.remove_edge('A', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['C']", "B:['C']", "C:['A', 'B']", "D:[]"]
        self.my_graph.remove_edge('C', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['C']", "B:[]", "C:['A']", "D:[]"]
    # Remove edge between A and B when there is no edge available
    def test_addEdge_2Vertex_noEdge(self):
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('A')
        a = self.my_graph.remove_edge('A', 'B')
        assert a is True
        b = self.my_graph.print_graph()
        assert b == ["B:[]", "A:[]"]
    # Remove vertex that exist
    def test_removeVertext(self):
        self.my_graph.add_vertex('B')
        self.my_graph.add_vertex('A')
        self.my_graph.remove_vertex('A')
        b = self.my_graph.print_graph()
        assert b == ["B:[]"]
    # Remove vertex that exist with multiple n vertex and edges
    def test_removeVertex_nVertex_nEdges(self):
        self.my_graph.add_vertex('A')
        self.my_graph.add_vertex('B')
        self.my_graph.add_edge('A', 'B')
        self.my_graph.add_vertex('C')
        self.my_graph.add_vertex('D')
        self.my_graph.add_edge('A', 'C')
        self.my_graph.add_edge('C', 'B')
        b = self.my_graph.print_graph()
        assert b == ["A:['B', 'C']", "B:['A', 'C']", "C:['A', 'B']", "D:[]"]
        self.my_graph.remove_vertex('C')
        c = self.my_graph.print_graph()
        print("Current graph:")
        print(c)
        assert c == ["A:['B']", "B:['A']", "D:[]"]
    # Remove vertex that in a empty graph
    def test_removeVertext_empty(self):
        a = self.my_graph.remove_vertex('A')
        b = self.my_graph.print_graph()
        assert a is False
        assert b == []

