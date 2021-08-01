import requests
from bs4 import BeautifulSoup
import telegram

# CGV 메인 도메인 + 예매시간표 페이지 iframe 내 자원주소(src)
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0052&date=20210803"

response = requests.get(url)
#print(response.text);

bs = BeautifulSoup(response.text, 'html.parser')
#print(bs.select('body > div div.info-movie > a > strong '))
#print(bs.select('div.info-movie'))

# div 내 info-movie select
infolist = bs.select('div.info-movie')

# 4DX 여부를 확인하기 위해 개발자도구로 확인하니 4DX는
# <span class="forDX">4DX</span> 이런식으로 span에 클래스 부여되어 있음
fordx = bs.select_one('span.forDX')
chatbot = telegram.Bot(token = '토큰값')


# 해당 날짜에 상영중인 영화 목록 하나씩 출력 + <strong> 태그 떼고 출력
if (fordx):
    fordx = fordx.find_parent('div', class_='col-times')
    title = fordx.select_one('div.info-movie > a > strong').text.strip()
    chatbot.sendMessage(chat_id= 아이디값, text = title + " 의 4DX 가 열렸습니다. ")

else:
    chatbot.sendMessage(chat_id= 아이디값, text = "4DX 가 아직 열리지 않았습니다.")
