import os
import shutil
from zipfile import ZipFile
from os import path
from shutil import make_archive

# Check if file exists
if path.exists("guru99.txt"):
    # get the path to the file in the current directory
        src = path.realpath("guru99.txt");
    # rename the original file
        os.rename("career.guru99.txt","guru99.txt")
    # now put things into a ZIP archive
        root_dir,tail = path.split(src)
        shutil.make_archive("guru99 archive","zip",root_dir)
    # more fine-grained control over ZIP files
        with ZipFile("testguru99.zip", "w") as newzip:
            newzip.write("guru99.txt")
            newzip.write("guru99.txt.bak")