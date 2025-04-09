'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}
        for i, num in enumerate(nums):
            pair_value = target - num
            if pair_value in nums_dict:
                return [nums_dict[pair_value], i]
            nums_dict[num] = i
        return []
    

answer = Solution()
print(answer.twoSum([1, 2, 4], 6)) # [1, 2]
