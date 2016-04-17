# Data by default is in KB unless mentioned otherwise
# 20 MB file size

from harddisk import file_table
import pickle

INODE_SIZE = 64
DISK_SIZE = 20482
INODE_ADDRESS_SPACE = 4096
MAX_INODES = INODE_ADDRESS_SPACE * 16
FILES = 256
FILE_SIZE = 64
BLOCK_SIZE = 1024
TOTAL_SIZE = 16384
NUMBER_FIXED_ADDRESSES = 7
SINGLE_HIERARCHY_ADDRESSES = 512
DISK_START = 0
SB_START = 0
ROOT_INODE_START = 3

EMPTY_ADDRESSES = []
FILE_DATA = []
DISK = []
INODES = {}
SB = {}
ROOT_DIR = {}
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
            'address': [5]
        }
    }

    # initialize disk elements
    DISK.append(None)
    DISK.append(SB)
    DISK.append(None)
    DISK.append(SINGLE_HIERARCHY)
    DISK.append(INODES)
    DISK.append(ROOT_DIR)
    DISK.append(FILE_DATA)
    DISK.append(EMPTY_ADDRESSES)
    DISK.append(file_table)

try:    
    dump_file = open('disk', 'rb')
    DISK = pickle.load(dump_file)
    dump_file.close()

    INODES = DISK[4]
    FILE_DATA = DISK[6]
    EMPTY_ADDRESSES = DISK[7]

except EOFError:
    print 'initializing'
    initialize_disk()


def dump():
    dump_file = open('disk', 'wb')
    pickle.dump(DISK, dump_file)
    dump_file.close()

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

        for address in INODES[number_inode]['single_hierachy']:
            EMPTY_ADDRESSES.append(address)

        del INODES[str(number_inode)]
        return True

    except KeyError:
        pass


def create_single_hierarchy_block():
    for i in range(0, SINGLE_HIERARCHY_ADDRESSES):
        index = EMPTY_ADDRESSES.pop()
        SINGLE_HIERARCHY[index] = ''
    return SINGLE_HIERARCHY


def open_file(filename):
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

    # check if data single_hierachy field is needed
    # or if data is exceeding limit
    if len(data) > NUMBER_FIXED_ADDRESSES*BLOCK_SIZE:
        if len(data) > NUMBER_FIXED_ADDRESSES*BLOCK_SIZE + SINGLE_HIERARCHY_ADDRESSES*BLOCK_SIZE:
            print 'File size too big.'
            return False
        else:
            INODES[number_inode]['single_hierachy'] = create_single_hierarchy_block()

    # truncate existing data in case of overwrite
    INODES[str(number_inode)]['address'] = []

    # divide input into block sized chunks
    chunks = [data[i:i + BLOCK_SIZE]
              for i in range(0, len(data), BLOCK_SIZE)]

    # fill data into the addresses
    for i in range(0, min(NUMBER_FIXED_ADDRESSES, len(chunks))):
        index = EMPTY_ADDRESSES.pop()
        FILE_DATA[index] = chunks[i]
        INODES[number_inode]['address'].append(index)

    try:
        i = 0
        for index in INODES[number_inode]['single_hierachy']:
            FILE_DATA[index] = chunks[i+NUMBER_FIXED_ADDRESSES]
            i = i + 1
    except KeyError:
        pass

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
    try:
        for item in INODES[number_inode]['single_hierachy']:
            data = data + FILE_DATA[item]
    except KeyError:
        pass

    dump()
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

    # check if data single_hierachy field is needed
    # or if data is exceeding limit
    if len(data) > NUMBER_FIXED_ADDRESSES*BLOCK_SIZE: #TODO: REMAINING SIZE
        if len(data) > NUMBER_FIXED_ADDRESSES*BLOCK_SIZE + SINGLE_HIERARCHY_ADDRESSES*BLOCK_SIZE:
            print 'File size too big.'
            return False
        else:
            INODES[number_inode]['single_hierachy'] = create_single_hierarchy_block()

    # divide input into block sized chunks
    chunks = [data[i:i + BLOCK_SIZE]
              for i in range(0, len(data), BLOCK_SIZE)]

    # fill data into the addresses
    for i in range(0, min(NUMBER_FIXED_ADDRESSES, len(chunks))):
        index = EMPTY_ADDRESSES.pop()
        FILE_DATA[index] = chunks[i]
        INODES[number_inode]['address'].append(index)

    try:
        i = 0
        for index in INODES[number_inode]['single_hierachy']:
            FILE_DATA[index] = chunks[i+NUMBER_FIXED_ADDRESSES]
            i = i + 1
    except KeyError:
        pass

    return True

