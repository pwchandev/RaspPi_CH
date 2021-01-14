# 導入必要的模塊包
import RPi.GPIO as GPIO
import time

# ADC0832 模擬到數字轉換器 - 引脚定義
ADC_CS  = 17
ADC_CLK = 27
ADC_DIO = 18

def setupADC():                             # 模擬到數字轉換器(ADC)設置函數                   
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)                  # 引脚用GPIO位置設置
    GPIO.setup(ADC_CS, GPIO.OUT) 
    GPIO.setup(ADC_CLK, GPIO.OUT)

def getResult(channel=0):                   # 獲得數字轉換器(ADC)結果
    GPIO.setup(ADC_DIO, GPIO.OUT)
    GPIO.output(ADC_CS, 0)
    
    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)

    GPIO.output(ADC_DIO, channel);  time.sleep(0.000002)

    GPIO.output(ADC_CLK, 1)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    GPIO.output(ADC_CLK, 0)
    GPIO.output(ADC_DIO, 1);  time.sleep(0.000002)
    
    dat1 = 0
    for i in range(0, 8):
        GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)
        GPIO.setup(ADC_DIO, GPIO.IN)
        dat1 = dat1 << 1 | GPIO.input(ADC_DIO)  # or ?
    
    dat2 = 0
    for i in range(0, 8):
        dat2 = dat2 | GPIO.input(ADC_DIO) << i
        GPIO.output(ADC_CLK, 1);  time.sleep(0.000002)
        GPIO.output(ADC_CLK, 0);  time.sleep(0.000002)
    
    GPIO.output(ADC_CS, 1)
    GPIO.setup(ADC_DIO, GPIO.OUT)

    if dat1 == dat2:
        return dat1
    else:
        return 0

def getResult1():              # 「getResult1」函數 - 通道1结果
    return getResult(1)


def main():
    while True:
        res = getResult()      # 召喚「getResult」函數獲取结果(0-255)
        print('結果 = {}'.format(res))
        time.sleep(0.4)        # 睡0.4秒再從ADC獲取结果

if __name__ == '__main__':
    print('啟動程式 ...')
    setupADC()
    try:
        main()
    except KeyboardInterrupt:
        pass
    finally:
        print('完成程式 ...')
        GPIO.cleanup()          # 按「Ctrl+C」清除GPIO端口並退出程式  

