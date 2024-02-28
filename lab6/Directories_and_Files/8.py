import os

def delete_file(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist")
        return

    if os.path.isfile(path):
        if os.access(path,os.X_OK):
            os.remove(path)
            print(f"The file '{path}' was removed.")
        else:
            print(f"The file '{path}' is not executable.")
    else:
        print(f"The path '{path}' is a directory, so executability is not applicable.")

# open("this_file_will_be_removed.txt","w").close()


delete_file("this_file_will_be_removed.txt")