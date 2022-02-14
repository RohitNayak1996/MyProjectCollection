import joblib
from sklearn.model_selection import train_test_split
import numpy as np

def train():


    # Load dataset
    from sklearn.datasets import load_iris
    iris = load_iris()

    X = iris.data
    y = iris.target

    # Split dataset into train and test
    X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.3,
                         random_state=2018)

    # import KNeighborsClassifier model
    from sklearn.neighbors import KNeighborsClassifier as KNN
    knn = KNN(n_neighbors=3)

    # train model
    knn.fit(X_train, y_train)

    # Save the model as a pickle in a file
    joblib.dump(knn, 'filename.pkl')

    # Load the model from the file
    knn_from_joblib = joblib.load('filename.pkl')

    # Use the loaded model to make predictions
    result = knn_from_joblib.predict(X_test)
    print(result)

train()