import random

class RandomizedSet:

    def __init__(self):
        self.items = dict()
        self.item_list = []
        self.i = 0

    def insert(self, val: int) -> bool:
        if val in self.items:
            return False
        
        self.items[val] = self.i
        self.item_list.append(val)
        self.i += 1
        
        return True
        

    def remove(self, val: int) -> bool:
        if val not in self.items:
            return False

        deleted_idx = self.items[val]
            
        if self.i -1 != deleted_idx:
            last_item = self.item_list[self.i - 1]
            self.item_list[deleted_idx] = last_item
            self.items[last_item] = deleted_idx
        
        del self.items[val]
        del self.item_list[self.i - 1]
        self.i -= 1
        
        return True
        

    def getRandom(self) -> int:
        random_idx = random.randrange(0, self.i)
        return self.item_list[random_idx]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()