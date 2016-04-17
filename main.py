import filesystem
import dirsystem
import os

commands = {
    'open': filesystem.open_file,
    'read': filesystem.read_file,
    'delete': filesystem.delete_file,
    'mkdir': dirsystem.make_dir,
    'cd': dirsystem.change_dir,
    'pwd': dirsystem.present_dir
}

current_path = 'root/'

while True:
    inp = raw_input('> ')
    try:
        x = commands[inp.split(' ')[0]](current_path, inp.split(' ')[1:])
        if (x):
            if type(x) == dict:
                print x
            else:
                current_path = x;
    except KeyError:
        print 'Invalid Command'
