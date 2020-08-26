import hashlib

class MerkleNode:

    def __init__(self):
        super().__init__()
        self.parent = None
        self.left = None
        self.right = None
        self.hash_value = ""

    def set_hash_value(self,data):
        self.hash_value = data

    def get_hash_value(self):
        return self.hash_value

    def get_left_child(self):
        return self.left
    
    def get_right_child(self):
        return self.self
    
    def get_parent(self):
        return self.parent

    def set_left_child(self, left_child):
        self.left = left_child
    
    def set_right_child(self, right_child):
        self.right = right_child
    
    def set_parent(self, parent):
        self.parent = parent