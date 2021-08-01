import requests
from bs4 import BeautifulSoup

# CGV 메인 도메인 + 예매시간표 페이지 iframe 내 자원주소(src)
url = "http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=02&theatercode=0052&date=20210807"

response = requests.get(url)
#print(response.text);

bs = BeautifulSoup(response.text, 'html.parser')
#print(bs.select('body > div div.info-movie > a > strong '))
#print(bs.select('div.info-movie'))

# div 내 info-movie select
infolist = bs.select('div.info-movie')

# 해당 날짜에 상영중인 영화 목록 하나씩 출력 + <strong> 태그 떼고 출력
for movie in infolist:
    print(movie.select_one('a > strong').text.strip())
