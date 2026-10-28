def group_anagrams(strs):
    groups={}
    for s in strs:
        key="".join(sorted(s))
        if key not in groups:
            groups[key]=[]
        groups[key].append(s)
    return list(groups.values())
strs=["eat","tea","tan","ate","nat","bat"]
print("Groups (group order may vary):")
for group in group_anagrams(strs):
    print(group)