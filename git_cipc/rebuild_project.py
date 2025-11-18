import os, re

def rebuild(cipc, last_step):
    
    # Get a list of all steps
    steps = list_steps(cipc.git_cipc_path)
    
    if not steps:
        print("Failed to read steps from header")
    
    if (not last_step in steps) and (last_step != None):
        print("Commit could not be resolved in repo")
        return False
    
    # Run Origin
    if not build_origin(os.path.join(cipc.commit_data_path, "origin")):
        print("Origin could not be build")
        return False
    
    # Run Script by script
    
    # Finish 
    
    
    

def list_steps(cipc_path):
    try:
        steps_list = []
        
        header_path = os.path.join(cipc_path, "header")
        with open(header_path, "r", encoding="utf-8") as f:
            
            found_build_order = False
            
            while True:
                curr_line = f.readline()
                
                if curr_line.rstrip() == "[BUILD:ORDER]":
                    found_build_order = True
                    continue
                
                if not found_build_order:
                    if curr_line == "":
                        return False
                    continue
                
                
                if curr_line == "" or curr_line == "\n":
                    break
                
                if len(steps_list) == 0 and curr_line.rstrip() != "origin":
                    return False
                
                steps_list.append(curr_line.rstrip())
        
        return steps_list            
            
            
    except Exception as e:
        print(e)
        return False
    
    
    
def last_step_exist(last_step):
    return True




def build_origin(origin_path):
    start_pattern = r"^\[FILE:.*?\]\[CHECKSUM:.*?\]\[TIMESTAMP:.*?\]"
    end_pattern = r"\[END\]" 
    
    try:
        with open(origin_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(e)
        return False

    
    starts_with_header = re.search(start_pattern, content)
    
    ends_with_end_tag = re.search(end_pattern, content)