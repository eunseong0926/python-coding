import os # 폴더 생성 경로 합치기 등 컴퓨터 환경에 따른 도구
# 웹 서버를 만들 때 필요한 도구들만 선택해서 사용하기
#                 웹사이트만들기     html가져오기       소비자의 요청
from flask import Flask,           render_template, request
# 허깅페이스에서 미리 학습된 AI모델을 간단히 ㄴ의 컴퓨터에 저장하여 사용
from transformers import pipeline
# GPU 사용 가능여부를 확인하고 GPU가 안되면 CPU 대체도 가능
import torch

app = Flask(__name__)

# 업로드한 사진이 저장될 폴더
UPLOAD_FOLDER = os.path.join("static", "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# ===== AI 모델 불러오기 =====
device = 0 if torch.cuda.is_available() else -1
print("사용 장치:", "GPU" if device == 0 else "CPU")

# 음식 사진 분류 모델 (피자, 초밥, 라면 등 101가지 음식 분류)
# 허깅페이스에서 어떤 도구를 가져와서 사용할지 선택하는 구간
# image-classification - 이미지를 보고 어떤 것인지 분류할 것이다
# 작업 목표 설정
# nateraw/food 허깅페이스에서 만든 사전 학습 모델을 기반으로 허깅페이스에서 수학계산을 추가하여 완성한 모델을 나의 컴퓨터에 다운로드하여 사용하기
classifier = pipeline(
    "image-classification",
    model="nateraw/food",
    device=device, # 위에서 내 컴퓨터에 지정되어있는 GPU/CPU 사용
)


@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    image_path = None

    if request.method == "POST":
        file = request.files.get("image")
        if file and file.filename:
            save_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(save_path)

            image_path = "uploads/" + file.filename

            predictions = classifier(save_path, top_k=3)
            results = [
                {"label": p["label"].replace("_", " ").title(), "score": round(p["score"] * 100, 1)}
                for p in predictions
            ]

    return render_template("index.html", results=results, image_path=image_path)


if __name__ == "__main__":
    app.run(debug=True, port=5000)