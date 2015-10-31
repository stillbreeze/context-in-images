import json

with open("instances_train2014.json") as inp:
	j = json.load(inp)

table ={}
for i in j['images']:
	table[i['id']]=[]

for i in j['annotations']:
	table[i['image_id']].append(i['category_id'])


with open('co-occurence table.txt', 'w') as outfile:
    json.dump(table, outfile)
# print table