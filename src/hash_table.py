class HashTable:
    def __init__(self, load_factor=0.7, initial_capacity=20):
        self.load_factor = load_factor
        self.inner_table = [None] * initial_capacity
        self.threshold = load_factor * initial_capacity
        self.size = 0

    def get(self, key):
        return 1

    def set(self, key, value):
        # get hash
        return value

    def delete(self, key):
        return key
