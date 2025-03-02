class Solution:

    def isValid(self, s: str) -> bool:
        closed = {')': '(', ']': '[', '}': '{'}
        
        stack = []

        for char in s:
            if char not in closed:
                stack.append(char)
                continue
            if not stack or closed[char] != stack.pop():
                return False
        return not stack
        
        
res = Solution()
print(res.isValid('(())'))