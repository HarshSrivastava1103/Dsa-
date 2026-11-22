from bisect import bisect_left
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        # Transform nums: +1 for target, -1 otherwise
        arr = [1 if x == target else -1 for x in nums]
        
        prefix = 0
        seen = [0]  # prefix sums seen so far
        res = 0

        for x in arr:
            prefix += x # running sum
            # count how many previous prefix sums are lesser than current
            idx = bisect_left(seen, prefix)
            res += idx
            # insert current prefix to keep list sorted
            seen.insert(idx, prefix)
        
        return res