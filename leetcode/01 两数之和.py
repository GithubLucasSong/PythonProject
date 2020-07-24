"""
1. 两数之和
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。



示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

###########################################################################################################

# 5856 ms	14.5 MB

# nums = [2, 7, 11, 15,]
# target = 23
#
# def twoSum(nums,target):
#
#     for i in range(len(nums)):
#         for j in range(i+1,len(nums)):
#             # print(nums[i],nums[j])
#             if nums[i]+nums[j] == target:
#                 return [i,j]
#
# print(twoSum(nums,target))






###########################################################################################################



#56 ms	15.2 MB


nums = [2, 7, 11, 15, ]
target = 9

def twoSum(nums, target):
    cache = {}
    for i in range(len(nums)):
        cur = target - nums[i]
        if nums[i] in cache:
            return (cache[nums[i]], i)
        cache[cur] = i
print(twoSum(nums, target))


###########################################################################################################