class Solution:
    def bit2dec(self, s: str):
        dec = 0
        for bit in s:
            dec <<= 1
            if bit == "1":
                dec += 1
        return dec
    
    def numSteps(self, s: str) -> int:
        dec = self.bit2dec(s)
        res = 0
        
        while dec != 1:
            res += 1
            dec = (dec + 1) if dec % 2 == 1 else (dec >> 1)
            
        return res        


def main():
    s = Solution()
    bits = "1101"
    print(s.numSteps(bits))
    
if __name__ == "__main__":
    main()
    