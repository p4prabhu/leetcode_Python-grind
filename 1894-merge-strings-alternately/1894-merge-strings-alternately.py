class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        st=[]
        i=j=0
        len1=len(word1)
        len2=len(word2)
        while i <len1 and j<len2:
            st.append(word1[i])
            st.append(word2[j])
            i+=1
            j+=1
        if i<len1:
            st.append(word1[i:])
        else:
            st.append(word2[j:])

        return "".join(st)


      
            
       







        

        
            

        
        