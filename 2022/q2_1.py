import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n")
#points
draw,win,lose=3,6,0
po={'X':1,'Y':2,'Z':3}
su=0
di={'A':'X','B':'Y','C':'Z'}
for i in input_str:
    i=i.split(" ")
    i[0]=di[i[0]]
    if(i[0]=='X'):
        if(i[1]=='Y'):
            su=su+win+po[i[1]]
        elif(i[1]=='X'):
            su=su+draw+po[i[1]]
        elif(i[1]=='Z'):
            su=su+lose+po[i[1]]
    elif(i[0]=='Y'):
        if(i[1]=='Z'):
            su=su+win+po[i[1]]
        elif(i[1]=='Y'):
            su=su+draw+po[i[1]]
        elif(i[1]=='X'):
            su=su+lose+po[i[1]]
    elif(i[0]=='Z'):
        if(i[1]=='X'):
            su=su+win+po[i[1]]
        elif(i[1]=='Z'):
            su=su+draw+po[i[1]]
        elif(i[1]=='Y'):
            su=su+lose+po[i[1]]
print(su)