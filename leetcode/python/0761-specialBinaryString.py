class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if len(s) == 2:
            return s
        diff, st, blocks = 0, 0, []
        for i in range(len(s)):
            if s[i] == '1':
                diff += 1
            else:
                diff -= 1
            
            if diff == 0:
                inner = self.makeLargestSpecial(s[st + 1: i])
                blocks.append('1' + inner + '0')
                st = i + 1
            
        blocks.sort(reverse=True)
        return ''.join(blocks)

def main():
    s = Solution()
    print(s.makeLargestSpecial("11011000"))

if __name__ == "__main__":
    main()
    