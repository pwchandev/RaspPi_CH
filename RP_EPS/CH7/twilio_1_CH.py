# 可以從 https://www.twilio.com/docs/python/install 下載幫助程式庫
from twilio.rest import Client

# 這些信息來自 twilio.com/console 的您的帳戶 Sid 和 身份驗證令牌(Auth Token)
# 危險！ 這是不安全的編碼 (信息安全問題)。 請參考 http://twil.io/secure
account_sid = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="這是Raspberry Pi的短信測試",
                     from_='+aaaaaaaaaaa',          # 短信發出號碼 (Twilio號碼)
                     to='+bbbbbbbbbbb'              # 短信接收號碼
                 )
#打印短信識別碼
print(message.sid)



