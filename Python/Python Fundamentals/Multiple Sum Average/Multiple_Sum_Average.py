# Multiples
for num in range(1, 1001, 2): #Part 1: for num in the range starting at 1 and ending at 1000, print every other number
    print num

for num in range(5, 1000001, 5): #part 2: for num in the range starting at 5 and ending at 1000001, iterate and print every fifth number
    print num


# Sum List
a = [1, 2, 5, 10, 255, 3]
b = sum(a) #sum all elements in a
print b


# #Average List
a = [1, 2, 5, 10, 255, 3]
ave = sum(a)/len(a) #add the value of each element to get the sum, then divide by the length of the list
print ave