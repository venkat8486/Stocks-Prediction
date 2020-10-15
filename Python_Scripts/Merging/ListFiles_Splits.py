import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "splits*.txt"
with open('FilesList_Splits.txt','w') as writefile:
    for entry in listOfFiles:    
        if fnmatch.fnmatch(entry, pattern):
            writefile.write(entry)
            writefile.write('\n')