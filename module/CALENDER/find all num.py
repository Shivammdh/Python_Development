import re

def chekdigit(sentence):
    s = [str(s) for s in re.findall(r'-?\d+\.?\d*', sentence)]
    if(len(s)==0):
        return ["NA"]
    else:
        return s
if __name__=='__main__':
    fptr=open('file1.txt','w')
    sentence = input()
    result=chekdigit(sentence)
    fptr.write('\n'.join(result))
    fptr.write('\n')
    fptr.close()
