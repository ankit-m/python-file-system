
# Data by default is in KB unless mentioned otherwise
# 20 MB file size

space = [0] * 20446
inode_size = 64             # This is in KB
inode_address_space = 4096
files = 256
file_size = 64
total_size = 16384 # This is 16 MB data size

inode = {
    'size' : 1,
    'date': 'NULL',
    'address': 4162
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

def create_disk():
    print "Hello"
    # Creating inode space here
    for i in range(3,5):
        a = []
        for j in range(0,64):
            a.append(inode)
        space[i] = a

    space[3][0] = root_inode
    # print space[3][0]

    # Creating file space here
    space[4098] = root
    space[4162] = "Hello, Can you see me!"
    print space[4098]
    return

create_disk()
sahil =  "Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.Hello this is a sample test file I am creating for myself.HeBLAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHh"

def open_file(file_name):
        root_dir = space[3][0]
        print root_dir
        root_dir_address = root_dir['address']
        myRoot = space[root_dir_address]
        if file_name in myRoot['fileName']:
            index =  myRoot['fileName'].index(file_name)
            index = index + 1
            space_value = space[3 + index/64][index%64]['address']
            print space[space_value]
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
