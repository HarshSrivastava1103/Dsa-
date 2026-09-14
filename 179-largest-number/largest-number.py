from functools import cmp_to_key

class Solution:

    def largestNumber(self, nums):
        # Convert integers to strings
        nums = list(map(str, nums))

        # Custom comparator
        def mycmp(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            return 0

        # Sort using custom comparator
        nums.sort(key=cmp_to_key(mycmp))

        # Handle case like [0, 0]
        if nums[0] == "0":
            return "0"

        # Join all strings
        return "".join(nums)