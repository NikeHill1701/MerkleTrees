import os
import math
import hashlib
from MerkleNode import MerkleNode

class MerkleTree:

    def __init__(self):
        super().__init__()
        self.count_merkle_nodes = 0
        self.merkle_root = None
    
    def get_merkle_node(self,data):

        merkle_node = MerkleNode()
        hash_value = hashlib.sha256(data).hexdigest()
        merkle_node.set_hash_value(hash_value)
        self.count_merkle_nodes += 1

        return merkle_node

    def join_merkle_roots(self,root1: MerkleNode(), root2: MerkleNode()):

        s = root1.get_hash_value() + root2.get_hash_value()
        new_root = self.get_merkle_node(s.encode())
        
        new_root.set_left_child(root1)
        new_root.set_right_child(root2)

        root1.set_parent(new_root)
        root2.set_parent(new_root)

        return new_root

    def construct_merkle_tree(self,data):

        n = len(data)
        if n == 1:
            return self.get_merkle_node(data[0])

        k = math.floor(math.log2(n))
        k = pow(2,k)
        if k == n:
            k = n // 2

        merkle_root1 = self.construct_merkle_tree(data[:k])
        merkle_root2 = self.construct_merkle_tree(data[k:n])

        merkle_root = self.join_merkle_roots(merkle_root1, merkle_root2)

        self.merkle_root = merkle_root

        return merkle_root

def divide_file_into_blocks(file,block_size):

    block_list = []

    with open(file, 'rb') as f:
        block = f.read(block_size)
        while block:
            print("Block: ", block)
            block_list.append(block)
            block = f.read(block_size)
    
    return block_list

def bfs(root):
    """
        TODO: Write code to traverse the tree
        and print the hash values stored in each node in each level.
    """
    print(root.get_hash_value())
    
file_path = "/home/nikhil/Desktop/btp/basic.py"
block_list = divide_file_into_blocks(file_path,50)

print(len(block_list))

mTree = MerkleTree()
merkle_root = mTree.construct_merkle_tree(block_list)

print(merkle_root)
print(mTree.count_merkle_nodes)

bfs(merkle_root)