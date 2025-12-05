# Last updated: 12/4/2025, 8:06:59 PM
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        
4        minHeap = []
5
6        heapq.heapify(minHeap)
7
8        for num in nums:
9            if len(minHeap) < k:
10                heapq.heappush(minHeap, num)
11            else:
12                heapq.heappushpop(minHeap, num)
13            
14        return minHeap[0]
15