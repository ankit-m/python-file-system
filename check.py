# Data by default is in KB unless mentioned otherwise
# 20 MB file size

INODE_SIZE = 64             # This is in KB
DISK_SIZE = 20482
INODE_ADDRESS_SPACE = 4096
FILES = 256
FILE_SIZE = 64
TOTAL_SIZE = 16384  # This is 16 MB data size
EMPTY_ADDRESSES = []
DISK = []
INODES = {}


def initialize_disk():
    global INODES
    global EMPTY_ADDRESSES
    global INODE_ADDRESS_SPACE
    global DISK_SIZE
    global DISK

    # initialize the entire file storage space to ZERO
    # and append them to EMPTY_ADDRESSES stack
    for i in range(INODE_ADDRESS_SPACE + 2, DISK_SIZE):
        EMPTY_ADDRESSES.append(i)

    # initialize the SUPER BLOCK (SB)
    SB = {
        'number_inode': 1,
        'free_blocks': EMPTY_ADDRESSES,
        'used_disk_blocks': 0
    }

    #initialize INODES dictionary
    INODES = {
        '1': {
            'size': 1,
            'LM': 'today',
            'CR': 'today',
            'address': [4]
        }
    }

    #initialize root dir
    ROOT_DIR = {}

    #initialize disk elements
    DISK.append(None)
    DISK.append(SB)
    DISK.append(None)
    DISK.append(INODES)
    DISK.append(ROOT_DIR)

initialize_disk()


def create_inode():
    if len(INODES) >= INODE_ADDRESS_SPACE:
        return False
    else:
        number_inode = DISK[1]['number_inode']
        INODES[str(number_inode + 1)] = {
            'size': 0,
            'LM': 'today',
            'CR': 'today',
            'address': []
        }
        DISK[1]['number_inode'] = DISK[1]['number_inode'] + 1
        return number_inode

create_inode()

def remove_inode(number_inode):
    try:
        del INODES[str(number_inode)]
        return True
    except KeyError:
        print 'Invalid i-Node'
        return False

remove_inode(2)

def open(filename):
    pass
