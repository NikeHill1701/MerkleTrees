import os
import math
import hashlib
import queue
from MerkleNode import MerkleNode

class MerkleTree:

    def __init__(self):
        super().__init__()
        self.count_merkle_nodes = 0
        self.merkle_root = None
    
    def get_merkle_node(self,data):
        """
            Creates and returns a new merkle node with the hash of data as the hash value.
            Data is to be provided in bytes from not unicode.
        """
        merkle_node = MerkleNode()
        hash_value = hashlib.sha256(data).hexdigest()
        merkle_node.set_hash_value(hash_value)
        self.count_merkle_nodes += 1

        return merkle_node

    def join_merkle_roots(self,root1: MerkleNode(), root2: MerkleNode()):
        """
            Joins two Merkle Roots to form a single tree
        """
        s = root1.get_hash_value() + root2.get_hash_value()
        new_root = self.get_merkle_node(s.encode())
        
        new_root.set_left_child(root1)
        new_root.set_right_child(root2)

        root1.set_parent(new_root)
        root2.set_parent(new_root)

        return new_root

    def construct_merkle_tree(self,data):
        """
            A recursive function which creates a Merkle Tree by hashing the given data
            1 Merkle Node for 1 unit of data
            Returns the root of the Merkle Tree
        """

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

    def get_tree_illustration(self, root, n_tabs, prefix = ""):
        """
            A recursive function to illustrate the Merkle Tree
            Sample Illustration:  root
                                    |---left_child
                                    |   |---left_child
                                    |   |---right_child
                                    |---right_child
                                        |---left_child
                                        |---right_child
        """
        if root == None:
            return
            
        print(prefix[:-2], '|', end='')
        #print(prefix, end='')
        print("|--", root.get_hash_value())
        self.get_tree_illustration(root.get_left_child(), n_tabs + 1, prefix + "    |")
        self.get_tree_illustration(root.get_right_child(), n_tabs + 1, prefix + "     ")


def divide_file_into_blocks(file,block_size):
    """
        A function to divide the data, for which the Merkle Tree has to be formed, 
        into blocks of given size
    """

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
    q = queue.Queue()
    q.put(root) 
    q.put(None)
    cnt = 0;
    while q.qsize() > 0:
        curr = q.get()
        if curr == None:
            print(cnt)
            cnt = 0
            print("-----------------")
            if q.qsize() > 0:
                q.put(None)
            continue
        cnt += 1
        print(curr.get_hash_value(), end=' || ')
        if curr.get_left_child() != None:
            q.put(curr.get_left_child())
        if curr.get_right_child() != None:
            q.put(curr.get_right_child())
    
file_path = "/home/nikhil/Desktop/btp/basic.py"
block_list = divide_file_into_blocks(file_path,50)

print(len(block_list))

mTree = MerkleTree()
merkle_root = mTree.construct_merkle_tree(block_list)

print(merkle_root)
print(mTree.count_merkle_nodes)

mTree.get_tree_illustration(mTree.merkle_root, 0)

#bfs(merkle_root)
