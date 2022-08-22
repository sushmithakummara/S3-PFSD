
#MODULES   of re
#import re
#str="Sundeep Saradhi"
#x=re.findall("i",str)
#x=re.search("Saradhi",str)--it does not give actual output,it only gives span the below span method give actual output
"""print(x.start())--gives out put of index because of start method we get actual result
print(x.start())----o/p-8
print(x.span())---o/p-(8,15)
print(x.string)---gives entire string"""
#x=re.split(" ",str) --o/p->['Sundeep', 'Saradhi']
#x=re.split("Sundeep",str)--->['', ' Saradhi']
"""str="Sundeep Saradhi is ftyyt"
x=re.split(" ",str,2)--->give slip into two
['Sundeep', 'Saradhi', 'is ftyyt']"""
#x=re.sub("S","e",str)-->eundeep earadhi
#x=re.sub("S","n",str,2)
#print(x)

#MODULE --OS
import os
"""cwd=os.getcwd()
print("current working directoruy",cwd)
OUTPUT-current working directoruy C:\Srinivasulu\PycharmProjects\S3-PFSD"""
#creating a directory
"""os.mkdir("Sushmitha-this is created in curret directory")
print("dir is created")"""
#to create a group of directories simultaneously
#os.mkdirs("Sushmitha\sub1\sub2\sub3")
#print("three sub directories are created in which is current directory")"""
#to delete particular directory
"""os.rmdir("Sushmitha\sub\sub1\sub2")
print("sub2 is deleted")"""
"""os.removedirs("Sushmitha\sub\sub1\sub2")
print("3 directories are delete")"""
# to get all the lists
"""lst=os.listdir()
print(lst)"""
# to check how many lists are there i.e number count
"""lst=os.listdir()
x=len(lst)
print(x)  -->15"""
#to execute aother than the python commands
"""x=os.system("date")
print(x)"""
#given input opens calculator as an output
"""y=os.system("calc")
print(y)"""
# to rename the file
"""os.rename("prog_7","Prog_7")
print("name changed")
"""