'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False
        
#         num = x
#         reversed_x = 0
        
#         while num != 0:
#             reversed_x = reversed_x * 10 + num % 10
#             num = num // 10
#         return x == reversed_x
    

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x) == str(x)[::-1]
    
    
sol = Solution()

print(sol.isPalindrome(122))