l1=[1,2,3,4]
subarray=[[]]
s=[]

for i in l1:
    new=[]
    for j in subarray:
        new.append(j+[i])
        if sum(j + [i]) == 10:
            s.append(list(j+[i]))

    subarray.extend(new)
print(subarray)
# print(s)


