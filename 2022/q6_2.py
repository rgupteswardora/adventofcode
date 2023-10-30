import sys
input_str = sys.stdin.read()
pt=0
for i in range(len(input_str)-3):
    se=len(set(input_str[i:i+4]))
    #print(i,set(input_str[i:i+4]),input_str[i:i+4])
    if(se==4):
        pt=i+4
        break
for j in range(pt,len(input_str)-13):
    if(len(set(input_str[j:j+14]))==14):
        print(j+14)
        break