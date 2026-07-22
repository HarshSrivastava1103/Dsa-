class Solution:
    def twoSum(self, nums, target):
        num_map = {}  # Dictionary to store number and its index
        #DSA
        for i in range(len(nums)):
            complement = target - nums[i]
            
            # If complement already exists in dictionary
            if complement in num_map:
                return [num_map[complement], i]
            
            # Store current number with its index
            num_map[nums[i]] = i