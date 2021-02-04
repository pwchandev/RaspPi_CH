# 導入smtplib 實現電郵發送功能
import smtplib

#電郵變數和常數
SMTP_SERVER = 'smtp.xxxxx.com'      # 電子郵件服務器（例如: 谷歌SMTP服務器)。
SMTP_PORT_SSL = xxx                 # 電子郵件服務器SSL端口 (例如: 谷歌SMTP服務器SSL端口)
USERNAME = 'xxxxxxxx@xxxxx.com'     # 更改此設置以匹配你的電郵帳戶
PASSWORD = 'xxxxxxxxxxxxxxxx'       # 更改此設置以匹配你的電郵帳戶應用程式密碼
sendFrom = 'xxxxxxxx@xxxxx.com'     # 更改此設置以匹配你的發出電郵帳戶
sendTo = 'xxxxxxxx@xxxxx.com'       # 更改此設置以匹配你的接收電郵帳戶
emailSubject = "Welcome email from Raspberry Pi"  # 更改此設置以匹配你發出電郵主題
emailContent = "This is a new email test - Raspberry Pi"  # 更改此設置以匹配你發出電郵內容

with smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT_SSL) as session:
        #登入到你的電郵
        session.login(USERNAME, PASSWORD)
        subject = emailSubject
        body = emailContent
        msg = f'Subject: {subject}\n\n{body}'
        session.sendmail(sendFrom, sendTo, msg)
        session.quit()
        
# 注意:  這方法只可以發出英文電郵主題和內容



