def extract_Specialcharacters(s):
    specialcharacters=0
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz1133434':
            specialcharacters=i
    return specialcharacters

str1=input()
a=extract_Specialcharacters(str1)
print("specialcharacters in:'",str1,"'is",a)


