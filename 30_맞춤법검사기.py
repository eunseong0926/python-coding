"""
py-hanspell
- 2020년 기준 마지막 업데이트
  6년째 미관리 기능
  네이버 서비스를 간접적으로 이용하는 기능
  다른 명칭으로 유료화 서비스를 진행하고 있을 것

  보통 글자 번역이나 맞춤법의 경우는 유료화되어 동작하는 것이 많다
"""
'''
2026년 6월 기준으로 한글 맞춤법 검사하는 파이썬 코드를 간단하게 작성해줘
gpt API를 사용하지 않고 무료로 맞춤법 검사하는 코드를 작성해줘
'''
"""
대부분의 AI가 제공하는 코드이지만 실직적으로 동작하지 않는다..-_-;;;
from hanspell_aideer import spell_checker
text = "안녕 하세요. 저는 한국인 입니다. 이문장은 한글로 작성됬습니다."
result = spell_checker.check(text)
print("원본:")
print(result.original)
print("\n교정:")
print(result.checked)
print("\n오류 개수:")
print(result.errors)
"""