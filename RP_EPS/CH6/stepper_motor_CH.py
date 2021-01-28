import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# ins1=GPIO4, ins2=GPIO17, ins3=GPIO27, ins4=GPIO22
control_pins = [4,17,27,22]

class steppers:
    def __init__(self, control_pins):
        self.control_pins = control_pins
        self.halfstep_seq = [[1,0,0,0],[1,1,0,0],[0,1,0,0],[0,1,1,0],
                             [0,0,1,0],[0,0,1,1],[0,0,0,1],[1,0,0,1]]    
        for pin in self.control_pins:
           GPIO.setup(pin, GPIO.OUT)
           GPIO.output(pin, 0)
                             
    def step_clk(self, steps=1, tsec=0.001):
        print(f'步進電機順時針旋轉 {steps} 步數')
        for i in range(steps):
          for halfstep in reversed(range(8)):
            for pin in range(4):
              GPIO.output(self.control_pins[pin], self.halfstep_seq[halfstep][pin])
            # time.sleep(0.001)
            time.sleep(tsec)

    def step_atclk(self, steps=1, tsec=0.001):
        print(f'步進電機逆時針旋轉 {steps} 步數')
        for i in range(steps):
          for halfstep in range(8):
            for pin in range(4):
              GPIO.output(self.control_pins[pin], self.halfstep_seq[halfstep][pin])
            # time.sleep(0.001)
            time.sleep(tsec)
                             
    def step_idle(self, tsec=1):
        print(f'步進電機處於閒置狀態 {tsec} 秒。')
        for pin in range(4):
            GPIO.output(self.control_pins[pin], 0)
        time.sleep(tsec)                   
                             
def main():
    step_motor = steppers(control_pins)
    # 計算出每度轉的步數
    ratio = 512/360
    degree = 0
    while True:
        degree = float(input('請輸入需要順時針旋轉角度？ '))
        turn = int(degree*ratio)
        print(f'順時針旋轉從基點旋轉的角度 {turn}')
        step_motor.step_clk(turn,0.01)
        # 步進電機處於閒置狀態秒數時間
        step_motor.step_idle(3)
        # 逆時針旋轉一整圈
        step_motor.step_atclk(512)
        time.sleep(3)

if __name__ == '__main__':
    print('啟動程式...')
    try:
        while True:
             main()
        # 通過按 CTRL+C 重置
    except KeyboardInterrupt:
        print('完成程式...')
        GPIO.cleanup()
