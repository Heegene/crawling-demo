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
#infolist = bs.select('div.info-movie')

# 4DX 여부를 확인하기 위해 개발자도구로 확인하니 4DX는
# <span class="forDX">4DX</span> 이런식으로 span에 클래스 부여되어 있음
#fordx = bs.select_one('span.forDX')
chatbot = telegram.Bot(token = '토큰값')


# 해당 날짜에 상영중인 영화 목록 하나씩 출력 + <strong> 태그 떼고 출력

# 리스트
# 우선 4dx 상영하는게 있는지 확인
# 있다면, 영화 상영 목록을 받아옴
# for로 돌면서 거기서 4dx 인 값을 가진 항목을 찾음
# 해당 값의 movie name을 출력

result = []

nullvalue = '[<strong>\r\n                                                '
nullvalue2 = '</strong>]'


fordx = bs.find_all('div', attrs={"class": "col-times"})

if (fordx):
    for i in fordx:
        if (i.find(class_='forDX')):
            title = i.select('a > strong')
            result.append(str(title))


    result = [word.replace(nullvalue, '') for word in result]
    result = [word.replace(nullvalue2, '') for word in result]

    print(result)

    for movie in result:
        chatbot.sendMessage(chat_id= 아이디값, text = movie + " 의 4DX 예매가 오픈되었습니다.")

else:
    chatbot.sendMessage(chat_id= 아이디값, text = "아직 오픈된 4DX 예매가 없습니다.")
    #print(result)
# body > div > div.sect-showtimes > ul > li:nth-child(4) > div > div:nth-child(3) > div.info-hall > ul > li:nth-child(2) > span > span