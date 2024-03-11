import os


def dir(path, list_all): 

    for dir_name in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir_name)):
            print(dir_name)
            if list_all:
                dir(os.path.join(path, dir_name))

def files(path,list_all):
    for file_name in os.listdir(path):
        if os.path.isfile(os.path.join(path, file_name)):
            print(file_name)
        if list_all and os.path.isdir(os.path.join(path, file_name)):
            files(os.path.join(path, file_name), True)

# dir("../", True)
files("../", True)