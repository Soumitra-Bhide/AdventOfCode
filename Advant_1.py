import collections

ID_1=[]
ID_2=[]
Diff=[]

with open("Advant_1.txt","r") as Advant_1:
    lines=Advant_1.readlines()

for i in lines:
    as_list=i.split("   ")
    ID_1.append(int(as_list[0]))
    ID_2.append(int(as_list[1]))


ID_1.sort()
ID_2.sort()

for i in range(len(ID_1)):
    Diff.append(abs(ID_1[i]-ID_2[i]))


print(sum(Diff))

############################################################

Uq_ID_1= list(set(ID_1))
sum=0

if len(ID_1)==len(Uq_ID_1):
    counter=dict(collections.Counter(ID_2))
    for i in range(len(ID_1)):
        temp= ID_1[i]*counter.get(ID_1[i],0)
        sum=sum+temp
    print(sum)

            
        
