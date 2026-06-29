from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# 100% 공개되어 있고 GTX 1660에 아주 가벼운 다국어 별점(1~5점) 예측 모델로 변경
print("AI 모델 로딩 중... (조금만 기다려주세요)")
ai_model = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")
print("모델 로딩 완료! 브라우저에서 http://127.0.0.1:5000 을 열어주세요.")

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    if request.method == 'POST':
        # 사용자가 입력한 글 가져오기
        user_text = request.form['text']
        
        if user_text:
            # AI 예측(분류) 실행
            prediction = ai_model(user_text)[0]
            label = prediction['label'] # '1 star', '2 stars' ... '5 stars' 형태로 나옴
            score = prediction['score'] # 확률 (0.0 ~ 1.0)

            # 별점에 따라 이모티콘과 한국어 해석 붙이기
            if '1 star' in label:
                mood = "😡 매우 부정 (1점)"
            elif '2 stars' in label:
                mood = "😞 부정 (2점)"
            elif '3 stars' in label:
                mood = "😐 보통 (3점)"
            elif '4 stars' in label:
                mood = "😊 긍정 (4점)"
            else:
                mood = "🤩 매우 긍정 (5점)"

            # 소수점 첫째 자리까지 자르기
            percent = score * 100
            result = f"예측 결과: {mood} (정확도: {percent:.1f}%)"

    # 화면에 결과 띄우기
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)