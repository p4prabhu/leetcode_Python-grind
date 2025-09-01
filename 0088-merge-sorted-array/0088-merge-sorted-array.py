# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         for i in range(m,m+n):
#             nums1[i]=nums2[i-m]

#         nums1.sort()
#         return nums1

        
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i=m-1
        j=n-1
        k=m+n-1
        while i>=0 and j>=0:
            n1,n2=nums1[i],nums2[j]
            if nums1[i]>nums2[j]:
                nums1[k]=n1
                i-=1
               
            else:
                nums1[k]=n2
                j-=1
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

      








     