# Last updated: 12/4/2025, 11:22:31 AM
1class KthLargest:
2
3    def __init__(self, k: int, nums: List[int]):
4        self.k = k
5        self.minheap = nums
6        heapq.heapify(self.minheap)
7
8        while len(self.minheap) > self.k:
9            heapq.heappop(self.minheap)
10
11    def add(self, val: int) -> int:
12        heapq.heappush(self.minheap, val)
13        
14        while len(self.minheap) > self.k:
15            heapq.heappop(self.minheap)
16        
17        return self.minheap[0]
18
19        
20
21
22# Your KthLargest object will be instantiated and called as such:
23# obj = KthLargest(k, nums)
24# param_1 = obj.add(val)