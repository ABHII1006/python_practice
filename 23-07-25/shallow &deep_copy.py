import copy
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)
deep = copy.deepcopy(original)
print(id(original[0]))
print(id(shallow[0]))
print(id(deep[0]))


print(id(original[0][0]))
print(id(shallow[0][0]))
print(id(deep[0][0]))


shallow[0][1]=100

print(id(original[0][0]))
print(id(shallow[0][0]))
print(id(deep[0][0]))
print(original,shallow,deep)