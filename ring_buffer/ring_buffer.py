class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.storage = []
        self.oldest_index = 0

    def append(self, item):
        if self.size == self.capacity:
            self.storage[self.oldest_index] = item
            capacity = self.capacity - 1
            if self.oldest_index < capacity:
                self.oldest_index += 1 
            else: self.oldest_index = 0

        else:
            self.storage.append(item)
            self.size += 1

    def get(self):
        return self.storage
        