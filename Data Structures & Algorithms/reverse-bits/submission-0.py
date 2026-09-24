class Solution:
    def reverseBits(self, n: int) -> int:
        n=bin(n)[2:].zfill(32)
        nr=n[::-1]
        return int(nr,2)