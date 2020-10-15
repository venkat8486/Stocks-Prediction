import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "rights*.txt"
with open('FilesList_Rights.txt','w') as writefile:
    for entry in listOfFiles:    
        if fnmatch.fnmatch(entry, pattern):
            writefile.write(entry)
            writefile.write('\n')