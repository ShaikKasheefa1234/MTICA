def extract_consonant(s):
    consonant=''
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz':
            consonant=i
    return consonant
str1=input()
a=extract_consonant(str1)
print("consonant in:'",str1,"'is",a)



