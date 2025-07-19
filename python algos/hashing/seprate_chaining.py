# Hashing maps data to a specific index in a hash table, using a hash function
# achieves search, insert, and delete in O(1) time on average

# Hashing implementation based on chaining
# Method 1: no rehashing, fixed size array

class Simple_Hash:
    """
    Simple chaining implementation, no fixed size array
    Auxiliary space: O(1), no extra space is needed
    """

    def __init__(self, buckets: int):
        self.size = buckets
        self.hash_table = [[] for _ in range(self.size)]
    
    def hash_index(self, key: int) -> int:
        return key % self.size

    def insert_item(self, key: int):
        index = self.hash_index(key)
        self.hash_table[index].append(key)
    
    def remove_item(self, key: int):
        index = self.hash_index(key)
        if key in self.hash_table[index]:
            self.hash_table[index].remove(key)

    def display(self):
        for i in range(self.size):
            print(i, end = "")

            for key in self.hash_table[i]:
                print("->", key, end="")
            
            print()

class chaining_rehashing:
    """
    Hash table where number of buckets is not fixed, the hash table is adjusted
    when the load factor exceeds a threshold, 0.5 in this example

    Complexity:
    Rehashing has O(n) complexity
    Search O(n) complexity
    Auxiliary space: O(n)
    """

    def __init__(self, buckets: int):
        self.bucket_count = buckets
        self.num_elems = 0
        self.table = [[] for _ in range(self.bucket_count)]

    def hash_func(self, key: int):
        return key % self.bucket_count
    
    def get_load_factor(self):
        return self.num_elems / self.bucket_count
    
    def insert(self, key: int):
        while self.get_load_factor() > 0.5:
            self.rehash()
        
        index = self.hash_func(key)
        self.table[index].append(key)
        self.num_elems += 1
    
    def remove(self, key: int):
        index = self.hash_func(key)

        if key in self.table[index]:
            self.table[index].remove(key)
            self.num_elems -= 1

    def rehash(self):
        old_table = self.table
        self.bucket_count *= 2
        self.table = [[] for _ in range(self.bucket_count)]

        for bucket in old_table:
            for key in bucket:
                self.insert(key)
    
    def display(self):
        for i in range(self.bucket_count):
            print(i, end = "")
            for elem in self.table[i]:
                print("-->", elem, end = "")

            print()


if __name__ == "__main__":
    keys = [7, 18, 12, 25, 14]

    # table = Simple_Hash(len(keys))
    
    # for i in range(len(keys)):
    #     table.insert_item(keys[i])

    # table.display()

    table = chaining_rehashing(len(keys))
    for key in keys:
        table.insert(key)
    
    table.display()

        