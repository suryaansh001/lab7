'''l=str(input())
m=l[ : :-1]
print(m)
print(l)'''
l=map(str,input().split())
m=[]
i=int(len(l))
while i >0:
    m.append(l[i])
    i-=1
print(m)