class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d=Counter(s)
        maximum= max(d.values())
        minimum=min(d.values())

        return maximum==minimum

        