# class Solution:
#     def reverseWords(self, s: str) -> str:
        # s=s.strip()
        # print(s)
        # words=s.split()
        # print(words)
        # rev_words= words[::-1]
        # print(rev_words)
        # return " ".join(rev_words)
    


class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        w=s.split()
        rev_word=w[::-1]
        return " ".join(rev_word)
