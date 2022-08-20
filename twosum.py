class Solution:
    def twoSum(self, nums, target):
        num_dict = {} # val : index

        for index, val in enumerate(nums):
            diff = target - val
            if diff in num_dict:
                return [num_dict[diff], index]
            else:
                num_dict[val] = index





"""         diffs = {}
        
        for index, val in enumerate(nums):
            diffs[target - val] = [index, val]
        for index, val in enumerate(nums):
            try:
                diffs[val]
                result = [index, diffs[val][0]]
                return result
            except:
                continue """
        
        #{2: 7, 7: 2, 11: -2, 15: -6}
        #[2, 7, 11, 15]
        
"""         for index, val in enumerate(nums):
            for index_2, val_2 in enumerate(nums[1::]):
                result = [index, index_2] """
                    
        #return result

solution = Solution()
print(solution.twoSum([2,7,11,15], 9))