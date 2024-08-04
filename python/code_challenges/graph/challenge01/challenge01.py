# Write here the code challenge solution
from graph import Graph
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

print(graph.__str__())


print(graph.BFS(nodes[0])) # root node 'A'














