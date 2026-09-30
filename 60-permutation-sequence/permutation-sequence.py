factorials = [1, 1]
mult = 1
for i in range(2, 10):
    mult *= i
    factorials.append(mult)

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        res = ""
        s = set()
        for i in range(n, 0, -1):
            curr_digit = 1
            while curr_digit in s:
                curr_digit += 1
            while k > factorials[i - 1]:
                curr_digit += 1
                while curr_digit in s:
                    curr_digit += 1
                k -= factorials[i - 1]
            res += str(curr_digit)
            s.add(curr_digit)
        return res