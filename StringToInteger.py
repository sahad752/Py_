class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        
        if not s:
            return 0
        negative = False
        out = 0
        
        if s[0]=="+":
            negative = False
        elif s[0]=="-":
            negative = True
        elif not s.isnumeric :
            return 0 
        else :
            out = ord(s[0]) - ord("0")
        for i in range(1,len(s)):
            if s[i].isnumeric():
                out = out * 10 +(ord(s[i])- ord("0"))
                if not negative and out >= 2147483648:
                    return 2147483648
                if negative and out >= 2147483648:
                    return -2147483648
            else:
                break
        if not negative:
            return out 
        else :
            return -out
