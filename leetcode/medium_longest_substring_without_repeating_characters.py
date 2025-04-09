'''Given a string s, find the length of the longest substring without duplicate characters.

'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # char_set = set()
        # left = 0
        # right = 0
        # max_length = 0
        
        
        # while left < len(s):
        #     if s[right] not in char_set:
        #         char_set.add(s[right])
        #         max_length = max(max_length, len(char_set))
        #         right += 1
        #     else:
        #         left += 1
        #         right = left
        #         char_set.clear()
        # return max_length
        
        char_set = set()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)
        
        return max_length
