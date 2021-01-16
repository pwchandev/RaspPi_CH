# 導入必要的模塊包
import RPi.GPIO as GPIO    
import time

# TM1638 引脚定義
DIO = 27                # 使用 GPIO27（引腳13）進行數據輸入/輸出（DIO）
CLK = 18                # 使用 GPIO18（引腳12）用於時鐘（CLK）
STB = 17                # 使用 GPIO17（引腳11）進行芯片選擇（STB）
LSBFIRST = 0            # 初始化變數和常數
MSBFIRST = 1
tmp = 0                 

# TM1638標準API函數
def _shiftOut(dataPin, clockPin, bitOrder, val): # TM1638「_shiftOut()」函數
        for i in range(8):
                if bitOrder == LSBFIRST:
                        GPIO.output(dataPin, val & (1 << i))
                else:
                        GPIO.output(dataPin, val & (1 << (7 -i)))
                GPIO.output(clockPin, True)
                time.sleep(0.000001)                    
                GPIO.output(clockPin, False)
                time.sleep(0.000001)                    
        
def sendCommand(cmd):                            # TM1638「_sendCommand()」函數
        GPIO.output(STB, False)
        _shiftOut(DIO, CLK, LSBFIRST, cmd)
        GPIO.output(STB, True)

def TM1638_init():                               # TM1638「TM1638_init()」函數 - 用於初始化
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(DIO, GPIO.OUT)
        GPIO.setup(CLK, GPIO.OUT)
        GPIO.setup(STB, GPIO.OUT)
        sendCommand(0x8f)

def numberDisplay(num):                          # TM1638「numberDisplay()」函數 - 整數顯示
        digits = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
        sendCommand(0x40)
        GPIO.output(STB, False)
        _shiftOut(DIO, CLK, LSBFIRST, 0xc0)
        _shiftOut(DIO, CLK, LSBFIRST, digits[num//1000%10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[num//100%10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[num//10%10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[num%10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        GPIO.output(STB, True)

def numberDisplay_dec(num):                      # TM1638「numberDisplay_dec()」函數 - 浮點數顯示
        digits = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f]
        integer = 0
        decimal = 0
        pro = int(num * 100)
        integer = int(pro / 100)
        decimal = int(pro % 100)
        sendCommand(0x40)
        GPIO.output(STB, False)
        _shiftOut(DIO, CLK, LSBFIRST, 0xc0)
        _shiftOut(DIO, CLK, LSBFIRST, digits[integer//10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[integer%10] | 0x80)
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[decimal//10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, digits[decimal%10])
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)


def numClear():                                 # TM1638「numClear()」函數 - 清理顯示
        sendCommand(0x40)
        GPIO.output(STB, False)
        _shiftOut(DIO, CLK, LSBFIRST, 0xc0)
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)     # 個位數字
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)     # 十位數字
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)     # 百位數字
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)     # 千位數字
        _shiftOut(DIO, CLK, LSBFIRST, 0x00)
        GPIO.output(STB, True)
        time.sleep(1)

def destroy():                                  # 清理 GPIO 端口
    GPIO.cleanup()

def main():                                     # 定義「main」函數
    print('數字: 十進制整數 ...')
    for i in range (0,10000):
        numberDisplay(i)                        # TM1638顯示整數
        time.sleep(0.001)
    numClear()
    print('數字: 十進制有2個小數點...')
    for i in range (0,10000):
        num = i/100
        numberDisplay_dec(num)                  # TM1638顯示浮點數和2小數點
        time.sleep(0.001)
    numClear()
        

if __name__ == '__main__':                      # 程式從這裡開始
    print('啟動程式...')
    TM1638_init()                               # 召喚「TM1638_ini()」函數來初始化 TM1638 LED 顯示
    try:
        main()          
    except KeyboardInterrupt:                   # 當按下「Ctrl+C」時，完成執行程式。
        print('完成程式...')
        destroy()
    
