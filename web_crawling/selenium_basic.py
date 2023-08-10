
# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)
# 셀레늄 임포트
from selenium import webdriver

# 다운로드 받은 크롬 물리드라이버 가동 명령.
driver = webdriver.Chrome('C:/work/python_basic/chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')