def count_Digit(s):
    n_Digit=0
    for i in s:
        if i in '123456789':
            n_Digit+=1
    return n_Digit

str1=input()
a=count_Digit(str1)
print("No of digits in:'",str1,"'is",a)
