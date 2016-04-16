import filesystem
import dirsystem
import os

commands = {
    'open': filesystem.open_file,
    'read': filesystem.read_file,
    'delete': filesystem.delete_file
}

current_path = 'root/'

while True:
    inp = raw_input(current_path + ' > ')
    try:
        commands[inp.split(' ')[0]](current_path, inp.split(' ')[1:])
    except KeyError:
        print 'Invalid Command'
