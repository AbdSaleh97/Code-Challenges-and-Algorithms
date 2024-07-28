import pytest
from challenge04 import sort_people

def test_sort_people_example():
    # Test with example input
    names = ["Alice", "Bob", "Bob"]
    heights = [155, 185, 150]
    expected_output = ["Bob", "Alice", "Bob"]
    assert sort_people(names, heights) == expected_output

def test_sort_people():
    names = ["Alice", "Bob", "Charlie", "David"]
    heights = [165, 160, 180, 150]
    expected_output = ["Charlie", "Alice", "Bob", "David"]
    assert sort_people(names, heights) == expected_output

def test_sort_people_single_person():
    # Test with a single person
    names = ["Alice"]
    heights = [170]
    expected_output = ["Alice"]
    assert sort_people(names, heights) == expected_output

def test_sort_people_empty_lists():
    # Test with empty lists
    names = []
    heights = []
    expected_output = []
    assert sort_people(names, heights) == expected_output

def test_sort_people_varied_heights():
    # Test with varied heights
    names = ["John", "Doe", "Smith", "Jane"]
    heights = [190, 150, 180, 160]
    expected_output = ["John", "Smith", "Jane", "Doe"]
    assert sort_people(names, heights) == expected_output

def test_sort_people():
    names = ["Anna", "Bella", "Cara"]
    heights = [180, 160, 150]
    expected_output = ["Anna", "Bella", "Cara"]  # Order remains the same
    assert sort_people(names, heights) == expected_output

if __name__ == "__main__":
    pytest.main()
