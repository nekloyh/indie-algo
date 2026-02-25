from typing import List

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        tmpArr = []
        
        for num in arr:
            ones = bin(num).count('1')
            tmpArr.append((num, ones))
        
        tmpArr.sort(key=lambda x: (x[1], x[0]))
        
        return [x[0] for x in tmpArr]
    
def main():
    s = Solution()
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print(s.sortByBits(arr))

if __name__ == "__main__":
    main()
    