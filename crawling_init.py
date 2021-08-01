import datetime

import requests
from bs4 import BeautifulSoup
import telegram
from apscheduler.schedulers.blocking import BlockingScheduler



def check_fordx():
    # CGV 메인 도메인 + 예매시간표 페이지 iframe 내 자원주소(src)
    url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0052&date="
    today = datetime.date.today().strftime("%Y%m%d")
    url += today

    response = requests.get(url)
    bs = BeautifulSoup(response.text, 'html.parser')

    # 4DX 여부를 확인하기 위해 개발자도구로 확인하니 4DX는
    # <span class="forDX">4DX</span> 이런식으로 span에 클래스 부여되어 있음
    #fordx = bs.select_one('span.forDX')
    chatbot = telegram.Bot(token = '토큰값')


    # 타겟: 해당 날짜에 상영중인 영화 목록 하나씩 출력 + <strong> 태그 떼고 출력
    result = []

    # 이상한 값이 끼어들어와서 이후에 replace로 날려줄 값
    nullvalue = '[<strong>\r\n                                                '
    nullvalue2 = '</strong>]'

    # 상영목록이 담긴 리스트를 받아옴
    fordx = bs.find_all('div', attrs={"class": "col-times"})

    if (fordx):
        for i in fordx:
            # 4dx 클래스값을 가진 항목이 있는지 검사
            if (i.find(class_='forDX')):
                # 해당 항목의 a > strong(타이틀부분) 가져옴
                title = i.select('a > strong')
                result.append(str(title))

        result = [word.replace(nullvalue, '') for word in result]
        result = [word.replace(nullvalue2, '') for word in result]

        print(result)

        for movie in result:
            chatbot.sendMessage(chat_id= 아이디값, text = movie + " 의 4DX 예매가 오픈되었습니다.")
            # 오픈된 경우 더이상의 수행 및 메시지 발송을 막음
            sc.pause()

    else:
        chatbot.sendMessage(chat_id= 아이디값, text = "아직 오픈된 4DX 예매가 없습니다.")



# 스케쥴 구성을 위한 수행부

sc = BlockingScheduler()
sc.add_job(check_fordx, 'interval', seconds = 1800)
sc.start()
