'''Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.'''

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # First solution
        # return len(nums) != len(set(nums))
        
        # Second solution
        checked_nums = dict()
        for num in nums:
            checked_nums[num] = checked_nums.get(num, 0) + 1
            if checked_nums[num] > 1:
                return True
        return False
    
a = Solution()
nums = [1,1,1,3,3,4,3,2,4,2]
print(a.containsDuplicate(nums))
