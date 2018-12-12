word_list = ['hello','world','my','name','is','Anna']
char = 'o'
newList = []
for elem in word_list:
    if char in elem:
        newList.append(elem)
print newList
        
