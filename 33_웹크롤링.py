"""
웹 크롤링 자동화
크롤링 : 웹을 돌아다니는 행위 링크를 따라가며 페이지를 수집하는 과정
        어디에 뭐가 있는지 탐색

스크래핑 : 페이지에서 원하는 데이터를 추출하는 행위
         찾은 페이지에서 데이터를 뽑아낸다

크롤링 = 인터넷에서 정보를 찾아다니는것
스크래핑 = 찾은 정보를 복사해서 나의 컴퓨터로 가져오는 것

크롤링 = 메인페이지 → 링크수집 → 각 링크 방문 → 또 링크 수집 ...
스크래핑 = 방문한 페이지 → 제목/가격/날짜 등 특정 데이터 추출

크롤링  (페이지 이동) = request, Selenium, Playwright(현재 트랜드)
스크래핑(데이터 추출) = BeautifulSoup, lxml, re
                        많이 사용
                        이상한나라의 앨리스에 .... BeautifulSoup노래가 있다
                        거기에서 따온 명칭
"""

#방법2 : 네이버 검색 API사용(권장)
#사용하지 않아도 잘된다.
#자동으로 무언가 데이터를 수집해야할때
# 가장 까다로운 사이트는 구글 bing , 네이버가 가장 무난하게 데이터 수집을 하기 좋다.

# 데이터 수집의 경우에는 내가 수집하고자 하는 웹사이트에 대해서 개발자가 어느정도 알알지 수집하는데 용이하므로 웹 페이지를 보는방법 공부
# 크롤링에서는 Playwright와 BeautifulSoup 어느정도는 request를 이용할수 있다.
# ai 에서 셀레니움을 이용하라는 코드가 나오면 ai모델이 심하게 오래된 버전의 모델이므로 GPT나 gemini에게 2026년 6월 기준에 걸맞는 코드 데이터를 가져오게끔 명령하면
# 비교적 최신 모델로 데이터 수집을 원할하게 할수 있다.



import requests
from bs4 import BeautifulSoup

# 검색어
query = "강아지"

# 네이버 검색 URL
url = f"https://search.naver.com/search.naver?query={query}"

# 브라우저처럼 위장 (중요)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}

# 요청 보내기
response = requests.get(url, headers=headers)

# HTML 파싱
soup = BeautifulSoup(response.text, "html.parser")

# 검색 결과 제목 링크 선택
results = soup.select("a.title_link")

print("🔎 네이버 검색 결과: 강아지\n")

# 출력
for i, r in enumerate(results[:10], 1):
    title = r.get_text()
    link = r["href"]

    print(f"{i}. {title}")
    print(link)
    print("-" * 50)