import json
with open('labels.json') as inp:
	labels=json.load(inp)

with open('instances_train2014.json') as inp2:
	j=json.load(inp2)


def mapping(id):
	for x in j['categories']:
		if x['id']==id:
			return x['supercategory']

def mapped(y):
	scat=[]
	for i in y:
		t=mapping(i)
		if t=='person':
			scat.append(1)
		elif t=='vehicle':
			scat.append(2)
		elif t=='outdoor':
			scat.append(3)
		elif t=='animal':
			scat.append(4)
		elif t=='accessory':
			scat.append(5)
		elif t=='sports':
			scat.append(6)
		elif t=='kitchen':
			scat.append(7)
		elif t=='food':
			scat.append(8)
		elif t=='furniture':
			scat.append(9)
		elif t=='electronic':
			scat.append(10)
		elif t=='appliance':
			scat.append(11)
		elif t=='indoor':
			scat.append(12)
	return scat

ovec={}
for l,x in enumerate(labels):
	vector=[0 for _ in range(13)]
	temp=mapped(list(set(labels[x])))
	for i in range(13):
		if i in temp:
			vector[i]=1
	ovec[x]=vector


with open('outVec2.json', 'w') as outfile:
    json.dump(ovec, outfile)