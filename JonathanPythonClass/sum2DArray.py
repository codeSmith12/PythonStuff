array = [
[1,2,3,4,5,6],
[9,12,55,23],
[20,99,1000],
]
def sumArray(array):
    sum = 0
    for ary in array: # loop through each array
        for num in ary: # loop through each item in an array
            sum += num
    print(sum)

sumArray(array)
