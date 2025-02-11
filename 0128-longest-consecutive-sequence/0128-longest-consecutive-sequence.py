class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        max_seq = 0
        for n in nums_set:
            if (n - 1) not in nums_set:
                leng = 1 
                while (n + leng) in nums_set:
                    leng += 1
                max_seq = max(leng, max_seq)

        return max_seq

        #T: O(n)
        #S: O(n)