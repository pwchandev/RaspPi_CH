# 導入需要模塊模塊
import RPi.GPIO as GPIO
import time

# 創建一個從3.0到13.0的浮點數列表以最大化伺服擺幅掃描
control = [x*0.5 for x in range(6, 26)]
servo = 13

# 引脚用GPIO位置設置
GPIO.setmode(GPIO.BCM)
GPIO.setup(servo,GPIO.OUT)

# 伺服馬達操作規格:
# 1.0 毫秒脈衝，持續0度（左）
# 1.5 毫秒脈衝 90度（中等）
# 2.0 毫秒脈衝180度（右）
# 預計每20毫秒更新一次(50hz, 頻率為20毫秒)
# 0度的「Duty Cycle」=（1/20）* 100 = 5％
# 90度的「Duty Cycle」=（1.5 / 20）* 100 = 7.5％
# 180度的「Duty Cycle」=（2/20）* 100 = 10％
# PWM信號的5％「Duty Cycle」相應最左邊的位置。10％「Duty Cycle」相應應極右位置，
# 我們需要改變「Duty Cycle」在5％到10％之間， 從而獲得伺服電機清掃效果。

p=GPIO.PWM(servo,50)      # 設置頻率50hz 
p.start(3.0)              # 啟動「Duty Cycle」(將伺服器設置為0度)

# 伺服電機掃描效果
try:
   while True:
      for x in range(19):
         p.ChangeDutyCycle(control[x])
         # time.sleep(0.03)
         time.sleep(0.5)
         print(x)
      for x in range(18,0,-1):
         p.ChangeDutyCycle(control[x])
         # time.sleep(0.03)
         time.sleep(0.5)
         print(x)
          
except KeyboardInterrupt:
    pass
    
finally:
    x = 9
    p.ChangeDutyCycle(control[x])
    time.sleep(0.5)
    GPIO.cleanup()
