'''Lst1=["Sadan","SUV","","","Pickup",'',' ']
ans=[]
for i in Lst1:
    if i:
        ans.append(i)
print(ans)'''



Lst1=["Sadan","SUV","","","Pickup",'',' ']
ans=[i for i in Lst1 if i]
#for i in Lst1:
    #if i:
       # ans.append(i)
print(ans)
