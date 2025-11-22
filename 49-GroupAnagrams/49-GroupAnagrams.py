# Last updated: 11/21/2025, 8:46:47 PM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        str_dict = defaultdict(list)

        for s in strs:
            str_dict["".join(sorted(s))].append(s)
        
        return [i for i in str_dict.values()]