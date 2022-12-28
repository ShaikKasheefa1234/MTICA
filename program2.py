string='''
practice problems for List Com pre hension in python.
'''


wordsLst=string.split(' ')
#print(wordsLst)
wordsLst=[i.strip("\n") for i in wordsLst]
#print(wordsLst)
ans={i:i[::-1] for i in wordsLst}
print(ans)
