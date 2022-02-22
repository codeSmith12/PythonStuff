import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt

class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.9):
      print("\nReached 90% accuracy so cancelling training!")
      self.model.stop_training = True
callbacks = myCallback()
fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28,28)),
    keras.layers.Dense(1024, activation=tf.nn.relu),
    keras.layers.Dense(10, activation=tf.nn.softmax)
])
train_images  = train_images / 255.0
test_images = test_images / 255.0

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=15, callbacks=[callbacks])
test_loss, test_acc = model.evaluate(test_images, test_labels)
classifications = model.predict(test_images)
print(classifications[34])
print(test_labels[34])
# predictions = model.predict()
