import os

def check_path_access(path):
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist")
        return
    
    if os.access(path,os.R_OK):
        print(f"The path '{path}' is readable.")
    else:
        print(f"The path '{path}' is not readable.")

    if os.access(path,os.W_OK):
        print(f"The path '{path}' is writable.")
    else:
        print(f"The path '{path}' is not writable.")

    if os.path.isfile(path):
        if os.access(path,os.X_OK):
            print(f"The file '{path}' is executable.")
        else:
            print(f"The file '{path}' is not executable.")
    else:
        print(f"The path '{path}' is a directory, so executability is not applicable.")

check_path_access("2.py")        