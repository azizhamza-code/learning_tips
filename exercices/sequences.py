# I am exercising myself, do not help me with the solution 
# Only complete what I already know and start

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        self.validate_words(word1, word2)
        # do not help me with the solution , only complete what I already started
        rs = ""
        indix = 0
        while(indix < len(word1) and indix < len(word2)):
            rs += word1[indix] + word2[indix]
            indix +=1
        if indix < len(word1):
            rs += word1[indix:]
        else : 
            rs += word2[indix:]
        return rs
    def validate_words(self, word1: str, word2: str) -> None:
        assert isinstance(word1, str), "word1 is not a string"
        assert isinstance(word2, str), "word2 is not a string"
        
        if not word1.islower():
            word1 = word1.lower()
        if not word2.islower():
            word2 = word2.lower()
        
        assert len(word1)>0 and len(word2)>0

if __name__ == "__main__":
    s = Solution()
    print(s.mergeAlternately("abcd", "pq")) # "adbecf"