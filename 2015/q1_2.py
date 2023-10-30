import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n\n")
str=input_str[0]
flo=0
count=0
for i in str:
    if i=="(":
        flo=flo+1
    elif i==")":
        flo=flo-1
    if(flo==-1):
        print(count+1)
        break
    count=count+1
print(flo)