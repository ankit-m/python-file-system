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
    pass


def open_dir(arg):
    pass


def rename_dir(arg):
    pass


def change_dir(path, args):
    location = traverse_disk(path)



def present_dir(arg):
    pass
