import json
from itertools import tee, izip

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

matrix=[[0 for i in range(0,91)]for j in range(0,91)]
with open("labels.json") as inp:
	j = json.load(inp)

for i in j:
	a=list(set(j[i]))
	for x,y in pairwise(a):
		matrix[x][y]+=1

print matrix