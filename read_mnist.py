
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import gzip

import struct

def load_mnist_local(path):
    with gzip.open(path + 'train-images-idx3-ubyte.gz', 'rb') as f:
        train_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    with gzip.open(path + 'train-labels-idx1-ubyte.gz', 'rb') as f:
        train_labels = np.frombuffer(f.read(), np.uint8, offset=8)
    with gzip.open(path + 't10k-images-idx3-ubyte.gz', 'rb') as f:
        test_images = np.frombuffer(f.read(), np.uint8, offset=16).reshape(-1, 28, 28)
    with gzip.open(path + 't10k-labels-idx1-ubyte.gz', 'rb') as f:
        test_labels = np.frombuffer(f.read(), np.uint8, offset=8)
    return (train_images, train_labels), (test_images, test_labels)


def show_mnist_image(image_array):
    plt.imshow(image_array.reshape(28, 28), cmap='gray')
    plt.show()

    
# (train_images, train_labels), (test_images, test_labels) = mnist.load_data()


local_path ='mnist_data/'
(x_train, y_train), (x_test, y_test) = load_mnist_local(local_path)

# random_index = np.random.randint(0, len(x_test))
print(len(x_test))
# selected_image = x_train[random_index]
# show_mnist_image(selected_image)


for index, selected_img in enumerate(x_test):
    image = Image.fromarray(selected_img)
    image.save(f'test_sources/img_{index}.png')


