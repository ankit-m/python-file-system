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
    for i in range(INODE_ADDRESS_SPACE + 2, DISK_SIZE):
        SPACE[i] = 0
        EMPTY_ADDRESSES.append(i)
    SPACE[0] = None
    SPACE[1] = {
        'number_inodes': INODE_ADDRESS_SPACE,
        'free_blocks': EMPTY_ADDRESSES,
        'used_disk_blocks': 0
    }

    SPACE[2] = None

    root_inode = {
        'size': 1,
        'LM': 'today',
        'CR': 'today',
        'add1': '3,1'
    }
    a = []
    a.append(root_inode)
    SPACE[3] = a
    SPACE[3][0] = root_inode

    root = {
        'inode': [],
        'fileName': []
    }

    SPACE[4098] = root

initialize_disk()


def create_inode():
    SPACE[1]['number_inodes'] = SPACE[1]['number_inodes'] - 1
    inode = {
        'size': 1,
        'LM': 'today',
        'CR': 'today'
    }
    
    index = SPACE[1]['used_disk_blocks']
    SPACE_value = SPACE[3 + index / 64][index % 64]['add1']
    print SPACE_value
    SPACE[int(SPACE_value.split(',')[0])][int(SPACE_value.split(',')[1])] = inode  # check for node creation
    print 'ok'


# def create_disk():
#     print "Hello"
#     # Creating inode SPACE here
#     for i in range(3, 5):
#         a = []
#         for j in range(0, 64):
#             a.append(inode)
#         SPACE[i] = a
#
#     SPACE[3][0] = root_inode
#     # print SPACE[3][0]
#
#     # Creating file SPACE here
#     SPACE[4162] = "Hello, Can you see me!"
#     print SPACE[4098]
#     return

# create_disk()


def open_file(file_name):
    root_dir = SPACE[3][0]
    root_dir_address = root_dir['add1']
    create_inode()
    # myRoot = SPACE[int(root_dir_address.split(',')[0])][int(root_dir_address.split(',')[1])]
    # if file_name in myRoot['fileName']:
    #     index = myRoot['fileName'].index(file_name)
    #     index = index + 1
    #     SPACE_value = SPACE[3 + index / 64][index % 64]['address']
    #     print SPACE[SPACE_value]
    # else:
    #     print "False"
    # print myRoot['fileName'][index]

open_file('sahil')


def write_file(file_name):

    return "Error in Writing to Disk"


def read_file(file_name):

    return "Error in Read File Operation"


def create_file(file_name):

    return "Error in Creating File"
