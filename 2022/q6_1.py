import sys
input_str = sys.stdin.read()
for i in range(len(input_str)-3):
    se=len(set(input_str[i:i+4]))
    #print(i,set(input_str[i:i+4]),input_str[i:i+4])
    if(se==4):
        print(i+4)
        break