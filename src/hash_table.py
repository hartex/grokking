class HashTable:
    def __init__(self, load_factor=0.75, initial_capacity=20):
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
            array_under_index.append((key, value))
        else:
            self.inner_table[index] = [(key, value)]
        self.size += 1
        self.__increase_capacity()

    def pop(self, key):
        index = self.hash_function(key)
        array_under_index = self.inner_table[index]
        if array_under_index:
            for i in range(0, len(array_under_index)):
                array_key = array_under_index[i][0]
                if array_key == key:
                    self.size -= 1
                    return array_under_index.pop(i)

    def items(self):
        resulted_array = []
        for bucket in self.inner_table:
            if bucket:
                for item in bucket:
                    if item:
                        resulted_array.append(item)
        return resulted_array

    def __increase_capacity(self):
        if self.__should_increase_capacity():
            self.inner_table.extend([None] * len(self.inner_table))
            self.threshold = self.load_factor * len(self.inner_table)

    def __should_increase_capacity(self):
        return self.size >= self.threshold

    def __str__(self):
        return self.items().__str__()


# todo unit tests

instance = HashTable(initial_capacity=5)
instance.set('string', 1111)
instance.set('strin123g', 1000)
instance.set('stri123344ng', 1000)
instance.set('stri12334ng', 1000)
instance.set('stri1234ng', 1000)
instance.set('stri14ng', 1000)
instance.pop('stri12334ng')
instance.set('stri1244ng', 1000)

print(instance.size)
print(instance)
print(instance.get('string'))
