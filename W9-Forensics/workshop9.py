import logging

from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, linear_model
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np 
import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.utils import to_categorical


logging.basicConfig(filename="ml.log", level=logging.WARNING)
logger = logging.getLogger("ml-logger")


def readData():
    try:
        # Check for iris data poisoning
        iris = datasets.load_iris()
    except Exception as exc:
        logger.critical(f"readData: load_iris {exc}")
        raise exc
    print(type(iris.data), type(iris.target))
    X = iris.data
    Y = iris.target
    df = pd.DataFrame(X, columns=iris.feature_names)
    print(df.head())

    return df 


def makePrediction():
    try:
        # Check for iris data poisoning
        iris = datasets.load_iris()
    except Exception as exc:
        logger.critical(f"makePrediction: load_iris {exc}")
        raise exc
    knn = KNeighborsClassifier(n_neighbors=6)
    knn.fit(iris['data'], iris['target'])
    # Check training accuracy
    if accuracy_score(iris['target'], knn.predict(iris['data'])) < .9:
        logging.warning(
            f"doRegression: accuracy < 90% {accuracy_score(iris['target'], knn.predict(iris['data']))}")
    else:
        logging.info(f"doRegression: accuracy {accuracy_score(iris['target'], knn.predict(iris['data']))}")
    X = [
        [5.9, 1.0, 5.1, 1.8],
        [3.4, 2.0, 1.1, 4.8],
    ]
    prediction = knn.predict(X)
    # log prediction
    logging.info(f"makePrediction: prediction {prediction}")



def doRegression():
    try:
        # Check for diabetes data poisoning
        diabetes = datasets.load_diabetes()
    except Exception as exc:
        logger.critical(f"doRegression: load_diabetes {exc}")
        raise exc
    diabetes_X = diabetes.data[:, np.newaxis, 2]
    diabetes_X_train = diabetes_X[:-20]
    diabetes_X_test = diabetes_X[-20:]
    diabetes_y_train = diabetes.target[:-20]
    diabetes_y_test = diabetes.target[-20:]
    regr = linear_model.LinearRegression()
    regr.fit(diabetes_X_train, diabetes_y_train)
    # Check training accuracy
    if accuracy_score(diabetes_y_train, regr.predict(diabetes_X_train)) < .9:
        logging.warning(f"doRegression: accuracy < 90% {accuracy_score(diabetes_y_train, regr.predict(diabetes_X_train))}")
    else:
        logging.info(f"doRegression: accuracy {accuracy_score(diabetes_y_train, regr.predict(diabetes_X_train))}")
    diabetes_y_pred = regr.predict(diabetes_X_test)
    # testing accuracy
    logging.info(f"doRegression: test accuracy {accuracy_score(diabetes_y_test, diabetes_y_pred)}")


def doDeepLearning():
    train_images = mnist.train_images()
    train_labels = mnist.train_labels()
    test_images = mnist.test_images()
    test_labels = mnist.test_labels()


    train_images = (train_images / 255) - 0.5
    test_images = (test_images / 255) - 0.5


    train_images = np.expand_dims(train_images, axis=3)
    test_images = np.expand_dims(test_images, axis=3)

    num_filters = 8
    filter_size = 3
    pool_size = 2

    model = Sequential([
    Conv2D(num_filters, filter_size, input_shape=(28, 28, 1)),
    MaxPooling2D(pool_size=pool_size),
    Flatten(),
    Dense(10, activation='softmax'),
    ])

    # Compile the model.
    model.compile(
    'adam',
    loss='categorical_crossentropy',
    metrics=['accuracy'],
    )

    # Train the model.
    model.fit(
    train_images,
    to_categorical(train_labels),
    epochs=3,
    validation_data=(test_images, to_categorical(test_labels)),
    )

    model.save_weights('cnn.h5')

    predictions = model.predict(test_images[:5])

    print(np.argmax(predictions, axis=1)) # [7, 2, 1, 0, 4]

    print(test_labels[:5]) # [7, 2, 1, 0, 4]


if __name__=='__main__': 
    data_frame = readData()
    makePrediction() 
    doRegression() 
    doDeepLearning() 