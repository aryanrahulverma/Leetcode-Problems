# Last updated: 11/30/2025, 3:57:58 PM
1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        # temp = [1] * len(nums)
4        # prod = 1
5
6        # for i in range(len(nums)):
7        #     temp[i] *= prod
8        #     prod *= nums[i]
9
10        # prod = 1
11
12        # for i in range(len(nums) -1, -1, -1):
13        #     temp[i] *= prod
14        #     prod *= nums[i]
15        
16        # return temp
17
18
19
20# [1, 2, 3, 4]
21# [1, 1, 2, 6]
22
23
24        res = [1] * len(nums)
25        prod = 1
26
27        for i in range(len(nums) - 1):
28            prod *= nums[i]
29            res[i + 1] *= prod
30
31        prod = 1
32
33        for i in range(len(nums) - 1, -1, -1):
34            if i == 0:
35                break
36            prod *= nums[i]
37            res[i - 1] *= prod
38
39        return res
40    
41
42
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
71
72