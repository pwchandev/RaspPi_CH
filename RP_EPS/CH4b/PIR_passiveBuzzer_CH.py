# 導入必要的模塊包
import RPi.GPIO as GPIO     
import time         

PIRpin = 17                             # 被動紅外線傳感器(PIR)引脚 GPIO17
BZRpin = 18                             # 蜂鳴器引脚 GPIO18
buzzer = ''

def setupBuzzer():                      # 蜂鳴器設置函數
    GPIO.setmode(GPIO.BCM)              # 引脚用GPIO位置設置
    GPIO.setup(BZRpin, GPIO.OUT)        # 引脚模式設置為輸出
    GPIO.output(BZRpin, GPIO.LOW)
    buzzer = GPIO.PWM(BZRpin, 50)       # 頻率：50Hz; 産生蜂鳴器脈衝
    # 設置 PIR引脚的輸入模式默認 0v（LOW）
    buzzer.start(0)                     # Duty cycle:0 啟動蜂鳴器
    GPIO.setup(PIRpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    return buzzer                       # 返回蜂鳴器對象

def soundBuzzer(buzzer):                # 蜂鳴器發聲函數
    buzzer.ChangeDutyCycle(50)          # 啟動蜂鳴器發聲
    for f in range(100, 2000, 100):
        buzzer.ChangeFrequency(f)       # 改變頻率産生不同的聲音
        time.sleep(0.2)                  
#     for f in range(2000, 100, -100):
#         buzzer.ChangeFrequency(f)
#         time.sleep(0.2) 
    buzzer.ChangeDutyCycle(0)           # 停止蜂鳴器發聲

def main(buzzer):           # 程式的主要
    while True:
        # 檢測到移動時 PIR引腳 將變為3.3v（HIGH）
        if GPIO.input(PIRpin) == GPIO.LOW:  
                print('...未檢測到移動!')    
                time.sleep(1)       # 睡眠1秒鐘，然後再次檢查PIR傳感器的狀態 
        else:
                print('檢測到移動!...')
                soundBuzzer(buzzer) # 發出蜂鳴聲

if __name__ == '__main__':              
    # 程序從這裡開始。 此「if」語句對於確定程式是否執行本身程式或其他程式的一部分。
    # (即是否使用「導入模塊包」獲取該程式的功能)
    print ('啟動程式 ...')
    buzzer = setupBuzzer()              # 初始化蜂鳴器設置（例如GPIO引脚模式和引脚設置）
    try:
        main(buzzer)                    # 轉到「main()」函數調用以啟動程式

    except KeyboardInterrupt:
        print('完成程式 ...')
        buzzer.stop()                   # 停止蜂鳴器
        GPIO.cleanup()                  # 按「Ctrl+C」清除GPIO端口並退出程式         



