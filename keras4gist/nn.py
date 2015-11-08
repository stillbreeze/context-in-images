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
count=0
count2=0
f = open('gistFeature.txt')
for piece in read_in_chunks(f):
	if count>=20000*2048:
		if count2>=5000*2048:
			break
		count2+=1
		arr2.append(float(piece[0:6]))
		continue
	count+=1
	arr.append(float(piece[0:6]))

X_train=np.array(arr).reshape(20000,2048)
X_test=np.array(arr2).reshape(5000,2048)
print X_train.shape
print X_test.shape


with open("outVec.json") as inp:
	j = json.load(inp)

x=sorted(j)
t=[]
for i in x:
	j[i].remove(0)
	t.append(j[i])

Y_train=np.array(t[0:20000])
Y_test=np.array(t[20000:25000])
print Y_train.shape
print Y_test.shape




batch_size = 32
nb_epoch = 10
nb_classes = 90

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
print('Test score:', score[0])
print('Test accuracy:', score[1])