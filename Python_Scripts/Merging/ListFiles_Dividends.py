import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "dividends*.txt"
with open('FilesList_Dividends.txt','w') as writefile:
    for entry in listOfFiles:    
        if fnmatch.fnmatch(entry, pattern):
            writefile.write(entry)
            writefile.write('\n')