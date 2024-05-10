colors=["Orange", "Blue", "Green", "White", "Yellow", "Brow", "Cream"]
color_i_want="White"
length=len[colors]
count=0
while  count<length:
    print(colors[count])
    if colors[count]==color_i_want:
        print("They have color i want")
        break
    count +=1