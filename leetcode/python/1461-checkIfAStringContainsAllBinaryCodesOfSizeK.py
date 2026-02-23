class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        if k > len(s):
            return False
        
        temp = s[:k]
        setString: set[str] = {temp}
        
        for i in range(k, len(s)):
            temp = temp[1:] + s[i]
            setString.add(temp)
        
        return len(setString) == pow(2, k)

def main():
    s = Solution()
    print(s.hasAllCodes("0110", 2))

if __name__ == "__main__":
    main()
    