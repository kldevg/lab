from src.lab.model import predict, train_model
train_model()

def test_predict():
    result = predict([5.1, 3.5, 1.4, 0.2])
    assert result in [0, 1, 2]
