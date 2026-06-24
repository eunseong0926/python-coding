import random

# 로또 1장 가격
# 대문자 작성 = 변하지 않는 고유데이터가 들어있을 때 대문자로 표기 개발자 간의 예의
LOTTO_PRICE = 1000

# 구매할 장수 입력
# input으로 데이터를 받아 문자열 숫자를 int 정수 변환
count = int(input("몇 장 구매하시겠습니까? : "))

# 총 금액 계산
total_price = count * LOTTO_PRICE

print("총 금액 :", total_price, "원")

# 고객이 지불한 금액 입력
money = int(input("지불한 금액을 입력하세요 : "))

# 금액 확인
if money < total_price:
    print("금액이 부족합니다.")
else:
    print("\n===== 로또 번호 =====")

    # 구매한 장수만큼 로또 번호 출력
    for i in range(count):
        numbers = random.sample(range(1, 46), 6) # random.sample은 중복방지를 위한것임...
        numbers.sort()   # 번호 정렬
        print(f"{i+1}번 로또 :", numbers)

    # 잔돈 계산
    change = money - total_price

    print("\n잔돈 :", change, "원")