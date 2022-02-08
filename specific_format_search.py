


import os
from pathlib import Path
from os import listdir


def getFile(path,pattern):
    list=[]
    for files in os.listdir(path):
        
        if files.endswith(pattern):             
           list.append(files)
    
    return list








































