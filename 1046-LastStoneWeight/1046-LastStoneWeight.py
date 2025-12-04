# Last updated: 12/4/2025, 3:39:12 PM
1class Solution:
2    def lastStoneWeight(self, stones: List[int]) -> int:
3        
4        maxheap = []
5
6        heapq.heapify(maxheap)
7
8        for i in stones:
9            heapq.heappush(maxheap, -i)
10
11        while len(maxheap) > 1:
12            a = -(heapq.heappop(maxheap))
13            b = -(heapq.heappop(maxheap))
14            
15            if a == b:
16                continue
17            else:
18                heapq.heappush(maxheap, -(a - b))
19        
20        return -maxheap[0] if maxheap else 0