class Solution:
    def twoSum(self, nums, target) :
        if len(nums) == 2:
            return [0, 1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums [j] == target:
                    return [i,j]
            

if __name__ == "__main__":
    sol  = Solution()
    print(sol.twoSum([2,7,11,15], 9) )
    print(sol.twoSum([3,2,4], 6) )
    print(sol.twoSum([3,3], 6) )
