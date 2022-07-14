# valid anagram
class Solution:
    def isAnagram(self, s, t) :
        if len( s )  != len(t) :
            return False
        return  ''.join(sorted( list(s) )) == ''.join(sorted( list(t) ))


if __name__ == "__main__":
    sol  = Solution()
    print(sol.isAnagram("anagram", "nagaram") )
    print(sol.isAnagram("rat", "car") )
    print(sol.isAnagram("rat", "art") )
