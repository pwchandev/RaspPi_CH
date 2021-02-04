# 導入smtplib 實現電郵發送功能
import smtplib
from email.message import EmailMessage
import json

# 用json文件帳戶信息比較安全的編碼 (信息安全問題)。
with open('config/email.json') as f:
  data = json.load(f)
# print(data)


#電郵變數和常數
SMTP_SERVER = data['email_smtp_server']     # 電子郵件服務器（例如: 谷歌SMTP服務器)。
SMTP_PORT_SSL = data['email_smtp_port_ssl'] # 電子郵件服務器SSL端口 (例如: 谷歌SMTP服務器SSL端口)
USERNAME = data['email_username']           # 更改此設置以匹配你的電郵帳戶
PASSWORD = data['email_password']           # 更改此設置以匹配你的電郵帳戶應用程式密碼
sendFrom = data['email_sendFrom']           # 更改此設置以匹配你的發出電郵帳戶
sendTo = data['email_sendTo']               # 更改此設置以匹配你的接收電郵帳戶

msg = EmailMessage()
msg['Subject'] = "歡迎樹莓派 (Raspberry Pi)" # 更改此設置以匹配你發出電郵主題      
msg['From'] = sendFrom
msg['To'] = sendTo
msg.set_content("中文電子郵件測試 - Test Email!") # 更改此設置以匹配你發出電郵內容

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT_SSL) as session:
        #登入到你的電郵
        session.login(USERNAME, PASSWORD)
        session.send_message(msg)
        session.quit()

# 注意:  這方法可以發出中文和英文電郵主題和內容



