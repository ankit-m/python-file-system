import inode_space
import filesystem

print "Testing All components - 6 Tests"

create_this = ['Hello.txt','Sahil.c','Muchhu.js','Blahhhh.txt']
add_this = ['Hello.txt','Sahil.c','Blahhhh.txt','3.html','Muchhu.js']
write_this = ['Sahil.c', 'Mucchu.js','Hello.txt']
read_this = ['Hello.txt', 'Mucchu.js']
seek_read = [20, 0]
data_to_write = ["TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.TESTING THIS COMPONENT.Random Input to terminate Sahil.c with dots ........................................................", "My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit.My name is Ankit. FILE TERMINATION DOTS.........................................................","BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME.BRO BRO OS IS AWESOME. Dot Terminations marks the end! ......................................................................"]
delete_this = ['Hello.txt','My.js']
open_after_delete = ['Hello.txt','Sahil.c']
read_after_write_and_delete = ['Mucchu.js','Sahil.c','Hello.txt']


def create_test():
    for i in len(create_this):
        message = inode_space.open(create_this[i])
        if message == False:
            print "Out of space"
        else:
            print "File opened/Created"
    print "Test 1 -> Complete"


def open_test():
    for i in len(add_this):
        message = inode_space.open(add_this[i])
        if message == False:
            print "Out of space"
        else:
            print "File opened"
    print "Test 2 -> Complete"

def write_test():
    for i in len(write_this):
        message = inode_space.write(write_this[i],data_to_write[i])
        if message == False:
            print "Write Unsuccessful"
        else:
            print "Write Successful"
    print "Test 3 -> Complete"

def read_test():
    for i in len(read_this):
        message = inode_space.read(read_this[i],seek_read[i])
        if message == False:
            print "Read Unsuccessful"
        else:
            print "Read Successful"
    print "Test 4 -> Complete"

def delete_test():
    for i in len(delete_this):
        message = inode_space.free(delete_this[i])
        if message == False:
            print "File Does not exist"
        else:
            print "File Deleted"
    print "Test 5 -> Complete"

def open_delete():
    for i in len(open_after_delete):
        message = inode_space.open(open_after_delete)
        if message == False:
            print "Not found: Deleted"
        else:
            print "Found"
    print "Test 6 -> Complete"

def read_after_ops():
    for i in len(read_after_write_and_delete):
        message = inode_space.read(read_after_write_and_delete[i],0)
        if message == False:
            print "Could not read. Deleted file"
        else:
            print "Read File.After modification"
    print "Test 7 -> Complete"

print "Test 1: Create File"
create_test()

print "Test 2: Open File"
open_test()

print "Test 3: Write File"
write_test()

print "Test 4: Read with seek"
read_test()

print "Test 5: Delete File"
delete_test()

print "Test 6: Open After delete"
open_delete()

print "Test 7: Read after delete and write File"
read_after_ops()

print "Test complete"
