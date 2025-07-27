class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix=strs[0]
        for i in range(len(prefix)):
            for words in strs:
                if i == len(words) or prefix[i] != words[i]:
                    return prefix[:i]
        return prefix
              
               
           
        