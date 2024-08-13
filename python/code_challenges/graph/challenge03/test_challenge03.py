# Write your test here
import pytest
from challenge03 import Graph  # Assuming your Graph class is in a file named graph.py

@pytest.mark.parametrize("vertices, edges, expected", [
    (8, [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 4], [1, 7], [7, 3]], False),  # Example 1: Not strongly connected
    (5, [[1, 2], [1, 0], [0, 4], [4, 3], [3, 2], [3, 1], [2, 1], [2, 4]], True),   # Example 2: Strongly connected
    (4, [[0, 1], [1, 2], [2, 3], [3, 0]], True),                                    # Simple cycle: Strongly connected
    (3, [[0, 1], [1, 2]], False),                                                   # Not a cycle: Not strongly connected
    (1, [], True),                                                                  # Single vertex, no edges: Strongly connected
    (6, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0]], True),                    # Simple cycle with 6 vertices: Strongly connected
    (6, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]], False),                   # Two separate cycles: Not strongly connected
    (7, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 6], [6, 3]], False)            # Disconnected components: Not strongly connected
])
def test_is_strongly_connected(vertices, edges, expected):
    g = Graph(vertices)
    for u, v in edges:
        g.add_edge(u, v)
    assert g.is_strongly_connected() == expected
