# Last updated: 11/21/2025, 8:46:41 PM
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [[] for i in range(len(nums)+1)]
        freq = defaultdict(int)
        res = []

        for num in nums: 
            freq[num] += 1
        
        for key, value in freq.items():
            bucket[value - 1].append(key)

        for i in reversed(bucket):
            if i:
                while i:
                    res.append(i.pop())
                    k -= 1
            if k == 0:
                return res