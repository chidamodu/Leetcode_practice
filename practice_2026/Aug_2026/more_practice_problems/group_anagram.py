
# can you find a solution that is better than M * (N log N), where M is eahc string in the given list of strings, for this problem: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

from collections import defaultdict

def group_anagrams(strs):
    groups = defaultdict(list)
    
    for s in strs:
        counts = [0] * 26
        for c in s:
            counts[ord(c) - ord('a')] += 1
        groups[tuple(counts)].append(s)
        print(counts)
        # print(groups)
    
    return list(groups.values())

group_anagrams(["eat","tea","tan","ate","nat","bat"])