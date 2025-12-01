# class Solution:
#     def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
#         greatest = max(candies)
#         result=[] 
#         for candy in candies:
#             if candy + extraCandies >= greatest:
#                 result.append(True)
#             else:
#                 result.append(False)  
#         return result     

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        mx= max(candies)
        l=[]
        for can in candies:
            if can+extraCandies>=mx:
                l.append(True)
            else:
                l.append(False)
        return l

