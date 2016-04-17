import pickle

try:    
    dump_file = open('disk', 'rb')
    DISK = pickle.load(dump_file)
    dump_file.close()
    file_table = DISK[8]

except EOFError:
    file_table = {
        'root': {

        }
    }

