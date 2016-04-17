from harddisk import disk
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
    location[filename] = {
        'name': filename,
        'type': filetype,
        'attrs': 'rw',
        'data': ' '
    }
    return location[filename]


def read_file(path, args):
    location = traverse_disk(path)
    filename = args[0]
    try:
        print location[filename]['data']
    except KeyError:
        print 'No such file in this directory'


def write_file(arg):
    pass


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
