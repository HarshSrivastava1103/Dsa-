class Solution:
    def addDigits(self, num: int) -> int:
        if num <= 9:
            return num

        while num > 9:
            d = 0
            while num > 0:
                d += num % 10
                num = num // 10
            num = d

        return num
        