nums = [2,4,6,3,7,10]
summed = []
for i in range(len(nums)):
    if i == 0:
        summed.append(nums[i])
    elif i > 0:
        summed.append(summed[i-1] + nums[i])

for num in summed:
    print(num)