#MODULE
#os

import os
"""
cwd=os.getcwd()
print("the current working directory", cwd)
"""
#to change the current working directory
"""def current_path():
    print("the current working directory ")
    print(os.getcwd())
    print()
current_path()
os.chdir('../')
current_path()"""
# to creating directory
directory="geeks for geeks"
parent_dir="C:\Users\Srinivasulu\PycharmProjects\S3-PFSD/"
path=os.path.join(parent_dir,directory)
os.mkdir(path)
print("Directory ids created", directory)
directory="geeks"
parent_dir="C:\Users\Srinivasulu\PycharmProjects\S3-PFSD/"
