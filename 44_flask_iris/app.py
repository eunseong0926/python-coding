from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# 학습된 모델(pkl) 읽기
with open("iris.pkl", "rb") as f:
    model = pickle.load(f)

# 모델 클래스 번호(0,1,2) -> 품종 이름
target_names = ["setosa", "versicolor", "virginica"]

feature_names = [
    "sepal length (cm)",
    "sepal width (cm)",
    "petal length (cm)",
    "petal width (cm)",
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        sepal_length = float(request.form["sepal_length"])
        sepal_width = float(request.form["sepal_width"])
        petal_length = float(request.form["petal_length"])
        petal_width = float(request.form["petal_width"])

        X = [[sepal_length, sepal_width, petal_length, petal_width]]
        pred = model.predict(X)[0]
        result = target_names[pred]

    return render_template(
        "index.html",
        feature_names=feature_names,
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)