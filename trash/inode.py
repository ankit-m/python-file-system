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


def create_inode():
    pass

    def open_file(file_name):

        global INODES
        root = DISK[INODES['1']['address'][0]]

        if file_name in root['fileName']:
            index = root['fileName'].index(file_name)
            index = index + 1
            return index
        else:
            return create_inode(file_name)

    def read_file(fd,seek_value):

        global INODES
        root = DISK[INODES['1']['address'][0]]

        if fd in root['inode']:

            index =  root['inode'].index(fd)
            index = index + 1
            inode_value = INODES[index]
            limit = len(inode_value['address'])
            a = []
            for i in range(limit):
                a.append(inode_value['address'][i])
            return True,a[seek_value:len(a)]

        else:
            return False,"Error in Read File Operation"
        # print myRoot['fileName'][index]

    def write_file(fd, data,seek_value):

        global INODES
        root = DISK[INODES['1']['address'][0]]

            SPACE_value = SPACE[3 + index/64][index%64]['address']      # Gets address in memory from inode of file
            limit = int(math.ceil((seek_value + len(data))/1024)) + 1

            if seek_value:
                   # Extra one because limit must be included in for loop
                print limit
                print len(data)

                if limit > 64:
                    # Extend code SPACE goes here
                else:

                    start_index = seek_value/BYTE_SIZE
                    start_offset = seek_value%BYTE_SIZE
                    start_limit = SPACE_value + start_index + start_offset
                    chunk = data[(seek_value):(seek_value + start_offset)]
                    start = int(math.ceil(start_index))

                    for start in range(limit):
                        chunk = data[(start*1024):(1024*(start+1))]
                        SPACE[start_limit + start] = chunk


            else:
                limit = int(math.ceil(len(data)/1024)) + 1
                if limit > 64:
                    # Extend SPACE here
                else:
                    for i in range(limit):
                        chunk = data[(i*1024):(1024*(i+1))]
                        SPACE[SPACE_value + i] = chunk

        return "Error in Writing to Disk"
def remove_inode():
    pass

def open(filename):
    pass
