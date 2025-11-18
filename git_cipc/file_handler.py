import os

def create_file(filename, path):
    try:
        open(path + filename, "x")
        return True
    except Exception as e:
        print(e)
        return False
    
    
    
def get_files_to_store(curr_path):
        # to store files in a list
    list = []

    for (root, dirs, file) in os.walk(curr_path):
        path = ""
        
        if root == curr_path:
            # print("Currently in root")
            # Does nothing cause "path" is already cleared
            pass
        
        elif ".git_cipc" in root:
            continue
        
        else:
            path = root.split("/")[-1]
        
        for f in file:
            list.append(os.path.join(path, f))
    
    return list


def write_file_contents(filepath, contents):
    # Define the full file path
    full_file_path = "data_files/logs/daily_log.csv"

    # 1. Extract the directory part of the path
    directory = os.path.dirname(full_file_path)

    # 2. Create the directories if they don't exist
    #   - exist_ok=True: Prevents an error if the directory already exists.
    if directory: # Check if the directory variable is not empty
        os.makedirs(directory, exist_ok=True)
        
    