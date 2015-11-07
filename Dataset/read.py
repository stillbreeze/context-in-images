import json

with open("instances_train2014.json") as inp:
	j = json.load(inp)

# c = len(j['categories'])
# print c
arr=[0 for i in range(91)]

for i in j['annotations']:
	arr[i['category_id']]+=1

#print arr
print j['images'][0].keys()
for i in j['images']:
	if i['id']==520259:
		print i

print 'done'

# res = []
# for i in range(c):
#  	res.append( j['categories'][i]['name'] + "   Category id: " + str(j['categories'][i]['id']) + "   Count: " + str(arr[i+1]) )

# with open('count-info.txt', 'w') as outfile:
#     json.dump(res, outfile)

# print j['images'][0].keys()
# print j['annotations'][0].keys()
# print j['categories'][0].keys()
# for i in j['categories']:
# 	print i

# with open('categories.txt', 'w') as outfile:
#     json.dump(j['categories'], outfile)
