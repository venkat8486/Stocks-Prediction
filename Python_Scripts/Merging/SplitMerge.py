with open('FilesList_Splits.txt','r') as readfilename:
    j=0
    for line in readfilename.readlines():
        j=j+1
        #print(j)
        line=line.replace("\n","")
        i=0
        with open(line,'r') as readfile:
            line=line.replace("splits_","")
            line=line.replace(".txt","")
            for line1 in readfile.readlines():
                    i=i+1
                    #print(j,i)
                    if i>1:
                        #print(line1)
                        line1=line1.replace("  Add to Watchlist","")
                        line1=line1.replace("  Add to Portfolio","")                           
                        with open('MergedSplit.txt','a') as mergefile:
                            if i==2 and j==1:
                                #print(line1)
                                mergefile.write('"Year"|' + line1)
                            elif i>2:
                                mergefile.write('"' + line + '"|' + line1)                                

            
        
        
   


