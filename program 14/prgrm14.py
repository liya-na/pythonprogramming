col1=['red','blue','yellow','white']
col2=['green','blue','yellow']
print(col1)
print(col2)
for i in range(len(col1)):
    if col1[i]not in col2:
        print("the color is:",col1[i])