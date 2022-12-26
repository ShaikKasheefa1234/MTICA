def count_Specialcharacters(s):
    specialcharacters=0
    for i in s:
        if i in 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz1133434':
            specialcharacters+=1
    return specialcharacters

str1=input()
a=count_Specialcharacters(str1)
print("No of specialcharacters in:'",str1,"'is",a)
