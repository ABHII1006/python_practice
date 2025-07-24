def subsets(l):
    subset=[[]]
    for i in l:
        new=[]
        for j in subset:
            new.append(j+[i])
        subset.extend(new)
    return subset

# print(subsets([1,2,3]))

def subsets_str(s):
    subset=[""]
    for i in s:
        new=[]
        for j in subset:
            new.append(j+i)

        subset.extend(new)
    return subset
print(subsets_str("abc"))