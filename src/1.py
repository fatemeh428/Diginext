
def repeat_str_and_repeat_a(str, n):
    
    #tekrar kol word
    word = int(n/len(str))
    
    #tekrar char
    char= n - (len(str)*word)
   
    
    str1 = word*str
    
    
    str2= str[:char]
    
    str3= str1+str2
    repeat_a= 0
    for i in str3:
        if i =='a':
            repeat_a+=1
    return(repeat_a)
