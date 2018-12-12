#Find and Replace
words = "It's thanksgiving day. It's my birthday,too!"
print words.find("day")
words = words.replace("day", "month")
print words


#Min and Max
x = [2,54,-2,7,12,98]
print min(x)
print max(x)


#First and Last
x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]
y = [x[0], x[len(x) - 1]]
print y


#New List
x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
firstList = x[:len(x)/2]
print firstList
secondList = x[len(x)/2:]
print secondList
secondList.insert(0, firstList)
print secondList
