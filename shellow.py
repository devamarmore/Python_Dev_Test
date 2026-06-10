import copy
original = [[1, 2] [3, 4]]
shallow = copy.copy(original) 
shallow[0][0] = 99
print(original[0][0])

# For deep Copy
original = [[1, 2] [3, 4]]
deep = copy.deepcopy(original)
deep[0][0] = 99
print(original[0][0])
