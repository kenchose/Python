def identitylist(lst):
    newStr = ''
    total = 0
    for elem in lst:
        if isinstance(elem, int) or isinstance(elem, float):
            total += elem
        elif isinstance(elem, str):
            newStr += elem + ' '
    if newStr and total:
        print "The list you entered is of mixed type"
        print "String:", newStr
        print 'Sum:', total

    elif newStr:
        print "The string you entered is of string type"
        print 'String:', newStr
   
    else: 
        print "The list you entered is of integer type"
        print 'Sum:', total

# #input
# l = ['magical unicorns',19,'hello',98.98,'world']
# #output
# "The list you entered is of mixed type"
# "String: magical unicorns hello world"
# "Sum: 117.98"


# # input
# l = [2,3,1,7,4,12]
# #output
# "The list you entered is of integer type"
# "Sum: 29"



# # input
# l = ['magical','unicorns']
# #output
# "The list you entered is of string type"
# "String: magical unicorns"

























