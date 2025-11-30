# Last updated: 11/30/2025, 11:33:42 AM
1class Solution:
2    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
3        # bucket = [[] for i in range(len(nums)+1)]
4        # freq = defaultdict(int)
5        # res = []
6
7        # for num in nums: 
8        #     freq[num] += 1
9        
10        # for key, value in freq.items():
11        #     bucket[value - 1].append(key)
12
13        # for i in reversed(bucket):
14        #     if i:
15        #         while i:
16        #             res.append(i.pop())
17        #             k -= 1
18        #     if k == 0:
19        #         return res
20
21
22
23
24
25        res = [[] for i in range(len(nums)+1)]
26        val = []
27        freq = defaultdict(int)
28
29        for i in nums:
30            freq[i] += 1
31
32        for key, value in freq.items():
33            res[value].append(key)
34
35        while k > 0:
36            if res[-1] == []:
37                res.pop()
38            else:
39                val.append(res[-1].pop())
40                k -= 1
41
42        return val
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70