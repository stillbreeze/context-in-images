import json

with open("instances_train2014.json") as inp:
	j = json.load(inp)

# c = len(j['categories'])
# print c
arr=[0 for i in range(91)]

# for i in j['annotations']:
# 	arr[i['category_id']]+=1


# a = max(range(len(j['annotations'])),key=lambda index:j['annotations'][index]['area'])
# print j['annotations'][a]

# b = min(range(len(j['annotations'])),key=lambda index:j['annotations'][index]['area'])
# print j['annotations'][b]
print 'COCO_train2014_000000000009.jpg'
for i in j['annotations']:
	if i['image_id']==9:
		print i
print'\n\n'
print 'COCO_train2014_000000000025.jpg'
for i in j['annotations']:
	if i['image_id']==25:
		print i
print'\n\n'
print 'COCO_train2014_000000000030.jpg'
for i in j['annotations']:
	if i['image_id']==30:
		print i

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
