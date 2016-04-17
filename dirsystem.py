from harddisk import file_table


def traverse_disk(path):
    directories = path.split('/')
    directories.pop()
    location = file_table[directories[0]]
    for folder in directories[1:]:
        location = location[folder]
    return location


def make_dir(path, args):
    location = traverse_disk(path)
    location[args[0]] = {}


def remove_dir(path, args):
    location = traverse_disk(path)
    try:
        del location[args[0]]
    except KeyError:
        print 'No such directory'


def rename_dir(path, args):
    location = traverse_disk(path)
    location[args[1]] = location.pop(args[0])


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


def list_all(path, args):
    location = traverse_disk(path)
    for key, val in location.iteritems():
        print key
