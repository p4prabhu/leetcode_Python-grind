# class Solution:
#     def mergeAlternately(self, word1: str, word2: str) -> str:
#         st=[]
#         i=j=0
#         len1=len(word1)
#         len2=len(word2)
#         while i <len1 and j<len2:
#             st.append(word1[i])
#             st.append(word2[j])
#             i+=1
#             j+=1
#         if i<len1:
#             st.append(word1[i:])
#         else:
#             st.append(word2[j:])

#         return "".join(st)


      
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i=j=0
        s1=len(word1)
        s2=len(word2)
        l=[]
        while i < s1 and j < s2:
            l.append(word1[i])
            l.append(word2[j])
            i+=1
            j+=1
        if i<len(word1):
            l.append(word1[i:])
        else:

            l.append(word2[j:])
        return "".join(l)





        