import os
import collections

reads=[]

with open("Advant_2.txt", "r") as Advant_2:
    lines = Advant_2.readlines()
    reads = [list(map(int, line.split())) for line in lines]

count=0
for i in range(len(reads)):
    if all(abs(j-k)<=3 for j,k in zip((reads[i]),reads[i][1:])):
        if all(j > k for j,k in zip((reads[i]),reads[i][1:])) or all(j < k for j,k in zip((reads[i]),reads[i][1:])):
            print(reads[i])
            count=count+1

print(count)

            
        
