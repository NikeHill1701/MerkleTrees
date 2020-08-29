from pathlib import Path

def divide_file_into_blocks(file,block_count = 128):
    """
        A function to divide the data, for which the Merkle Tree has to be formed, 
        into blocks of given size
    """
    file_size = Path(file).stat().st_size
    block_size = file_size // block_count + (file_size % block_count > 0)

    block_list = []

    with open(file, 'rb') as f:
        block = f.read(block_size)
        while block:
            block_list.append(block)
            block = f.read(block_size)
    
    return block_list
