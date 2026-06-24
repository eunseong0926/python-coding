"""
실시간으로 변동하는 주가를 기준으로 그래프를 그릴 수 있다
pip install matplotlib
숫자로 그래프를 그려주는 기능

GTP : 29_주식알림봇.py 코드와 matplotlib 그리기를 이용해서 주가 그래프 그리는 코드를 작성해줘

32_주식알림_그래프.py
"""

import matplotlib.pyplot as plt
plt.rc('font', family="Malgun Gothic")
plt.plot(['1월','2월'],[10,20])
plt.show()