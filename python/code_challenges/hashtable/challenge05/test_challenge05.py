import pytest
from challenge05 import array_intersection

def test_array_intersection():
    # Basic test case
    assert set(array_intersection([1, 2, 2, 1], [2, 2])) == {2}
    
    # Different sizes of arrays
    assert set(array_intersection([4, 9, 5], [9, 4, 9, 8, 4])) == {9, 4}
    
    # No intersection
    assert set(array_intersection([1, 2, 3], [4, 5, 6])) == set()
    
    # One empty array
    assert set(array_intersection([], [1, 2, 3])) == set()
    assert set(array_intersection([1, 2, 3], [])) == set()
    
    # Both empty arrays
    assert set(array_intersection([], [])) == set()
    
    # All elements intersect
    assert set(array_intersection([1, 2, 3], [1, 2, 3])) == {1, 2, 3}
    
    # Repeated elements in one array
    assert set(array_intersection([1, 1, 1, 1], [1, 1])) == {1}
    
    # Repeated elements in both arrays
    assert set(array_intersection([1, 2, 2, 3, 3, 3], [3, 3, 2, 2, 1, 1])) == {1, 2, 3}
    
    # Large arrays with intersection
    assert set(array_intersection(list(range(1000)), list(range(500, 1500)))) == set(range(500, 1000))
    
    # Large arrays with no intersection
    assert set(array_intersection(list(range(1000)), list(range(1000, 2000)))) == set()

if __name__ == "__main__":
    pytest.main()
