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


def initialize_disk():

    # initialize the entire file storage space to ZERO
    # and append them to EMPTY_ADDRESSES stack
    for i in range(INODE_ADDRESS_SPACE + 2, DISK_SIZE):
        EMPTY_ADDRESSES.append(i)

    # initialize the SUPER BLOCK (SB)
    SB = {
        'number_inodes': INODE_ADDRESS_SPACE,
        'free_blocks': EMPTY_ADDRESSES,
        'used_disk_blocks': 0
    }

    #initialize INODES dictionary
    INODES = {
        'root_inode': {
            'size': 1,
            'LM': 'today',
            'CR': 'today',
            'add1': 1
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


def create_inode():
    pass

def remove_inode():
    pass

def open(filename):
    pass
