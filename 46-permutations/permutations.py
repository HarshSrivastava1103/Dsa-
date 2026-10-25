class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        ans = [
            [[0]],
            [[1, 0], [0, 1]],
            [
                [2, 1, 0], [1, 2, 0], [1, 0, 2],
                [2, 0, 1], [0, 2, 1], [0, 1, 2]
            ]
        ]

        n = len(nums)

        if n <= 3:
            return [[nums[i] for i in p] for p in ans[n - 1]]

        from itertools import permutations
        return [list(p) for p in permutations(nums)]

            