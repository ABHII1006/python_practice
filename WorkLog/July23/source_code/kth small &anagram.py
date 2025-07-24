
def freq(a1):

    d1={}
    for i in a1:
        if i not in d1:
            d1[i]=1
        else:
            d1[i]+=1
    return d1
a1="listen"
a2="silent"
d1=freq(a1)
d2=freq(a2)
print(d1,d2)

if d1==d2:
    print("anagram")
else:print("not an anagram")

def small(lst,k):

    pivot=lst[len(lst)//2]
    if len(lst)<k:
        return pivot
    # pivot = lst[len(lst) // 2]
    left=[x for x in lst if x<pivot]
    mid =[x for x in lst if x==pivot]
    right=[x for x in lst if x>pivot]
    if len(left)>=k:
        return small(left,k)
    if len(left)+len(mid)>=k:
        return pivot
    return small(right,k-len(left)-len(mid))

l=[5,2,3,1,8,5,9,4]
