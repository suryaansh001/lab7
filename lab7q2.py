l=str(input())
space=" "
sp=0
count=0
for i in l:
    count+=1
    if i==space:
        sp+=1

print(count-sp)