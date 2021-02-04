# 導入smtplib 實現電郵發送功能
import smtplib
import imghdr                       # 導入imghdr測試附件類型
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
msg['Subject'] = "歡迎樹莓派 - 附件測試"   # 更改此設置以匹配你發出電郵主題     
msg['From'] = sendFrom
msg['To'] = sendTo
msg.set_content("中文電子郵件附件測試 - attachment testing")  # 更改此設置以匹配你發出電郵內容

# 附件1張圖片
image_file = 'rasp-pi-4.jpg'        # 圖片文件名稱
with open(image_file, 'rb') as f:   # 讀取文件轉變為文件數據，類型和名稱
    file_data = f.read()
    file_type = imghdr.what(f.name) # 確定圖像類型
    file_name = f.name
# 加入圖片附件到電郵信息內
msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)

# 附件1個PDF文件 (可以是其它規格文件)
pdf_file = 'test.pdf'               # 文件名稱
with open(pdf_file, 'rb') as f:     # 讀取文件轉變為文件數據和名稱
    file_data = f.read()
    file_name = f.name
msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT_SSL) as session:
        #登入到你的電郵
        session.login(USERNAME, PASSWORD)
        session.send_message(msg)
        session.quit()

# 注意:  這方法可以發出中文和英文電郵主題和內容


