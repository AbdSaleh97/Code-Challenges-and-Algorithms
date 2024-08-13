from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = defaultdict(list)  # Adjacency list
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def dfs(self, v, visited):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs(i, visited)
    
    def is_strongly_connected(self):
        for i in range(self.V):
            visited = [False] * self.V
            self.dfs(i, visited)
            
            # If DFS didn't visit all vertices, return False
            if any(not visited[j] for j in range(self.V)):
                return False
        
        return True

# Example usage:
numbers = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [1, 7], [7, 3]]
g = Graph(8)  # 8 vertices (0 to 7)
for u, v in numbers:
    g.add_edge(u, v)

print("Strongly connected" if g.is_strongly_connected() else "Not strongly connected")
