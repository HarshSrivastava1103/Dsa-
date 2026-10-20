class Solution:
    i = 0

    def decodeString(self, s: str) -> str:
        res = ""
        while self.i < len(s) and s[self.i] != "]":
            if not s[self.i].isdigit():
                res += s[self.i]
                self.i += 1
            else:
                n = 0
                while self.i < len(s) and s[self.i].isdigit():
                    n = n * 10 + ord(s[self.i]) - 48
                    self.i += 1
                self.i += 1
                t = self.decodeString(s)
                self.i += 1
                while n > 0:
                    res += t
                    n -= 1
        return res