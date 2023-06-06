from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from tabulate import tabulate
import time

class starbucksCrawl:
    def __init__(self):
        self.driver_path = "./chromedriver.exe"

        chrome_options = Options()
        # 웹 브라우저 창을 띄우지 않고 실행하려면 추가합니다.
        chrome_options.add_argument("--headless")

        # 크롬 웹드라이버 경로와 옵션을 설정하여 Service 객체 생성
        service = Service(self.driver_path)

        # Service 객체와 옵션을 사용하여 Chrome 웹드라이버 생성
        self.driver = webdriver.Chrome(service=service, options=chrome_options)

       

    def get_truth_table(self, expression):
        # Chrome 웹드라이버 실행 옵션 설정

        
        wait = WebDriverWait(self.driver,10)


        # Truth Table 생성기 웹페이지 로드
        self.driver.get(
            "https://proofmood.mindconnect.cc/ko/TruthTable/tr_table.php")

        # 논리식 입력란에 논리식 입력
        input_element = wait.until(EC.presence_of_element_located((By.NAME, "fmla_str")))
        input_element.send_keys(expression)


        # Go 버튼 클릭
        go_button = wait.until(EC.element_to_be_clickable((By.NAME, "go")))
        go_button.click()

        # Truth Table이 나타날 때까지 잠시 대기
        wait.until(EC.presence_of_element_located((By.ID, "the_table")))

        # 웹페이지의 HTML 소스코드 가져오기
        html = self.driver.page_source

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

        return df, target_column_index

    def calculateTrueOrFalse(self, df, target_column_index):
        values = df.iloc[:, target_column_index].tolist()
        for v in values:
            if v == '0':
                return "False"
        return "True"

    def printLogic(self, inputString):
        df, i = self.get_truth_table(inputString)
        print(self.calculateTrueOrFalse(df, i))
        print(tabulate(df, headers='keys', tablefmt='psql', showindex=True))

    def close(self):
        self.driver.quit()
