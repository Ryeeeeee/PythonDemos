# getAllFiles.py
# get all files(not including directory) in the specified path

import os

def getAllFiles(path):
    currentFiles = os.listdir(path)
    allFiles = []
    for fileName in currentFiles:
        fullFileName = os.path.join(path, fileName)
        if os.path.isdir(fullFileName):
            nextDirs = getAllFiles(fullFileName)
            allFiles.extend(nextDirs)
        else:
            allFiles.append(fullFileName)
    return allFiles

def getAllFilesByWalk(path):
    for root, dirs, files in os.walk(path):
        for filePath in files:
            print os.path.join(root, filePath)

if __name__ == '__main__':
    #print getAllFiles('.')
    getAllFilesByWalk('..')