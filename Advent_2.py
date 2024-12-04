reads=[]
bad_reads=[]
good_reads=[]

with open("Advant_2.txt", "r") as Advant_2:
    lines = Advant_2.readlines()
    reads = [list(map(int, line.split())) for line in lines]

def safe(list,i):
    if all(abs(j-k)<=3 for j,k in zip((list[i]),list[i][1:])):
        if all(j > k for j,k in zip((list[i]),list[i][1:])) or all(j < k for j,k in zip((list[i]),list[i][1:])):
            return True


for i in range(len(reads)):
    if (safe(reads,i)):
            good_reads.append(reads[i])
    else:
        bad_reads.append(reads[i])
            

print(len(good_reads))

############################################################################################################


for i in range(len(bad_reads)):
   sublists= [bad_reads[i][:j] + bad_reads[i][j+1:] for j in range(len(bad_reads[i]))]
   for l in range(len(sublists)):
       if safe(sublists,l):
            good_reads.append(bad_reads[i])
            break
    

print(len(good_reads))



        
