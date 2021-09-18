l=[name for name in input().split(',')]

for i in l:
    result = i.endswith('sh')
    if(result):
        print(i)