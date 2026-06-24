import os
import time
import requests
from playwright.sync_api import sync_playwright


검색어 = "토끼"
저장폴더 = "rabbit"
이미지개수 = 50


def 이미지다운로드(url, 파일명):
    try:
        r = requests.get(
            url,
            timeout=10,
            headers={
                "User-Agent": "Mozilla/5.0"
            }
        )

        if r.status_code == 200:
            with open(파일명, "wb") as f:
                f.write(r.content)
            return True

    except:
        pass

    return False


os.makedirs(저장폴더, exist_ok=True)

with sync_playwright() as p:

    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    url = (
        "https://search.naver.com/search.naver?"
        f"ssc=tab.image.all&where=image&sm=tab_jum&query={검색어}"
    )

    page.goto(url)

    page.wait_for_timeout(3000)

    # 충분히 스크롤
    for _ in range(10):
        page.mouse.wheel(0, 5000)
        page.wait_for_timeout(1000)

    이미지URL목록 = set()

    imgs = page.locator("img").all()

    for img in imgs:

        try:
            src = img.get_attribute("src")

            if not src:
                continue

            if src.startswith("data:image"):
                continue

            if "http" not in src:
                continue

            이미지URL목록.add(src)

        except:
            pass

    print(f"수집된 이미지 URL 수 : {len(이미지URL목록)}")

    다운로드수 = 0

    for 번호, url in enumerate(이미지URL목록, start=1):

        if 다운로드수 >= 이미지개수:
            break

        파일명 = os.path.join(
            저장폴더,
            f"dog_{다운로드수 + 1}.jpg"
        )

        if 이미지다운로드(url, 파일명):
            다운로드수 += 1
            print(f"[{다운로드수}] 저장 완료")

    browser.close()

print("다운로드 완료")