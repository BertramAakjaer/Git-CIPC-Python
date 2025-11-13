import os, xxhash

import git_cipc.file_handler as file_handler

def initialize_project(cipc):
    # 1. Make version control folder
    if not os.path.exists(cipc.git_cipc_path):
        os.makedirs(cipc.git_cipc_path)
        
    if not os.path.exists(cipc.commit_data_path):
        os.makedirs(cipc.commit_data_path)
        
    
    
    # 2. Make Header & Origin file for folder
    if not file_handler.create_file("header", cipc.git_cipc_path):
        print("Header already exists!")
    
    if not file_handler.create_file("origin", cipc.commit_data_path):
        print("Origin already exists!")
    
    if not populate_header(cipc):
        print("Error populating header")
        
        
    # 3. Get the list of all files and directories
    files = file_handler.get_files_to_store(cipc.curr_path)
    
    # 4. Make "origin" commit
    if not populate_origin(files, cipc):
        print("Error populating origin")
        
    
    return True
        
    

def populate_header(cipc):
    try:
        dest_path = os.path.join(cipc.git_cipc_path, "header")
        with open(dest_path, "w", encoding="utf-8") as f:
            f.write("[Build:Order]\n")
            f.write("origin\n")
        
        return True
    except Exception as e:
        print(e)
        return False


def populate_origin(files, cipc):
    try:
        dest_path = os.path.join(cipc.commit_data_path, "origin")
        with open(dest_path, "w", encoding="utf-8") as f_origin:
            for file in files:
                
                file_full_path = os.path.join(cipc.curr_path, file)
                                
                with open(file_full_path, "r", encoding="utf-8") as f_in:
                    
                    # Read the entire content of the source file
                    content = f_in.read()
                    
                    file_checksum = xxhash.xxh3_128_hexdigest(content)
                    
                    file_stat = os.stat(file_full_path)
                    last_modified = file_stat.st_mtime
                    
                    f_origin.write(f"[FILE:{file}][CHECKSUM:{file_checksum}][TIMESTAMP:{last_modified}]\n")
                    
                    f_origin.write(content)                        
                    f_origin.write("\n")
                    f_origin.write("[END]")
                    f_origin.write("\n\n")
                                
        return True
    
    except Exception as e:
        print(e)
        return False