"""
Homework 7, Exercise 2
Daniel Wandeler
December 8, 2020

This program searches a directory tree for .pdf files, printing the file, its size, and absolute path. Those
files are then copied into a new folder.

This program uses the current working directory as the starting file path of checking for the prompt. Also,
the new directory is made in the current working directory as well.
"""
import os
import shutil

path = os.getcwd()
newDir = "hw7_ex2"

def pdfGetter():
    newDirPath = os.path.join(path, newDir)
    if not os.path.exists(newDirPath): os.mkdir(newDirPath)
    # Following tutorial from lecture slides
    for folderName, subfolders, filenames in os.walk(path):
        for subfolder in subfolders:
            for filename in filenames:
                if filename.endswith('.pdf'):
                    print(os.path.abspath(filename))
                    print("Total file size: {}\n".format(os.path.getsize(filename)))
                    pdfFile = open(filename)
                    pdfFile.read()
                    pdfFile.close()
                    shutil.copy(filename, newDirPath)


# Iterates through whole directory tree and prints critical info about .pdf files within
pdfGetter()
