class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        p = s.count('1')
        return '1' * (p - 1) + '0' * (len(s) - p) + '1'