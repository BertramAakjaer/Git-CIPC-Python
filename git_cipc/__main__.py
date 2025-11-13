# Imports of external libaries
import argparse, os

# Domestic libarias/modules custom programmed in these scripts
import git_cipc.init_cicp as init_cipc
import git_cipc.rebuild_project as rebuild_proj


# Handler for flags used
parser = argparse.ArgumentParser(prog="git-cipc", description="Git like project for version control")
parser.add_argument('-i', '--init', action='store_true', help="Init a project")
parser.add_argument('-c', '--commit', action='store_true', help="Commit new changes")
parser.add_argument('-r', '--remove', action="store_true", help="Removes the found project in folder")
parser.add_argument('-R', '--rebuild', action="store_true", help="Rebuilds the entire project from the version control code")


class CIPC_Project:
    def __init__(self):
        self.curr_path = os.getcwd()
        self.git_cipc_path = self.curr_path + "/.git_cipc/"
        self.commit_data_path = self.git_cipc_path + "/data/"



def main():
    args = parser.parse_args()
        
    if more_than_one_flag([args.init, args.commit, args.remove]):
        print("Please only use one flag at a time :)")
        return

    if not any(vars(args).values()):
        parser.print_help()
    else:
        cipc_object = CIPC_Project()
        
        if args.init:
            init_cipc.initialize_project(cipc_object)
        if args.commit:
            print("Test 2")
        if args.remove:
            print("Test 3")
        if args.rebuild:
            rebuild_proj.rebuild(cipc_object, None)
            
            
            
            
def more_than_one_flag(list_of_flags):
    count_flags = 0
    
    for i in list_of_flags:
        if i:
            count_flags += 1

    return (count_flags > 1)