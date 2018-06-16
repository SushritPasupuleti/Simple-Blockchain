#%%
import hashlib as hasher
import hashlib
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def hash_block(self):
        sha = hasher.sha256()
        #sha.update(str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode('utf-8')
        sha.update((str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)).encode())
        return sha.hexdigest()

def create_1st_block():
    return Block(0, date.datetime.now(), "First Block", "0")

def next_block(previous_block):
    this_index = previous_block.index + 1
    this_timestamp = date.datetime.now()
    this_data = "Hey! I'm block " + str(this_index)
    this_hash = previous_block.hash

    return Block(this_index, this_timestamp, this_data, this_hash)


def init_chain():
    blockchain = [create_1st_block()]
    previous_block = blockchain[0]

    num_of_blocks_to_add = 20

    for i in range(0, num_of_blocks_to_add):
        block_to_add = next_block(previous_block)
        blockchain.append(block_to_add)
        previous_block = block_to_add
        
        print("Block number {} is here!!!".format(block_to_add.index))
        print("Hash: {}\n".format(block_to_add.hash))

init_chain()
