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