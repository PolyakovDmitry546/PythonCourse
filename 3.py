# здача 1

nums = [-2,1,-3,4,-1,2,1,-5,4]

startindex = 0
endindex = 0
maxsum = 0
for i in range(len(nums)):
    sum = 0
    j = i
    while j < len(nums):
        sum += nums[j]
        if sum >= maxsum:
            maxsum = sum
            startindex = i
            endindex = j
        j += 1

print(nums[startindex:endindex + 1])
print("Max sum:", maxsum)

# задача 2

intervals = [[1,3],[2,6],[8,10],[15,18]]

intervals.sort(key=lambda x: (x[0], x[1]))

startindex = 0
resultlist = []
for i, value in enumerate(intervals):
    if intervals[startindex][1] < value[0]:
        resultlist.append([intervals[startindex][0], intervals[i - 1][1]])
        startindex = i
resultlist.append([intervals[startindex][0], intervals[-1][1]])

print(resultlist)




