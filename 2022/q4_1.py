import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n")
count=0
for i in input_str:
    cou=set()
    i=i.split(",")
    x,y=i[0].split("-"),i[1].split("-")
    x1,x2=int(x[0]),int(x[1])
    y1,y2=int(y[0]),int(y[1])
    set1=set([i for i in range(x1,x2+1)])
    set2=set([i for i in range(y1,y2+1)])
    if(len(set1)>=len(set2)):
        for j in set2:
            if j in set1:
                cou.add(j)
        if len(cou)!=0 and len(cou)==len(set2):
            count=count+1
    elif(len(set1)<len(set2)):
        for j in set1:
            if j in set2:
                cou.add(j)
        if len(cou)!=0 and len(cou)==len(set1):
            count=count+1
print(count)
