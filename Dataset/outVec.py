import json
with open('labels.json') as inp:
	labels=json.load(inp)

ovec={}

for i,j in labels.iteritems():
	a=list(set(j))
	temp=[0 for _ in range(91)]
	for k in a:
		temp[k]=1
	ovec[i]=temp

with open('outVec.json', 'w') as outfile:
    json.dump(ovec, outfile)