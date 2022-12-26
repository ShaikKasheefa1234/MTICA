def extract_Digit(s):
    temp_Digit=''
    for i in s:
        if i in '0123456789':
            temp_Digit+=i
    return temp_Digit
str1=input()
a=extract_Digit(str1)
print("digits in:'",str1,"' is",a)
