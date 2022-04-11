# Create new directory
# Create new text file
# Within text file, list of files in current directory, along wit bite count within file
# Folder called results
# results.txt
# Only count files

import os

ppath = (os.path.split(os.path.realpath("textfile.txt")))
ppath = str(ppath[0])

folderName = "results"
fileName = "results.txt"

def createFolder(fpath):
    finalPath = os.path.join(ppath,fpath)

    os.mkdir(finalPath)
    print(finalPath)

def createfile(fpath,tpath):
    # Create new file
    nf = open(os.path.join(ppath,fpath,tpath),"w+")
    
    # This creates the list of file names
    f = os.listdir(ppath)
    
    # Gets sum of bites for files
    x = 0
    for s in f:
        x = x + os.stat(s).st_size
    nf.writelines("Total bytecount:"+str(x)+'\n'+"Files list:"+'\n'+"----------------"+'\n')
    
    # writes files in list
    for i in f:
        nf.writelines(i+'\n')
    print(x)
    print(f)

    # don't like how i'm recreating folder path in both functions
    
createFolder(folderName)
createfile(folderName,fileName)
    
