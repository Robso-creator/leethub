# hash map key = num and value = index

# [1,2,3]
# target = 4
#   i= 2
#   num=3
#   dict_index = { 1: 0, 2: 1, }
#   vl_search = 1
#
# return [2, 0]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        saw_dict = {}

        for i, num in enumerate(nums):
            _target = target - num
            if _target in saw_dict:
                return [i, saw_dict[_target]]

            saw_dict[num] = i
        
#: t: O(N)
#: s: O(N)