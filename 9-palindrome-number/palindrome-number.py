class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        x_copy = x
        rev = 0
        while x > 0:
            rem = x % 10
            rev = rev * 10 + rem
            x //= 10
        return rev == x_copy

sol = Solution()
print(sol.isPalindrome(121))  # True
#HARSH 