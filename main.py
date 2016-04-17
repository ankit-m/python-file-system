import filesystem
import dirsystem
import os

journal = open ('journal.txt', 'a')


commands = {
    'open': filesystem.open_file,
    'read': filesystem.read_file,
    'delete': filesystem.delete_file,
    'write': filesystem.write_file,
    'rseek': filesystem.rseek,
    'append': filesystem.append_file,
    'mkdir': dirsystem.make_dir,
    'cd': dirsystem.change_dir,
    'pwd': dirsystem.present_dir,
    'rmdir': dirsystem.remove_dir,
    'mvdir': dirsystem.rename_dir,
    'ls': dirsystem.list_all
}

current_path = 'root/'

while True:
    inp = raw_input('> ')
    try:
        x = commands[inp.split(' ')[0]](current_path, inp.split(' ')[1:])
        journal.write(inp + '\n')
        if (x):
            if type(x) == dict:
                print x
            else:
                current_path = x;
    except KeyError:
        print 'Invalid Command'

journal.close()
