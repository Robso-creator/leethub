class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_hash = defaultdict(int)

        for n in nums:
            nums_hash[n] += 1
        print(nums_hash.get)
        return sorted(nums_hash, key=nums_hash.get, reverse=True)[:k]