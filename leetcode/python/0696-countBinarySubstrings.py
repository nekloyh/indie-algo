class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        length, res, temp = len(s), 0, [0]
        for i in range(1, length):
            if s[i] != s[i - 1]:
                temp.append(i)
        temp.append(length)
        print(temp)
        for i in range(1, len(temp) - 1):
            res += min(temp[i] - temp[i - 1], temp[i + 1] - temp[i])
                 
        return res
        
def main():
    s = Solution()
    print(s.countBinarySubstrings("10101"))
    
if __name__ == "__main__":
    main()
    