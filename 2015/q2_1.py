import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n")
sum=0
for i in input_str:
    j=i.split("x")
    a,b,c=int(j[0]),int(j[1]),int(j[2])
    l,b,h=a*b,b*c,a*c
    surface_area=2*(l+b+h)
    sum=sum+surface_area+min(l,b,h)
print(sum)