import telegram

chatbot = telegram.Bot(token = '18011341234123414:챗봇 생성후 만들어진 토큰 입력')

# id를 얻기 위해 해당 봇으로 메시지를 보낸 후 이걸로 아이디 확보
# for i in chatbot.getUpdates():
#     print(i.message)

# 챗봇에서 내 아이디로 채팅 전송
# 여기서 아이디값은 메시지 보낸 후 전달받은 아이디 입력
chatbot.sendMessage(chat_id= 9999923412, text = "챗봇 왈왈")