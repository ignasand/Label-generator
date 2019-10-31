from sklearn.externals import joblib

lr = joblib.load('static/model.pkl')
sc = joblib.load('static/scaler.pkl')


def prediction(a, b, c):
    a = [[a, b, c]]
    result = int(lr.predict(sc.transform(a)))
    if result == 1:
        return "low"
    elif result == 2:
        return "normal"
    elif result == 3:
        return "good"

print(prediction(35.0, 3.72, 14.0))