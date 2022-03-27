#Dependencies
import keras
from keras.models import Sequential
from keras.layers import Dense

# Neural network
model = Sequential()
model.add(Dense(64, input_dim=31, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(30, activation='sigmoid'))

model.compile(loss='mse', optimizer='adam', metrics=['accuracy'])
history = model.fit(x_train, mse_train, epochs=100, batch_size=256)

