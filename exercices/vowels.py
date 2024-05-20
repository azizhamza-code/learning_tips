class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U'] 
        if not any(vowel in s for vowel in vowels):
            return s
        s = list(s)
        track = []
        for i , c in enumerate(s) : 
            if c not in vowels:
                pass
            else:
                track.append((i,c))
        sorted_tracked = sorted(track, key=lambda item : -item[0])
        for item0,item in zip(sorted_tracked, track):
            s[item[0]] = item0[1]
        return "".join(s)

if __name__ == "__main__":
    s = Solution().reverseVowels('hamze')
    print(s)