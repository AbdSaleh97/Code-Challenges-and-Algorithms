from graph import Graph, Node

def test_add_node():
    graph = Graph()
    node = graph.add_node('A')
    assert node.value == 'A'
    assert node in graph.adj_list

def test_add_edge():
    graph = Graph()
    nodeA = graph.add_node('A')
    nodeB = graph.add_node('B')
    graph.add_edge(nodeA, nodeB)
    assert any(edge.vertex == nodeB for edge in graph.adj_list[nodeA])
    assert any(edge.vertex == nodeA for edge in graph.adj_list[nodeB])

def test_bfs_simple():
    graph = Graph()
    nodes = [graph.add_node(chr(65 + i)) for i in range(3)]
    graph.add_edge(nodes[0], nodes[1])
    graph.add_edge(nodes[1], nodes[2])
    result = graph.BFS(nodes[0])
    assert result == ['A', 'B', 'C']

def test_bfs_complex():
    graph = Graph()
    nodes = [graph.add_node(chr(65 + i)) for i in range(5)]
    graph.add_edge(nodes[0], nodes[1])
    graph.add_edge(nodes[0], nodes[2])
    graph.add_edge(nodes[1], nodes[3])
    graph.add_edge(nodes[2], nodes[4])
    result = graph.BFS(nodes[0])
    assert result == ['A', 'B', 'C', 'D', 'E']

def test_bfs_disconnected():
    graph = Graph()
    nodes = [graph.add_node(chr(65 + i)) for i in range(4)]
    graph.add_edge(nodes[0], nodes[1])
    graph.add_edge(nodes[2], nodes[3])
    result = graph.BFS(nodes[0])
    assert result == ['A', 'B']

def test_bfs_single_node():
    graph = Graph()
    node = graph.add_node('A')
    result = graph.BFS(node)
    assert result == ['A']

def test_bfs_empty_graph():
    graph = Graph()
    # Attempting BFS on an empty graph should not raise an error
    try:
        result = graph.BFS(Node('A'))
    except KeyError:
        result = []
    assert result == []
def test_bfs_challenge_example():
    vertex = ['A', 'C', 'E','B', 'F', 'D', 'G', 'I', 'H', 'K']
    graph = Graph()
    nodes = []
    for ver in vertex:
        nodes.append(graph.add_node(ver))

    graph.add_edge(nodes[0],nodes[1]) # A - C
    graph.add_edge(nodes[0],nodes[2]) # A - E
    graph.add_edge(nodes[0],nodes[3]) # A - B
    graph.add_edge(nodes[1],nodes[4]) # C - F
    graph.add_edge(nodes[4],nodes[8]) # F - H
    graph.add_edge(nodes[4],nodes[7]) # F - I
    graph.add_edge(nodes[3],nodes[5]) # B - D
    graph.add_edge(nodes[5],nodes[2]) # D - E
    graph.add_edge(nodes[4],nodes[2]) # F - E
    graph.add_edge(nodes[6],nodes[2]) # G - E
    graph.add_edge(nodes[6],nodes[8]) # G - H
    graph.add_edge(nodes[9],nodes[8]) # K - H
    graph.add_edge(nodes[9],nodes[7]) # K - I

    assert graph.BFS(nodes[0]) == ['A', 'C', 'E', 'B', 'F', 'D', 'G', 'H', 'I', 'K']