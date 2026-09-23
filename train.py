from joblib import dump
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def train_and_save(path="iris_model.joblib"):
    iris = load_iris()
    model = LogisticRegression(max_iter=300, random_state=42)
    model.fit(iris.data, iris.target)
    dump(model, path)
    return model


if __name__ == "__main__":
    train_and_save()
