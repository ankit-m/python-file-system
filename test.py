import inode_space
import filesystem
import time

print
print "Testing All components - 7 Tests"

create_this = ['Hello.txt','Sahil.c','Muchhu.js','Blahhhh.txt']
add_this = ['Mucchu.js','Hello.txt','Sahil.c','Blahhhh.txt','3.html','Mucchu.js']
write_this = ['Sahil.c','Mucchu.js','Hello.txt']
read_this = ['Hello.txt', 'Mucchu.js']
seek_read = [20, 0]
data_to_write = ["HEllo","Hello","Hello"]
delete_this = ['Hello.txt']
open_after_delete = ['Hello.txt','Sahil.c']
read_after_write_and_delete = ['Mucchu.js','Sahil.c','Blahhhh.txt']


def create_test():
    for i in range(len(create_this)):
        message = inode_space.open_file(create_this[i])
        if message == False:
            print "Already opened"
        else:
            print "File opened/Created"
    print "Test 1 -> Complete"
    return


def open_test():
    for i in range(len(add_this)):
        message = inode_space.open_file(add_this[i])
        if message == False:
            print "Already open"
        else:
            print "File opened"
    print "Test 2 -> Complete"
    return

def write_test():
    for i in range(len(write_this)):
        message = inode_space.write(write_this[i],data_to_write[i])
        if message == False:
            print "Write Unsuccessful!"
        else:
            print "Write Successful"
    print "Test 3 -> Complete"
    return

def read_test():
    for i in range(len(read_this)):
        message = inode_space.read(read_this[i],seek_read[i])
        if message == False:
            print "Read Unsuccessful"
        else:
            print "Read Successful"
    print "Test 4 -> Complete"
    return

def delete_test():
    for i in range(len(delete_this)):
        message = inode_space.free(delete_this[i])
        if message == False:
            print "File Does not exist"
        else:
            print "File Deleted"
    print "Test 5 -> Complete"
    return

def open_delete():
    for i in range(len(open_after_delete)):
        message = inode_space.open_file(open_after_delete)
        if message == False:
            print "Not found: Deleted"
        else:
            print "Found"
    print "Test 6 -> Complete"
    return

def read_after_ops():
    for i in range(len(read_after_write_and_delete)):
        message = inode_space.read(read_after_write_and_delete[i],0)
        if message == False:
            print "Could not read. Deleted file"
        else:
            print "Read File.After modification"
    print "Test 7 -> Complete"
    return

print
print "Test 1: Create File"
create_test()
time.sleep(1)
print
print "Test 2: Open File"
open_test()
time.sleep(1)
print
print "Test 3: Write File"
write_test()
time.sleep(1)
print
print "Test 4: Read with seek"
read_test()
time.sleep(1)
print
print "Test 5: Delete File"
delete_test()
time.sleep(1)
print
print "Test 6: Open After delete"
open_delete()
time.sleep(1)
print
print "Test 7: Read after delete and write File"
read_after_ops()
print
print "Tests complete"
