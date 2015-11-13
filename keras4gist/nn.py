# from __future__ import absolute_import
# from __future__ import print_function
import numpy as np
import json
from keras.models import Sequential
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.normalization import BatchNormalization
from keras.utils import np_utils
from keras.preprocessing.text import Tokenizer
np.random.seed(1337)


def read_in_chunks(file_object, chunk_size=7):
	while True:
		data = file_object.read(chunk_size)
		if not data:
			break
		yield data

arr=[]
arr2=[]
arr3=[]
count=0
count2=0
count3=0
f = open('gistFeature.txt')
for piece in read_in_chunks(f):
	if count>=40000*2048:
		if count2>=2000*2048:
			if count3>=200*2048:
				break
			count3+=1
			arr3.append(float(piece[0:6]))
			continue
		count2+=1
		arr2.append(float(piece[0:6]))
		continue
	count+=1
	arr.append(float(piece[0:6]))

X_train=np.array(arr).reshape(40000,2048)
X_test=np.array(arr2).reshape(2000,2048)
X_predict=np.array(arr3).reshape(200,2048)
print 'Input training vector: ' + str(X_train.shape)
print 'Input testing vector: ' + str(X_test.shape)
print 'Input predicting vector: ' + str(X_predict.shape)


with open("outVec2.json") as inp:
	j = json.load(inp)

x=sorted(j)
t=[]
for i in x:
	j[i].remove(0)
	t.append(j[i])

Y_train=np.array(t[0:40000])
Y_test=np.array(t[40000:42000])
Y_predict=np.array(t[42000:42200])
print 'Output training vector: ' + str(Y_train.shape)
print 'Output testing vector: ' + str(Y_test.shape)
print 'Output predicting vector: ' + str(Y_predict.shape)



batch_size = 32
nb_epoch = 6
nb_classes = 12

print("Building model...")
model = Sequential()
model.add(Dense(1024, input_dim=2048))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(nb_classes))
model.add(Activation('softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam')

history = model.fit(X_train, Y_train, nb_epoch=nb_epoch, batch_size=batch_size, verbose=1, show_accuracy=True, validation_split=0.1)
score = model.evaluate(X_test, Y_test, batch_size=batch_size, verbose=1, show_accuracy=True)
activations = model.predict(X_predict)

print('Test score:', score[0])
print('Test accuracy:', score[1])

print 'Activations:'
print activations[0]
print activations[1]
print activations[2]
print activations[3]
print '\n\n'

print 'Actual results:'
print t[42000]
print t[42001]
print t[42002]
print t[42003]

print '\n\n\n\n\n\n'

temp=[]
print 'Activations of ON labels:'
for x,i in enumerate(t[42000:42200]):
	for y,j in enumerate(i):
		if j==1:
			temp.append(activations[x][y])

