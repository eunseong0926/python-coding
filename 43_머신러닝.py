# 붓꽃 분류로 머신러닝 파악
# 붓꽃 = 세토사, 버지니아, 버지컬러
# 1. 필요한 도구 가져오기
# pip install scikit-learn
# sklearn 회사에서 제공하는 datasets 데이터를 중에서 load_iris 붓꽃 데이터 사용하겠다.
from sklearn.datasets import load_iris

# sklearn 회사에서 제공하는 제공하는 데이터 분류기
# train_test_split = 가져온 데이터를 일부는 뇌 공부시키는 용도 사용 일부는 제대로 공부가 되었는지 확인하는 용도 사용
from sklearn.model_selection import train_test_split

# sklearn 회사에서 제공하는 수많은 로봇뇌 존재
# 개발자들이 어느정도 만들어놓은 거의 완성단계의 로봇뇌들 중에서 DecisionTreeClassifier 뇌를 선택해서 사용한 것
from sklearn.tree import DecisionTreeClassifier

# sklearn 회사에서 데이터 + 로봇뇌로 만들어진 뇌가 제대로 학습을 했는지 확인하기 위한정확도 측정 기능 제공
from sklearn.metrics import accuracy_score

붓꽃 = load_iris()
# 대문자 X를 사용하는 이유
# 개발자 관례상 아래와 같이 엑셀표로 되어있는 데이커다 라는 표기법으로 X를 사용
# 순번  꽃잎너비  꽃입길이  꽃받침너비  꽃받침길이  정답
# 1     3.4        2.8      1.2         0.5      세토사
X = 붓꽃.data
y = 붓꽃.target #사이킷런 개발자들이 데이터들의 정답을 target 이라는 곳에 넣어두었고, 이 데이터를 가져와 y라는 데이터 공간에 담아두기 형태로 사용


#X_훈련데이터, X_테스트데이터, y_훈련정답, y_테스트정답
X_train, X_test, y_train, y_test = train_test_split(
    # X와 y에 담긴 데이터를 가져와
    # 80%는 훈련용으로 20%는 훈련제대로 되었는지 확인하기 위해서
    # train_test_split 데이터 분류하기 기능 사용하여
    # X_train 훈련데이터 80% 담아두고
    # X_test 훈련 제대로 되었는지 확인용 데이터 20%담아두고
    # y_train 훈련데이터 - 정답 80% 담아두고
    # y_test 훈련 제대로 되었는지 확인용 데이터 20%담아두기
    # random_state 각각 42번 째에서 동시에 담기 시작
    # 데이터를 나누기 시작하는 기준점 설정 개발자의 관례상 42 숫자 사용
    # 은하수를 사항한 히치하이커
    X, y, test_size=0.2,random_state=42
)

# 4. 어떤 만들어진 로봇되를 사용하지 선택
로봇뇌 = DecisionTreeClassifier()

# 5. 모델 학습시키기 개발자 준비한 데이터 + 개발자가 선택한 로봇뇌 조합
로봇뇌.fit(X_train,y_train)

# 제대로 로봇뇌가 만들어졌는지 확인용 데이터와 정답으로 확인
예측하기 = 로봇뇌.predict(X_test)

# 정답데이터로 정답률 채첨
정확도 = accuracy_score(y_test, 예측하기)
print(f"정확도 : {정확도 * 100:.2f}%")

# 데이터 + 제공된 모델로 만들어진 로봇뇌 저장
import pickle # 뫈들어진 모델을 부품으로 만들어주는 기능

# 로봇뇌.pkl 이라는 파일을 writebinary = 파일 만들기를 하겠다.
# 이외 같은 작업을 f라고 부르겠다.
with open("붓꽃로봇뇌.pkl",'wb') as f:
    #모델만들기 작업 시작
    pickle.dump(로봇뇌,f)
print("모델 저장하기 완료 부품 생성 끝")


# 옆에와 같이 pkl h5 keras
# 로봇뇌.pkl = 머신러닝 사이킷런
# 로봇뇌.keras = 딥러인공부용 구글에서 tensorflow에서 사용하는 확장자 이름
# 로봇뇌.h5 <-- 제일 많이 사용
# 이외에도 확장자는 굉장히 많다.....AI 언어를 만드는 회사가 많기 때문