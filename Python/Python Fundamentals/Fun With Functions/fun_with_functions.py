# Odd/Even
# def odd_even (num):
#     numIs = 'Number is '
#     even = '. This is an even number.'
#     odd = '. This is an odd number.'
#     for num in range(1, 1001, 1):
#         if num % 2 == 0:
#             print '{}{}{}'.format(numIs, num, even)
#         if num % 2 != 0:
#             print '{}{}{}'.format(numIs, num, odd)
# odd_even(1000)

# Multiply
def multiply(arr,num):
    for x in range(0, len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
output [10, 20, 50, 80 ]


# Hascker Challenge
arr = []
def layered_multiples(list, num):
    for elem in range(len(list)):
        list[elem] *= num
    return list
res = layered_multiples([2,4,5],3)
arr.append(res)
print arr

def layered_multiples(arr):
    print arr
    new_array = []
    for x in arr:
        val_arr = []
        for i in range(0,x):
            val_arr.append(1)
        new_array.append(val_arr)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x


