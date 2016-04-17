a = [{''},{'w----'}]
import re

TOTAL_SPACE = 20480
CHUNK_SIZE = 5
SPLIT_LIMIT = 5
MAX_INDEX = TOTAL_SPACE/CHUNK_SIZE
UNCHECKED = "@emp@ty@"
CHECKED = "filled"

space = [UNCHECKED] * MAX_INDEX

def provide_space(chunk):

    counter = 0
    for i in xrange(MAX_INDEX):
        if space[i] == "@emp@ty@":
            counter = counter + 1
            if counter == chunk:
                return fill_space(i - chunk,chunk), i-chunk
        else:
            counter = 0

    return False

def fill_space(start, chunk):
    end = start + chunk
    for i in xrange(start,end):
        space[i] = CHECKED
    return True

def write_data(index,data):
    index = data/SPLIT_LIMIT
    arr = re.findall('..?',data)
    counter = 0
    for i in xrange(index,len(arr)):
        if space[i] == UNCHECKED:
            counter = couner + 1
        else:
            if extend_space(i,len(arr) - i):
                complete_write_data()
            else
                return False
        # This function will automatically run when the loop terminates. If the else condition executed then it will return.
        complete_write_data(index,arr)

    return

def complete_write_data(index, arr):
    for i in xrange(index, len(arr)):


def free_space(start,end):

    for i in xrange(start, end)
        space_check[i] = -1
    return True

def extend_space(index, chunk):

    return False
