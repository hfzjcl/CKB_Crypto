
import os
import re

path = os.getcwd()

def get_filelist(dir):
    for home, dirs, files in os.walk(dir):
        #dir in this path
        for dir in dirs:
            fullname = os.path.join(home, dir)
            print(fullname)


        #file in this path
        for filename in files:
            #print(filename)
            fullname = os.path.join(home, filename)
            print(fullname)
            get_filelist(dir)

#get_filelist(path)

def rep_str(path):
    f = open(path,'r')
    all_lines = f.readlines()
    f.close()

    f = open(path,'w+')
    for each_line in all_lines:
        # replace <> to ""
        if "botan/" in each_line:
            each_line = each_line.replace("<","\"")
            each_line = each_line.replace(">","\"")
        f.writelines(each_line)
        #print each_line
    f.close()

def all_path_file(path):
    dirs = os.listdir(path)
    for file in dirs:
        if str(file)[0] == ".":
            continue
        curr_path = os.path.join(path,file)
        if os.path.isdir(curr_path):
            all_path_file(curr_path)
            continue
        #print(curr_path)
        rep_str(curr_path)

all_path_file(path) 





