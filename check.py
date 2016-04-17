# Data by default is in KB unless mentioned otherwise
# 20 MB file size

INODE_SIZE = 64
DISK_SIZE = 20482
INODE_ADDRESS_SPACE = 4096
MAX_INODES = INODE_ADDRESS_SPACE * 16
FILES = 256
FILE_SIZE = 64
BLOCK_SIZE = 1024
TOTAL_SIZE = 16384
NUMBER_FIXED_ADDRESSES = 7
EMPTY_ADDRESSES = []
FILE_DATA = []
DISK = []
INODES = {}
SINGLE_HIERARCHY = {}

# Called just once to after cold start, reset or restore.
def initialize_disk():
    global INODES
    global EMPTY_ADDRESSES
    global INODE_ADDRESS_SPACE
    global DISK_SIZE
    global DISK
    global FILE_DATA

    # initialize the entire file storage space to ZERO
    # and append them to EMPTY_ADDRESSES stack
    for i in range(0, DISK_SIZE - INODE_ADDRESS_SPACE - 2):
        EMPTY_ADDRESSES.append(i)
        FILE_DATA.append('')

    # initialize the SUPER BLOCK (SB)
    SB = {
        'init': False,
        'number_inode': 1,
        'free_blocks': EMPTY_ADDRESSES,
        'used_disk_blocks': 0
    }

    # initialize INODES dictionary
    INODES = {
        '1': {
            'size': 1,
            'LM': 'today',
            'CR': 'today',
            'address': [4]
        }
    }

    # initialize root dir
    ROOT_DIR = {}

    # initialize disk elements
    DISK.append(None)
    DISK.append(SB)
    DISK.append(None)
    DISK.append(SINGLE_HIERARCHY)
    DISK.append(INODES)
    DISK.append(ROOT_DIR)

initialize_disk()


def create_inode():
    if len(INODES) >= MAX_INODES:
        return False
    else:
        number_inode = DISK[1]['number_inode']
        new_node = number_inode+1
        INODES[str(new_node)] = {
            'size': 0,
            'LM': 'today',
            'CR': 'today',
            'address': []
        }
        DISK[1]['number_inode'] = DISK[1]['number_inode'] + 1
        return new_node


def remove_inode(number_inode):
    global EMPTY_ADDRESSES
    try:
        for address in INODES[str(number_inode)]['address']:
            EMPTY_ADDRESSES.append(address)
        del INODES[str(number_inode)]
        return True
    except KeyError:
        print 'Invalid i-Node'
        return False


def open(filename):
    global INODES
    global DISK
    root_files = DISK[INODES['1']['address'][0]]
    for inode, name in root_files.iteritems():
        if filename == name:
            return False
    number_inode = create_inode()
    if number_inode != False:
        root_files[str(number_inode)] = str(filename)
        return number_inode
    return False


def write(filename, data):
    global INODES
    global FILE_DATA
    global BLOCK_SIZE

    root_files = DISK[INODES['1']['address'][0]]
    for inode, name in root_files.iteritems():
        if filename == name:
            number_inode = inode
    if len(data) > NUMBER_FIXED_ADDRESSES*BLOCK_SIZE:
        return False
    else:
        #truncate existing data
        INODES[str(number_inode)]['address'] = []
        chunks = [data[i:i + BLOCK_SIZE]
                  for i in range(0, len(data), BLOCK_SIZE)]
        for i in chunks:
            index = EMPTY_ADDRESSES.pop()
            FILE_DATA[index] = str(i)
            INODES[number_inode]['address'].append(index)
        return True


def read(filename, seek):
    global INODES
    global DISK
    global FILE_DATA

    root_files = DISK[INODES['1']['address'][0]]
    for inode, name in root_files.iteritems():
        if filename == name:
            number_inode = inode
    data = ''
    for address in INODES[number_inode]['address']:
        data = data + FILE_DATA[address]
    return str(data[seek:len(data)])


def free(filename):
    global INODES
    global DISK
    global FILE_DATA

    root_files = DISK[INODES['1']['address'][0]]
    for inode, name in root_files.iteritems():
        if filename == name:
            number_inode = inode
    del root_files[number_inode]
    remove_inode(number_inode)


def append(filename, data):
    global INODES
    global FILE_DATA
    global BLOCK_SIZE

    root_files = DISK[INODES['1']['address'][0]]
    for inode, name in root_files.iteritems():
        if filename == name:
            number_inode = inode
    if len(data) > 7168:
        return False
    else:
        chunks = [data[i:i + BLOCK_SIZE]
                  for i in range(0, len(data), BLOCK_SIZE)]
        for i in chunks:
            index = EMPTY_ADDRESSES.pop()
            FILE_DATA[index] = str(i)
            INODES[number_inode]['address'].append(index)
        return True

# open('ankit.txt')
# write('ankit.txt',0, 'hello')
# print read('ankit.txt', 1)
