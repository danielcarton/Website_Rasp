# import OS module
import os
 
# Get the list of all files and directories

path=os.path.dirname(__file__)+"/pdf folder"
dir_list = [os.listdir(path),os.listdir(path)]
for x in range(len(dir_list[0])):
    dir_list[1][x]=dir_list[0][x].capitalize()
    dir_list[1][x]=dir_list[1][x].split(".")[0]   
 
# prints all files
print(len(dir_list[0]))
print(dir_list)