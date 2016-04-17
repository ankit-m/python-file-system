from harddisk import disk

def traverse_disk(path):
    directories = path.split('/')
    directories.pop()
    location = disk[directories[0]]
    for folder in directories[1:]:
        location = location[folder]
    return location


def make_dir(path, args):
    location = traverse_disk(path)
    location[args[0]] = {}


def remove_dir(arg):
    location = traverse_disk(path)
    try:
        del location[args[0]]
    except KeyError:
        print 'No such directory'


def rename_dir(arg):
    pass


def change_dir(path, args):
    location = traverse_disk(path)
    new_path = ''
    for folder in args:
        try:
            location = location[folder]
            new_path = new_path + folder + '/'
        except KeyError:
            print 'No such directory'
    return path + new_path

def present_dir(path, args):
    print path
