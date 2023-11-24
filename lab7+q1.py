k=str(input())
c=0
s=0
for i in k:
    if ord("A")<=ord(i)<=ord("Z"):
        c+=1
    else:
        s+=1
if s>=1:
    print("no")
else:
    print("yues")
