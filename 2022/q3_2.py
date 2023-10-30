import sys
input_str = sys.stdin.read()
input_str=input_str.split("\n")
su=0
for i in range(0,len(input_str),3):
    group=input_str[i:i+3]
    #print(group,"\n")
    ch=set()
    for char1 in group[0]:
        for char2 in group[1]:
            for char3 in group[2]:
                if(char1==char2):
                    if(char2==char3):
                        ch.add(char1)
    for char in ch:
        if char.islower():
            su=su+(ord(char)-96)
        else:
            su=su+(ord(char)-64+26)
print(su)