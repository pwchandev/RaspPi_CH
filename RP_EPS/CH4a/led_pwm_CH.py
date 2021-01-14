# 導入 GPIO 模塊庫
import RPi.GPIO as GPIO

# 設置GPIO 17來驅動LED秒    
GPIO.setmode(GPIO.BCM)
GPIO_PIN=17
freq=500                                        # 每秒500脈衝或500Hz
duty_cycle=100                                  # 100％或全亮度LED
GPIO.setup(GPIO_PIN, GPIO.OUT)                  # 設置GPIO引針17為輸出

# 設置脈衝寬調製
led = GPIO.PWM(GPIO_PIN, freq)
led.start(duty_cycle)                           # 啟動GPIO引針17脈衝寬調製 


# 調整「duty_cycle」變數以使LED變暗變光
while True:
    duty_cycle = int(input("輸入亮度LED(0到100):"))
    if duty_cycle >= 0 and duty_cycle <= 100:
        led.ChangeDutyCycle(duty_cycle)         # 較暗光LED
    else:
        break
    freq=int(input("輸入脈衝寬調製頻率 (> 1)Hz: "))# 輸入脈衝寬調製頻率 
    led.ChangeFrequency(freq)                   # 更改脈衝寬調製頻率

print('完成程式...清理所有GPIO端口')
led.stop(duty_cycle)                            # 停止GPIO引針17脈衝寬調製 
GPIO.cleanup()                                  # 清理所有GPIO端口 


