def removechar(txt):
    
    remove= 0
    for i in range(len(txt) -1):
        if (txt[i] == txt[i+1]):
            remove +=1
    return (remove)