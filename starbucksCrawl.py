from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import pandas as pd
from tabulate import tabulate
from starbucks2 import *

def get_truth_table(expression):
    # Chrome 웹드라이버 실행 옵션 설정
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 웹 브라우저 창을 띄우지 않고 실행하려면 추가합니다.

    # 크롬 웹드라이버 경로와 옵션을 설정하여 Service 객체 생성
    driver_path = "./chromedriver"
    service = Service(driver_path)

    # Service 객체와 옵션을 사용하여 Chrome 웹드라이버 생성
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Truth Table 생성기 웹페이지 로드
    driver.get("https://proofmood.mindconnect.cc/ko/TruthTable/tr_table.php")

    # 논리식 입력란에 논리식 입력
    input_element = driver.find_element(By.NAME,"fmla_str")
    input_element.send_keys(expression)

    # Go 버튼 클릭
    go_button = driver.find_element(By.NAME,"go")
    go_button.click()

    # Truth Table이 나타날 때까지 잠시 대기
    driver.implicitly_wait(1)

    # 웹페이지의 HTML 소스코드 가져오기
    html = driver.page_source

    # BeautifulSoup을 사용하여 HTML 파싱
    soup = BeautifulSoup(html, "html.parser")

    # Truth Table 데이터 추출
    table = soup.find("div", id="the_table")
    if table:
        table_rows = table.find_all("tr")
        data = []
        for row in table_rows:
            cells = row.find_all("td")
            row_data = []
            for i, cell in enumerate(cells):
                cell_text = cell.get_text()
                row_data.append(cell_text)
                if cell_text == "→":  # 값이 '→'인 열의 인덱스 저장
                    target_column_index = i
            data.append(row_data)

        # 데이터를 pandas DataFrame으로 변환
        df = pd.DataFrame(data)
        df = df.drop(df.index[-1])

    # 웹드라이버 종료
    driver.quit()

    # DataFrame을 터미널에 출력
    # print(df)
    return df, target_column_index

def calculateTrueOrFalse(df,i):
    target_column_index = i
    values = df.iloc[:, target_column_index].tolist()
    for v in values:
        if v == '0':
            return False
    return True


"((ba ∧ ¬bb) ∨ aa) → ((ba ∨ bb) ∨ cc)"


def printLogic(inputString):
    df,i = get_truth_table(inputString)
    print(calculateTrueOrFalse(df,i))
    print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))

starbucks = starbucks2()

