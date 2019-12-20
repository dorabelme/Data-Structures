class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        self._bubble_up(len(self.storage) - 1)

    def get_max(self):
        if self.get_size() >= 1:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def delete(self):
        if self.storage[0]:
            value = self.storage[0]

        if self.get_size() <= 1:
            self.storage = []
        else:
            self.storage[0] = self.storage.pop(self.get_size()-1)
            self._sift_down(0)
        return value

    def _bubble_up(self, index):
        while index > 0:
            parent = (index - 1) // 2

            if self.storage[index] > self.storage[parent]:
                self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
                index = parent
            else:
                break

    def _sift_down(self, index):
        while index < self.get_size():
            left = (2 * index) + 1 if (2 * index) + \
                1 < self.get_size() else index
            right = (2 * index) + 2 if (2 * index) + \
                2 < self.get_size() else index
            maxIndex = left if self.storage[left] > self.storage[right] else right

            if self.storage[index] < self.storage[maxIndex]:
                self.storage[index], self.storage[maxIndex] = self.storage[maxIndex], self.storage[index]
                index = maxIndex
            else:
                break
