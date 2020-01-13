
import os
import re

path = os.getcwd()


def overwrite_file(path):
    f = open(path,'r')
    all_lines = f.readlines()
    f.close()
    os.remove(path)
    f = open(path,'w+')
    for each_line in all_lines:
        f.writelines(each_line)
        #print each_line
    f.close()

def all_path_file(path):
    dirs = os.listdir(path)
    for file in dirs:
        curr_path = os.path.join(path,file)
        if os.path.isdir(curr_path):
            all_path_file(curr_path)
            continue
        #print(curr_path)
        #rep_str(curr_path)
        overwrite_file(curr_path)

all_path_file(path) 





