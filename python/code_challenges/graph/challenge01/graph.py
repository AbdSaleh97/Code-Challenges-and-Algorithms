class Node:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __eq__(self, other):
        return self.value == other.value

    def __hash__(self):
        return hash(self.value)

class Edge:
    def __init__(self, vertex, weight=0):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_node(self, value):
        node = Node(value)
        self.adj_list[node] = []
        return node
    
    def add_edge(self, node1, node2, weight=0):
        if node1 not in self.adj_list or node2 not in self.adj_list:
            return "Node does not exist"
        
        edge1 = Edge(node2, weight)
        self.adj_list[node1].append(edge1)

        edge2 = Edge(node1, weight)
        self.adj_list[node2].append(edge2)

    def BFS(self, root):
        queue = []  
        visited = set()  
        result = []  # List to collect node values
        queue.append(root)
        visited.add(root)

        while queue:
            current = queue.pop(0)  
            result.append(current.value)  # Append the current node's value to the result list

            neib_list = self.adj_list[current]
            for edge in neib_list:
                if edge.vertex not in visited:
                    queue.append(edge.vertex)
                    visited.add(edge.vertex)

        return result  # Return the list of node values

    def __str__(self):
        output = ''
        for vertex in self.adj_list:
            output += f'{vertex.value} -> '
            for edge in self.adj_list[vertex]:
                output += f'{edge.vertex.value} ({edge.weight}) ------> ' 
            output += '\n'
        return output

if __name__ == "__main__":
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    graph = Graph()
    nodes = []
    for ver in vertex:
        nodes.append(graph.add_node(ver))

    graph.add_edge(nodes[0], nodes[1])  # A - B
    graph.add_edge(nodes[0], nodes[2])  # A - C
    graph.add_edge(nodes[1], nodes[3])  # B - D
    graph.add_edge(nodes[1], nodes[4])  # B - E
    graph.add_edge(nodes[2], nodes[5])  # C - F
    graph.add_edge(nodes[2], nodes[6])  # C - G
    graph.add_edge(nodes[3], nodes[7])  # D - H
    graph.add_edge(nodes[4], nodes[8])  # E - I
    graph.add_edge(nodes[5], nodes[9])  # F - J
    graph.add_edge(nodes[6], nodes[9])  # G - J
    graph.add_edge(nodes[7], nodes[8])  # H - I

    print(graph)
    graph.BFS(nodes[0])