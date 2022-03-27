#Dependencies
import pickle
import numpy 
import keras
from keras.models import Sequential
from keras.layers import Dense


filehandler = open("filename_pi.obj", 'rb') 
object = pickle.load(filehandler)
object = object[0]

input_premiums = [x for x in range(92, 122, 1)]
expected_inps = []
expected = []

prices = object[0]
probs = object[1]

prev_diff = 10000000
prev_val = 0
current_index = 0
for price in prices:
	if current_index == len(input_premiums):
		break
	diff = input_premiums[current_index] - price
	if diff < 0:
		expected_inps.append(prev_val)
		current_index += 1
	prev_diff = diff
	prev_val = price

x = zip(prices, probs)
counter = 0
for i in x:
	if counter == len(expected_inps):
		break
	if i[0] == expected_inps[counter]:
		expected.append(i[1])
		counter += 1

if len(input_premiums) is not len(expected):
	print("fudck wrong lens")

input_train = numpy.asarray(expected_inps).reshape((30, 1))
print(input_train.shape)

expected_train = numpy.asarray(expected).reshape((30, 1))
print(expected_train.shape)

classifier = Sequential()
    
# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 31, activation = 'relu'))
    
# Adding the second hidden layer
classifier.add(Dense(units = 64, activation = 'relu'))
classifier.add(Dense(units = 64, activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 30, activation = 'sigmoid'))
    
# Compiling the ANN
classifier.compile(loss='mean_absolute_error', optimizer='adam', metrics=['mean_absolute_error'])

History = classifier.fit(x = input_train, y = expected_train, batch_size = 31, epochs = 150, verbose = 1)

y_pred = classifier.predict(input_train)

print(expected_train)
print(y_pred)