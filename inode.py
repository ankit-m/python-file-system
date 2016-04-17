# Data by default is in KB unless mentioned otherwise
# 20 MB file size
import math
This is 16 MB data size

SPACE = [0] * 20482
INODE_SIZE = 64             # This is in KB
inode_address_SPACE = 4096
FILES = 256
FILE_SIZE = 64
TOTAL_SIZE = 16384
BYTE_SIZE = 1024
BASE_ADDRESS = 4162
DISK_SPACE = 20482
# This is 16 MB data size

inode = {
    '1': ['size' : 1,'date': 'NULL','address': BASE_ADDRESS]
}

inode = {

}

root_inode = {
    'size': 64,
    'address': 4098
}

root = {
    'inode': [1,2,3],
    'fileName': ["sahil","Ankit.txt","Kushan.txt"]
}

content = None
def initialize_disk():
    for i in range(INODE_ADDRESS_SPACE + 2, DISK_SPACE):
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

    SPACE[3][0] = root_inode
def create_disk():
    print "Hello"
    # Creating inode SPACE here
    for i in range(3,5):
        a = []
        for j in range(0,64):
            a.append(inode)
        SPACE[i] = a

    SPACE[3][0] = root_inode
    # print SPACE[3][0]

    # Creating file SPACE here
    SPACE[4098] = root
    SPACE[4162] = "Hello, Can you see me!"
    print SPACE[4098]
    return

# create_disk()
# myData =  "Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.HeBLAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh"

    def open_file(file_name):
        root_dir = SPACE[3][0]
        root_dir_address = root_dir['address']
        myRoot = SPACE[root_dir_address]
        if file_name in myRoot['fileName']:
            index = myRoot['fileName'].index(file_name)
            index = index + 1
            return index
        else:
            return create_file(file_name)



    def write_file(file_name, data, seek_value):

        root_dir = SPACE[3][0]
        root_dir_address = root_dir['address']
        myRoot = SPACE[root_dir_address]

            index =  myRoot['fileName'].index(file_name)    # Gets the index of file name.
            index = index + 1       # The one is added because inode index 0 is the root inode index. Other inodes will start from 1.

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

write_file('sahil',myData)
read_file('sahil')


    def read_file(fd,seek_value):
        root_dir = SPACE[3][0]
        print root_dir
        root_dir_address = root_dir['address']
        myRoot = SPACE[root_dir_address]
        if fd in myRoot['inode']:
            index =  myRoot['inode'].index(fd)
            index = index + 1
            SPACE_value = SPACE[3 + index/64][index%64]['address']
            SIZE = (SPACE[3 + index/64][index%64]['size'])/1024
            a = []
            for i in range(SPACE_value  SIZE)
                a.append(SPACE[SPACE_value])
            return True,a
        else:
            return False,"Error in Read File Operation"
        # print myRoot['fileName'][index]

    def create_file(file_name):

        for i in range(3,5):
            for j in range(0,64):
                if SPACE[i][j]['address'] == 'NULL':
                    SPACE[i][j]['adress'] = BASE_ADDRESS + i*FILE_SIZE + j
                    return (i*FILE_SIZE + j)
        return False,"Error in Creating File.No SPACE."
