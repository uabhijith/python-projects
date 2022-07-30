#👾 🤖😈
row1=["🤖","🤖","🤖"]
row2=["🤖","🤖","🤖"]
row3=["🤖","🤖","🤖"]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position=input("Where do you want to put the treasure?")
horz=int(position[0])
vert=int(position[1])
map[vert-1][horz-1]="😈"
#print(map[0][0])
print(f"{row1}\n{row2}\n{row3}")