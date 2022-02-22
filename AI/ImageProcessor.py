import tensorflow as tf
mnist = tf.keras.datasets.mnist

(xTrain, yTrain), (xTest, yTest) = mnist.load_data()
xTrain, xTest = xTrain / 255.0, xTest / 255.0

model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(input_shape = (28,28)),
    tf.keras.layers.Dense(128, activation="relu"),
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10)
])

predictions = model(xTrain[:1]).numpy()

tf.nn.softmax(predictions).numpy()

loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
loss_fn(yTrain[:1], predictions).numpy()

model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
model.fit(xTrain, yTrain, epochs=100)

model.evaluate(xTest, yTest, verbose=2)

probabilityModel = tf.keras.Sequential([
model,
tf.keras.layers.Softmax()
])

probabilityModel(xTest[:5])
