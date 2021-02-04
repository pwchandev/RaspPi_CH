# 可以從 https://www.twilio.com/docs/python/install 下載幫助程式庫
from twilio.rest import Client
import json

# 這些信息來自 twilio.com/console 的您的帳戶 Sid 和 身份驗證令牌(Auth Token)
# 用json文件帳戶信息比較安全的編碼 (信息安全問題)。 請參考 http://twil.io/secure
with open('config/twilio.json') as f:
  data = json.load(f)
# print(data)

account_sid = data['twilio_sid']
auth_token = data['twilio_auth']
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="這是Raspberry Pi的短信測試-JSON文件",
                     from_=data['twilio_from'],          # 短信發出號碼 (Twilio號碼)
                     to=data['twilio_to']                # 短信接收號碼
                 )
#打印短信識別碼
print(message.sid)


