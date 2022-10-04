# [1,2,3,4,5,6], 10

def twoSum(nums, target):
    complements = {}
        
    for num in nums:
        if (num in complements):
            return (num, complements[num])
        else:
            complements[target - num] = num
    return (-1,-1)


print(twoSum([1,2,3,4,5,6], 0))