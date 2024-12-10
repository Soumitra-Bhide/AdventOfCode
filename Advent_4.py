with open("Advent_4.txt", 'r') as Advent_4:
    rows=Advent_4.read().splitlines()

grid=[]
temp=[]
directions=[(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1),(0,1)]
word="XMAS"
split_word=list(word)


for i in range(len(rows)):
        temp=list(rows[i])
        grid.append(temp)


count=0
for i in range(len(grid)):
      for j in range(len(grid[i])):
            if grid[i][j]==split_word[0]:
                  for k,l in directions:
                        end_row=i+(len(split_word)-1)*k
                        end_column=j+(len(split_word)-1)*l
                        if not (0 <= end_row < len(grid) and 0 <= end_column < len(grid[i])):
                              continue
                    
                        flag=True

                        for m in range(1,len(split_word)):
                            next_row_check = i + m*k
                            next_column_check= j + m*l
                            if grid[next_row_check][next_column_check] != split_word[m]:
                                  flag=False
                                  break
                        
                        if flag==True:
                              count+=1

                    
print(count)                                         
                  
##############################################################################



count2 = 0
directions2 = [(1, 1), (1, -1), (-1, -1), (-1, 1)]


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if not (0 <= i+1 < len(grid) and 0 <= i-1 < len(grid) and 0 <= j+1 < len(grid[i]) and 0 <= j-1 < len(grid[i])):
            continue
        if grid[i][j] == "A":
            M_count=0
            M_position=[]
            for k, l in directions2:
                if grid[i+k][j+l] == "M":
                     M_count+=1
                     temp=(k,l)
                     M_position.append(temp)
            if M_count==2:
                if grid[i-M_position[0][0]][j-M_position[0][1]]=="S" and grid[i-M_position[1][0]][j-M_position[1][1]]=="S":
                    count2+=1

print(count2)
              
                              

                        
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  
                  


                             
                        
                                    
                              