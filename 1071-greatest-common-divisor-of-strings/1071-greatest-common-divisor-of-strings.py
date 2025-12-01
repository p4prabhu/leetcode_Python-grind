# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
        # if str1+ str2 != str2+str1:
        #     return ""
        # size= math.gcd(len(str1), len(str2))
        # print(size)
        # return str2[:size]
        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2 =len(str1), len(str2)
        def isdivisor(l):
            if len1%l or len2%l:
                return False
            f1, f2 =len1//l, len2//l
            return str1[:l]*f1==str1 and  str1[:l]*f2==str2 


        for l in range(min(len1, len2),0,-1):
            if isdivisor(l):
                return str1[:l]
        return ""


        