# Given a base directory (folder), print k largest files in it

# A/
#   - B/
#    - quux (2G)
#   - C/
#     - bar (1G)
#     - D/
#       - baz (6G)
#       - quux (1G)
#   - foo (8G)

# printKLargest("A", 3) should print

#    A/foo
#    A/C/D/baz
#    A/B/quux

# because they are the three largest files in the tree rooted at A

# Following functions can be made use of:

# listoffiles(directory: string) -> array<string>
# sizeof(absolute_file_path) -> usize
# isdir(absolute_path: string) -> bool


import os
from operator import itemgetter


def sizeof(filepath):
    return os.path.getsize(filepath)

def isdir(filepath):
    return os.path.isdir(filepath)

def listoffiles(fp):
    fpaths = os.listdir(fp)
    return [os.path.join(fp, path) for path in fpaths]
    
def get_files(dirname, files=[]):
    if isdir(dirname):
        entities = listoffiles(dirname)
        for entity in entities:
            files.extend(get_files(entity))
    else:
        files.append(dirname)

    return files

def printKLargest(dirname, K):
    start = 0
    all_files = {}
    files = get_files(dirname)
    for filepath in files:
        all_files[filepath]  = sizeof(filepath)

    sorted_files = sorted(all_files.items(), key=itemgetter(1), reverse=True)
    while start < K:
        print(sorted_files.pop(0)[0])
        start+=1
    return


if __name__ == '__main__':
    printKLargest("data/A", 3)


# OUTPUT:
#
# data/A/foo
# data/A/C/D/baz
# data/A/B/quux
