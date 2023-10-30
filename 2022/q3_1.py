import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n")
su=0
for i in input_str:
    ch=set()
    le=len(i)
    #print(i)
    s1,s2=i[:le//2],i[le//2:]
    for char1 in s1:
        for char2 in s2:
            if(char1==char2):
                ch.add(char1)
    for char in ch:
        if char.islower():
            su=su+(ord(char)-96)
        else:
            su=su+(ord(char)-64+26)
print(su)
