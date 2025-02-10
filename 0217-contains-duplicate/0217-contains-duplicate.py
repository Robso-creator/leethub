class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        saw_dict = {}

        for num in nums:
            if num in saw_dict:
                return True
            else:
                saw_dict[num] = 1
        return False
        
        #S: O(N)
        #T: O(N)