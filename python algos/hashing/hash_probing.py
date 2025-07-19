class hashNode:
    
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value

class hashMap:
    """
    Insertion: O(n), worst case where all elements have collided, need to
    insert by checking free space one by one
    """
    def __init__(self):
        self.capacity = 20
        self.size = 0
        self.arr = [None] * self.capacity
        self.dummy = hashNode(-1, -1)
    
    def hash_func(self, key):
        return key % self.capacity

    def insertNode(self, key, value):
        temp = hashNode(key, value)
        hashIndex = self.hash_func(key)

        while self.arr[hashIndex] is not None:
            hashIndex = (hashIndex+1) % self.capacity
        
        if self.arr[hashIndex] is None or \
        self.arr[hashIndex].key == -1:
            self.size += 1
        self.arr[hashIndex] = temp
    
    def deleteNode(self, key):
        hashIndex = self.hash_func(key)

        while self.arr[hashIndex] is not None:
            if self.arr[hashIndex].key == key:
                temp = self.arr[hashIndex]
                self.arr[hashIndex] = self.dummy
                self.size -= 1
                return temp.value
            
            hashIndex = (hashIndex + 1) % self.capacity
        return -1
    
    def get(self, key):
        hashIndex = self.hash_func(key)
        counter = 0

        while self.arr[hashIndex] is not None:
            if counter > self.capacity:
                return -1
            if self.arr[hashIndex].key == key:
                return self.arr[hashIndex].value
            hashIndex = (hashIndex + 1) % self.capacity
            counter += 1
        return -1
    
    def display(self):
        for node in self.arr:
            if node is not None and node.key != -1:
                print(f"{node.key}: {node.value}")
    
    def sizeMap(self):
        return self.size
    

if __name__ == "__main__":
    h = hashMap()
    h.insertNode(1,1)
    h.insertNode(2,2)
    h.insertNode(2,3)
    h.insertNode(2,4)

    h.display()
    print(" ")
    h.deleteNode(2)
    h.display()