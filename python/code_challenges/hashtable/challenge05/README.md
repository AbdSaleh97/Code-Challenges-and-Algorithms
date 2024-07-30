# Hash Table:

## Challenge05 - Arrays Intersection:

 Write a function that it takes two arrays of integers, Return array of their intersection, Each element in the result must be unique and you may return the result in any order.
<br>

&nbsp;

## Example :
![](/assets/hashTable/arrayIntersection.jpg)

Input
<pre>arr1 = ["1","2","2","1"], arr2 = [2,2]</pre>


Output:
```python
[2]
```
<br>

## Instruction:

### Language: `JavaScript`:

* Create a branch called `arrayIntersection`.
* Run this command to pull the code challenge question: `npm run pull-challenge hashtable 05`
* Navigate to the challenge folder: `code-challenges/hashtable/challenge05`
* Write your solution in `challenge05.js` file.
* Write your tests in `challenge05.test.js` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `npm test`

## Language: `Python`:

* Create a branch called `arrayIntersection`.
* Run this command to pull the code challenge question: `python pull.py hashtable 05`
* Navigate to the challenge folder: `code_challenges/hashtable/challenge05`
* Write your solution in `challenge05.py` file.
* Write your tests in `test_challenge05.py` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `pytest`

## Language: `Java`:

* Create a branch called `arrayIntersection`.
* Run this command to pull the code challenge question: `npm run pull-challenge hashtable 05`
* Navigate to the challenge folder: `code-challenges/hashtable/challenge05`
* Write your solution in `App.java` file.
* Write your tests in `AppTest.java` file.
* Document your work along with an image of your whiteboard in the `whiteboard.md` file.
* To run your test: `gradle test`

## Submission:
* ACP your work once you are done.
* Create a pull request from your branch to the `main` branch
* Copy the link to your open pull request and paste it into the assignment submission field.
* Leave a description of how long this assignment took you in the comments box.
* Add any additional comments to your grader about your process or any difficulties you may have had with the assignment.
* Merge your branch into main, and delete your branch (don't worry, the PR link will still work).




### Whiteboard Explanation

#### 1. Problem Domain
The task is to find the intersection of two arrays of integers. Each element in the result must be unique, and the result can be returned in any order. We will solve this using a hash table to ensure efficient lookup and insertion operations.

#### 2. Algorithms
We use a hash table to track the elements in the first array and then check for their presence in the second array. The hash table will handle collisions using chaining with linked lists.

**Steps:**
1. Initialize a hash table.
2. Insert elements from the first array into the hash table.
3. For each element in the second array, check if it exists in the hash table:
    - If it does, add it to the result and remove it from the hash table to ensure uniqueness.
4. Return the result.

# 3. Pseudo Code
### Insert elements of the first array into the hash table
for num in arr1:
    if hash_table.search(num) is None:
        hash_table.insert(num, True)

## Initialize result array
result = []

## Check elements of the second array in the hash table
for num in arr2:
    if hash_table.search(num) is not None:
        result.append(num)
        hash_table.delete(num)  # Ensure each element in the result is unique

return result

