class Solution:
    def countBits(self, n: int) -> int:
        cnt = 0
        while n > 0:
            cnt += 1
            n >>= 1
        return cnt 
    
    def concatenatedBinary(self, n: int) -> int:
        MOD = (10 ** 9) + 7
        res, nBits = 0, 0
        for i in range(1, n + 1):
            nBits = self.countBits(i)
            res = (res << nBits) | i
            res %= MOD
        return res
    
def main():
    s = Solution()
    number = 3
    print(s.concatenatedBinary(number))

if __name__ == "__main__":
    main()
    