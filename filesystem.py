from harddisk import disk
import check
import pickle


def traverse_disk(path):
    directories = path.split('/')
    directories.pop()
    location = disk[directories[0]]
    for folder in directories[1:]:
        location = location[folder]
    return location


def open_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    filetype = args[0].split('.')[0]
    inode = check.open(filename)
    if(inode):
        location[filename] = {
            'name': filename,
            'type': filetype,
            'mode': 'rw',
            'rseek': 0,
            'wseek': 0,
            'inode': inode
        }
    else:
        print 'Cannot create file.'

def read_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        print check.read(filename, location[filename]['rseek'])
    except KeyError:
        print 'No such file in this directory'


def write_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        check.write(filename, location[filename]['wseek'], args[1])
    except KeyError:
        print 'No such file in this directory'

def delete_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        del location[filename]
    except KeyError:
        print 'No such file in this directory'


def get_attributes(arg):
    pass


def set_attributes(arg):
    pass

def seek(path, args):
    pass
