from linked import LinkedList
class HashTable:
    def __init__(self,size=100) -> None:
        self.size = size
        self.map = [None]*size
    def custom_hash(self,key):
        sum = 0
        for char in key:
            sum += ord(char)
        hash = sum * 1997 /2 + 4014
        return int(hash % self.size)

    def set(self, key ,value):
        hashed_key = self.custom_hash(key)
        
        if not self.map[hashed_key]: # if bucket empty
            self.map[hashed_key] = [key,value]
        else:
            if isinstance(self.map[hashed_key], LinkedList): # if bucket is not empty & is already a linked list
                self.map[hashed_key].push([key,value])
            else: # if bucket is not empty but it has only one element in the bucket, start chaining
                temp = self.map[hashed_key]
                list = LinkedList()
                list.push(temp)
                self.map[hashed_key] = list
                list.push([key,value])

    def contains(self, key):
        hashed_key = self.custom_hash(key)
        bucket = self.map[hashed_key]
        
        if bucket is None:
            return False
        if isinstance(bucket, LinkedList):
            current = bucket.head
            while current:
                if current.value[0] == key:
                    return True
                current = current.next
        else:
            if bucket[0] == key:
                return True
        return False
    def delete(self,key):
        hashed_key = self.custom_hash(key)
        bucket = self.map[hashed_key]

        if bucket is None:
            return False
        if isinstance(bucket, LinkedList):
            current = bucket.head
            while current:
                if current.value[0] == key:
                    bucket.remove(current.value)
                    return True
                current = current.next
        else:
            if bucket[0] == key:
                self.map[hashed_key] = None
                return True
            

    def __iter__(self):
        for bucket in self.map:
            if bucket:
                if isinstance(bucket, LinkedList):
                    current = bucket.head
                    while current:
                        yield current.value[0]
                        current = current.next
                else:
                    yield bucket[0]
            
    def __str__(self):
        result = []
        for i, bucket in enumerate(self.map):
            if bucket is None:
                result.append(f"Bucket {i}: Empty")
            elif isinstance(bucket, LinkedList):
                bucket_contents = []
                current = bucket.head
                while current:
                    bucket_contents.append(f"{current.value[0]}:{current.value[1]}")
                    current = current.next
                result.append(f"Bucket {i}: {' -> '.join(bucket_contents)}")
            else:
                result.append(f"Bucket {i}: {bucket[0]}:{bucket[1]}")
        return "\n".join(result)