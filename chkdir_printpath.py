# -*- coding: utf-8 -*- 

import os
import shutil

def showDir(path):

    print "========================================"
    for dirpath,dirnames,filenames in os.walk(path):
        for dirname in dirnames:
            print os.path.join(dirpath,dirname)


if __name__ == "__main__":

    tmpdir = "/Users/tomohiro/Plactice/python/tmp"

    os.mkdir(tmpdir)
    os.makedirs("/Users/tomohiro/Plactice/python/tmp/mkdir1/mkdir2/mkdir3")
    showDir(tmpdir)
    
    os.rmdir("/Users/tomohiro/Plactice/python/tmp/mkdir1/mkdir2/mkdir3")
    showDir(tmpdir)

#   os.removedirs(tmpdir)
    shutil.rmtree(tmpdir)

