import re

with open("Advent_3.txt","r") as Advent_3:
    text=Advent_3.read()


def patternMulti(x):
    output=0
    pattern= r'mul\((\d+),(\d+)\)'
    y= re.findall(pattern,x)
    for i in range(len(y)):
        temp=int(y[i][0])*int(y[i][1])
        output+=temp
    return output
    
ans=patternMulti(text)
print(ans)  

##########################################################3

disable= r"don\'t\(\)"
enable=r"do\(\)"

suppIndex=[]
enabIndex=[]

for suppressor in re.finditer(disable,text):
    suppIndex.append(suppressor.start())

for enabler in re.finditer(enable,text):
    enabIndex.append(enabler.start())


condText=""
flag=1
j=0
k=0
for i in range(len(text)):
    if i < suppIndex[j] and flag==1:
        condText+=text[i]
    if i == suppIndex[j]:
        flag=0
        if j < len(suppIndex)-1:
                j+=1
    if i ==enabIndex[k]:
        flag=1
        if k < len(enabIndex)-1:
                k+=1

condAns=patternMulti(condText)
print(condAns)
