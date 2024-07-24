# Write here the code challenge solution

from hash import HashTable

class has03:
    def solution(self,arr):
        table = HashTable()
        dublicate = HashTable()

        for num in arr:
            if table.contains(num):
                # table.delete(num)
                dublicate.set(num,1)
            else:
                table.set(num,1)
        
        unique_sum = 0
        for key in table:
            if key.isdigit() and not dublicate.contains(key):
                print(key)
                unique_sum += int(key) 

        return unique_sum
    

solution_instance = has03()
test_array = ["1", "2", "3","2","1"]
print("Sum of unique elements:", solution_instance.solution(test_array)) # output 3

hash_table = HashTable(size=10)
hash_table.set("apple", 1)
hash_table.set("banana", 2)
hash_table.set("orange", 3)
hash_table.set("grape", 4)
# hash_table.set("lemon", 5)
# hash_table.set("pear", 6)
# hash_table.set("lime", 7)
# print("\nHash Table contents:")
# print(hash_table)  # Print hash table using the __


