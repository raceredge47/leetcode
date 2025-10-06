class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)-1):
            num1 = nums[i]
            for j in range(len(nums[i+1::])):
                num2 = nums[i+1+j]
                sum = num1 + num2
                if sum == target:
                    return [i, i+1+j]