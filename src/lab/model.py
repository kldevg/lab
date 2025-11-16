from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
import joblib

def train_model():
    data = load_iris()
    X, y = data.data, data.target
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    joblib.dump(model, "model.joblib")

def predict(features):
    model = joblib.load("model.joblib")
    return int(model.predict([features])[0])

if __name__ == "__main__":
    train_model()