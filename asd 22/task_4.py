class aBST:

    def __init__(self, depth):
        tree_size = (2 ** (depth+1)) - 1
        self.Tree = [None] * tree_size
        self.depth = depth
	
    def FindKeyIndex(self, key):
        if self.Tree[0] is None:
            return None
        idx = 0
        while idx < len(self.Tree):
            if self.Tree[idx] is None:
                return -idx
            elif self.Tree[idx] == key:
                return idx
            elif key < self.Tree[idx]:
                idx = 2 * idx + 1
            else:
                idx = 2 * idx + 2
        return None
	
    def AddKey(self, key):
        if self.Tree[0] is None:
            self.Tree[0] = key
            return 0
        idx = 0
        while idx < len(self.Tree):
            if self.Tree[idx] is None:
                self.Tree[idx] = key
                return idx
            elif self.Tree[idx] == key:
                return idx
            elif key < self.Tree[idx]:
                idx = 2 * idx + 1
            else:
                idx = 2 * idx + 2
        return -1; 
        