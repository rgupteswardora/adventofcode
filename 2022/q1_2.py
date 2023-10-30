import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n\n")
ma=[]
for i in input_str:
    num=[int(number) for number in i.split("\n")]
    ma.append(sum(num))
ma.sort()
print(sum(ma[len(ma)-3:]))
#print(sum(ma[len:]))