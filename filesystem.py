from harddisk import file_table
import check
import pickle


def traverse_disk(path):
    directories = path.split('/')
    directories.pop()
    location = file_table[directories[0]]
    for folder in directories[1:]:
        location = location[folder]
    return location


def open_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    filetype = args[0].split('.')[0]
    inode = check.open_file(filename)
    if(inode):
        location[filename] = {
            'name': filename,
            'type': filetype,
            'mode': 'rw',
            'rseek': 0,
            'inode': inode
        }
    else:
        print 'Cannot create file.'


def read_file(path, args):
    location = traverse_disk(path)
    try:
        filename = args[0]
        print check.read(filename, location[filename]['rseek'])
    except KeyError:
        print 'No such file in this directory'
    except IndexError:
        print 'Insufficient arguments.'


def write_file(path, args):
    location = traverse_disk(path)
    try:
        filename = args[0]
        check.write(filename, args[1])
    except KeyError:
        print 'No such file in this directory'
    except IndexError:
        print 'Insufficient arguments.'


def delete_file(path, args):
    location = traverse_disk(path)
    try:
        filename = args[0]
        check.free(filename)
        del location[filename]
    except KeyError:
        print 'No such file in this directory'
    except IndexError:
        print 'Insufficient arguments.'


def get_attributes(arg):
    pass


def set_attributes(arg):
    pass


def rseek(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        location[filename]['rseek'] = int(args[1])
    except KeyError:
        print 'No such file open in this directory'
    except IndexError:
        print 'Insufficient arguments.'


def append_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        check.append(filename, args[1])
    except KeyError:
        print 'No such file open in the directory'
