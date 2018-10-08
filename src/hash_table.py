class HashTable:
    def __init__(self, load_factor=0.7, initial_capacity=20):
        self.load_factor = load_factor
        self.inner_table = [None] * initial_capacity
        self.threshold = load_factor * initial_capacity
        self.size = 0

    def hash_function(self, key_str):
        return sum([ord(c) for c in key_str]) % len(self.inner_table)

    def get(self, key):
        index = self.hash_function(key)
        array_under_index = self.inner_table[index]
        if array_under_index:
            for i in array_under_index:
                if i[0] == key:
                    return i[1]
        return None

    def set(self, key, value):
        index = self.hash_function(key)
        array_under_index = self.inner_table[index]
        if array_under_index:
            array_under_index.push((key, value))
        else:
            self.inner_table[index] = [(key, value)]
        self.size += 1

    def delete(self, key):
        index = self.hash_function(key)
        array_under_index = self.inner_table[index]
        if array_under_index:
            for i in array_under_index:
                if i[0] == key:
                    array_under_index[i] = None
                    break


instance = HashTable()
instance.set('string', 1000)
instance.set('strin123g', 1000)
instance.set('stri123344ng', 1000)
instance.delete('string')
instance.set('stri1244ng', 1000)

print(instance.get('string'))
