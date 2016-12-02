class HashTable:
    def __init__(self):
        self.size = 11
        self.keys = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value, size):
        # calculate hash
        hash_key = self.calculate_hash(key, size)
        store = False
        while not store:
            current_hash_key = hash_key
            if self.keys[current_hash_key] == None:
                self.put_key(current_hash_key, key)
                self.put_data(current_hash_key, value)
                store = True
            elif self.keys[current_hash_key] != None:
                # if collision, re calculate hash
                hash_key = self.recalculate_hash(current_hash_key, size)


    def put_key(self, hash_key, key):
        self.keys[hash_key] = key

    def put_data(self, hash_key, value):
        self.data[hash_key] = value

    def calculate_hash(self, key, size):
        hash_key = key % size
        return hash_key

    def recalculate_hash(self, old_hash, size):
        new_hash_key = (old_hash + 1) % size
        return new_hash_key

    def get_value(self, key, size):
        hash_key = self.calculate_hash(key, size)
        if self.keys[hash_key] != None:
            return self.data[hash_key]

    def __getitem__(self, key):
        return self.get_value(key, self.size)

    def __setitem__(self, key, value):
        self.put(key, value, self.size)

if __name__ == '__main__':
    table = HashTable()
    table[54] = 'cat'
    table[26] = 'dog'
    table[93] = 'lion'
    table[17] = "tiger"
    table[77] = "bird"
    table[44] = "goat"
    table[55] = "pig"
    table[20] = "chicken"
    table[22] = 'shark'
    table[33] = 'svin'

    print(table.keys)
    print(table.data)

# [77,     44,     55,    None,  26,    93,    17,      None, None, 20,        54]
# ['bird', 'goat', 'pig', None, 'dog', 'lion', 'tiger', None, None, 'chicken', 'cat']

# [77, 44, 55, 22, 26, 93, 17, 33, None, 20, 54]
# ['bird', 'goat', 'pig', 'shark', 'dog', 'lion', 'tiger', 'svin', None, 'chicken', 'cat']