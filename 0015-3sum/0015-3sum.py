class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            if i > 0 and a == nums[i - 1]:
                continue

            l = i +1
            r = len(nums) - 1
            while l < r:
                _sum = a + nums[l] + nums[r]

                if _sum > 0:
                    r -= 1
                elif _sum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

#T: O(n2)
#S: O(n)