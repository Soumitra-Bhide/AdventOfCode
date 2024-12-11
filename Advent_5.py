rules=[]
updates=[]


with open("Advent_5.txt","r") as Advent_5:
    lines=Advent_5.readlines()

for i in range(1176):
    as_list=lines[i].split("|")
    temp=(int(as_list[0]),int(as_list[1]))
    rules.append(temp)

for j in range(1177,1375):
    as_list=lines[j].strip().split(",")
    updates.append([int(x) for x in as_list]) 



correct_updates=[]

for update in updates:
    Flag=True
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                Flag=False
                break
    if Flag==True:
        correct_updates.append(update)

ans=[]
for CU in correct_updates:
    middleIndex=int((len(CU) - 1)/2)
    ans.append(CU[middleIndex])

print(sum(ans))

#####################################

incorrect_updates = [item for item in updates if item not in correct_updates]

def reorder(update,rules, corrected_list):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            a=update.index(rule[0])
            b=update.index(rule[1])
            if a < b:
                continue
            else:
                update[a],update[b]=update[b],update[a]
                return reorder(update,rules,corrected_list)
    corrected_list.append(update)

corrected_updates=[]

for ICU in incorrect_updates:
    reorder(ICU,rules,corrected_updates)

ans2=[]
for CDU in corrected_updates:
    middleIndex=int((len(CDU) - 1)/2)
    ans2.append(CDU[middleIndex])

print(sum(ans2))






