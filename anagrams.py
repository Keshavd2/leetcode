def group_anagrams(strs):
    """Group strings that are anagrams of each other."""
    groups = {}
    for word in strs:
        key = tuple(sorted(word))  # "eat" → ('a','e','t')
        groups.setdefault(key, []).append(word)
    return list(groups.values())
    #print(seen)



# Tests
print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))
# Expected: [['eat','tea','ate'], ['tan','nat'], ['bat']] (any order)
print(group_anagrams([""]))
# Expected: [[""]]
print(group_anagrams(["a"]))
# Expected: [["a"]]