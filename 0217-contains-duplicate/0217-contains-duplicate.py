class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw_dict = {}

        for num in nums:
            if num in saw_dict:
                return True
            else:
                saw_dict[num] = 1
        return False
        
        # nums.sort()

        # for i, _ in enumerate(nums):
        #     try:
        #         if nums[i] == nums[i+1]:
        #             return True
        #     except Exception:
        #         print('out of range')
        # return False

        # saw = defaultdict(int) #O(1)

        # for num in nums: # O(N)
        #     if num in saw:
        #         return True
        #     else:
        #         saw[num]+=1

        # return False

        #S: O(N)
        #T: O(N)