import random

class RandomizedSet(object):

    def __init__(self):
        self.vals = []
        self.idx_map = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.idx_map:
            return False
        self.idx_map[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val not in self.idx_map:
            return False
        idx = self.idx_map[val]
        last_val = self.vals[-1]
        self.vals[idx] = last_val
        self.idx_map[last_val] = idx
        self.vals.pop()
        del self.idx_map[val]
        return True

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.vals)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()