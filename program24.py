def remove_duplicates(s):
    str2=''
    for i in s:
        if i not in str2:
            str2 +=i
            #print (str2)
    return str2
        
str1=input("Enter your text: ")
print("Without duplicates: ",remove_duplicates(str1))
                                                   
