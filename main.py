class Solution(object):
    def twoSum(self, nums, target):
        nums_position = {}
    
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_position:
                return [nums_position[complement], i]

            nums_position[num] = i

solution = Solution()
print(solution.twoSum([2, 7, 9, 11, 15], 9))
