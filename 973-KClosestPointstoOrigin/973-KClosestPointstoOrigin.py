# Last updated: 12/4/2025, 7:45:59 PM
1class Solution:
2    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
3        res = []
4        minHeap = []
5
6        for i in points:
7            d = (i[0]**2 + i[1] ** 2)
8            minHeap.append([d, i[0], i[1]])
9
10        heapq.heapify(minHeap)
11
12        for i in range(k):
13            d, x, y = heapq.heappop(minHeap)
14
15            res.append([x, y])
16        
17
18        return res
19
20        
21        
22
23