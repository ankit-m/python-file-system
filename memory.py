# Data by default is in KB unless mentioned otherwise
# 20 MB file size

SPACE = [0] * 20482
INODE_SIZE = 64             # This is in KB
INODE_ADDRESS_SPACE = 4096
FILES = 256
FILE_SIZE = 64
DISK_SIZE = 20482
TOTAL_SIZE = 16384  # This is 16 MB data size
EMPTY_ADDRESSES = []


def initialize_disk():
    for i in range(INODE_ADDRESS_SPACE + 2, SPACE):
        SPACE[i] = 0
        EMPTY_ADDRESSES.append[i]
    SPACE[0] = None
    SPACE[1] = {
        'number_inodes': INODE_ADDRESS_SPACE,
        'free_blocks': EMPTY_ADDRESSES,
        'used_disk_blocks': 0
    }

    root_inode = {
        'size': 1,
        'LM': 'today',
        'CR': 'today'
        'add1': EMPTY_ADDRESSES.pop(),
        'add2': EMPTY_ADDRESSES.pop(),
        'add3': EMPTY_ADDRESSES.pop(),
        'add4': EMPTY_ADDRESSES.pop(),
        'add5': EMPTY_ADDRESSES.pop(),
        'add6': EMPTY_ADDRESSES.pop(),
        'add7': EMPTY_ADDRESSES.pop(),
    }

    SPACE[2] = root_inode


def create_inode(){
    SPACE[1]['number_inodes'] = SPACE[1]['number_inodes'] - 1
    inode = {
        'size': 1,
        'LM': 'today',
        'CR': 'today'
        'add1': EMPTY_ADDRESSES.pop(),
        'add2': EMPTY_ADDRESSES.pop(),
        'add3': EMPTY_ADDRESSES.pop(),
        'add4': EMPTY_ADDRESSES.pop(),
        'add5': EMPTY_ADDRESSES.pop(),
        'add6': EMPTY_ADDRESSES.pop(),
        'add7': EMPTY_ADDRESSES.pop()
    }
    SPACE[3 + SPACE[1]['used_disk_blocks']] = inode #check for node creation
    return True
}

root = {
    'inode': [1, 2, 3],
    'fileName': ["sahil", "Ankit.txt", "Kushan.txt"]
}

content = None


def create_disk():
    print "Hello"
    # Creating inode SPACE here
    for i in range(3, 5):
        a = []
        for j in range(0, 64):
            a.append(inode)
        SPACE[i] = a

    SPACE[3][0] = root_inode
    # print SPACE[3][0]

    # Creating file SPACE here
    SPACE[4098] = root
    SPACE[4162] = "Hello, Can you see me!"
    print SPACE[4098]
    return

create_disk()
sahil = "Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.HeBLAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh"


def open_file(file_name):
    root_dir = SPACE[3][0]
    print root_dir
    root_dir_address = root_dir['address']
    myRoot = SPACE[root_dir_address]
    if file_name in myRoot['fileName']:
        index = myRoot['fileName'].index(file_name)
        index = index + 1
        SPACE_value = SPACE[3 + index / 64][index % 64]['address']
        print SPACE[SPACE_value]
    else:
        print "False"
    # print myRoot['fileName'][index]
    return "File does not exist"

open_file('sahil')


def write_file(file_name):

    return "Error in Writing to Disk"


def read_file(file_name):

    return "Error in Read File Operation"


def create_file(file_name):

    return "Error in Creating File"
