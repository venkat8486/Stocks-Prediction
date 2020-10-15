import os, fnmatch

listOfFiles = os.listdir('.')
pattern = "bonus*.txt"
with open('FilesList_Bonus.txt','w') as writefile:
    for entry in listOfFiles:    
        if fnmatch.fnmatch(entry, pattern):
            writefile.write(entry)
            writefile.write('\n')