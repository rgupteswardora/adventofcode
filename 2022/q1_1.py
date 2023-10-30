import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n\n")
ma=0
for i in input_str:
    num=[int(number) for number in i.split("\n")]
    ma=max(sum(num),ma)
print(ma)