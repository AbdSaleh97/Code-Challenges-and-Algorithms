# Write your test here
import pytest
from hash import HashTable
from challenge03 import has03  # Adjust this import based on where you have defined the has03 class

def test_solution_unique_elements():
    solution_instance = has03()
    test_array = ["1", "2", "2", "1", "3", "2", "2", "3", "8"]
    result = solution_instance.solution(test_array)
    assert result == 8, "Test case failed: The sum of unique elements is incorrect."

def test_solution_no_duplicates():
    solution_instance = has03()
    test_array = ["5", "10", "15", "20"]
    result = solution_instance.solution(test_array)
    assert result == 5 + 10 + 15 + 20, "Test case failed: The sum of unique elements with no duplicates is incorrect."

def test_solution_all_duplicates():
    solution_instance = has03()
    test_array = ["5", "5", "5", "5"]
    result = solution_instance.solution(test_array)
    assert result == 0, "Test case failed: The sum of unique elements when all elements are duplicates should be 0."

def test_solution_empty_array():
    solution_instance = has03()
    test_array = []
    result = solution_instance.solution(test_array)
    assert result == 0

def test_solution_mixed_elements():
    solution_instance = has03()
    test_array = ["1", "2", "3" ,"3", "4"]
    result = solution_instance.solution(test_array)
    assert result == 1 + 2 + 4, "Test case failed: The sum of unique numeric elements is incorrect."

def test_solution_no_numeric_elements():
    solution_instance = has03()
    test_array = ["1","2","3","3","1"]
    result = solution_instance.solution(test_array)
    assert result == 2
