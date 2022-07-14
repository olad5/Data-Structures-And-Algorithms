# contains duplicate
class Solution:
    def containsDuplicate(self, nums) :
        if len( nums ) == 0 :
            return False
        hash_table = {}
        for num in nums:
            if hash_table.get(num, False) == True:
                return True
            hash_table[ num ] = True


        return False


if __name__ == "__main__":
    sol  = Solution()
    print(sol.containsDuplicate([1,2,3,1]) )
    print(sol.containsDuplicate([1,2,3,4]) )
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]) )
