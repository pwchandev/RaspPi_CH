# ADXL345加速度傳感器庫的簡單演示。 將打印 X，Y，Z 每半秒＃個軸加速度值。
# Author: Tony DiCola
# License: Public Domain

import time

# 導入ADXL345模塊
import Adafruit_ADXL345

# 創建一個ADXL345實例
accel = Adafruit_ADXL345.ADXL345()

# 你可以使用以下參數指定設備地址和I2C總線：:
#accel = Adafruit_ADXL345.ADXL345(address=0x54, busnum=2)

# 你可以選擇將範圍更改為以下之一:
#  - ADXL345_RANGE_2_G   = +/-2G (default)
#  - ADXL345_RANGE_4_G   = +/-4G
#  - ADXL345_RANGE_8_G   = +/-8G
#  - ADXL345_RANGE_16_G  = +/-16G
# 例如設置為 +/-16G：
#accel.set_range(Adafruit_ADXL345.ADXL345_RANGE_16_G)

# 數據速率更改為以下之一：例如設置為 +/-16G：
#  - ADXL345_DATARATE_0_10_HZ = 0.1 hz
#  - ADXL345_DATARATE_0_20_HZ = 0.2 hz
#  - ADXL345_DATARATE_0_39_HZ = 0.39 hz
#  - ADXL345_DATARATE_0_78_HZ = 0.78 hz
#  - ADXL345_DATARATE_1_56_HZ = 1.56 hz
#  - ADXL345_DATARATE_3_13_HZ = 3.13 hz
#  - ADXL345_DATARATE_6_25HZ  = 6.25 hz
#  - ADXL345_DATARATE_12_5_HZ = 12.5 hz
#  - ADXL345_DATARATE_25_HZ   = 25 hz
#  - ADXL345_DATARATE_50_HZ   = 50 hz
#  - ADXL345_DATARATE_100_HZ  = 100 hz (default)
#  - ADXL345_DATARATE_200_HZ  = 200 hz
#  - ADXL345_DATARATE_400_HZ  = 400 hz
#  - ADXL345_DATARATE_800_HZ  = 800 hz
#  - ADXL345_DATARATE_1600_HZ = 1600 hz
#  - ADXL345_DATARATE_3200_HZ = 3200 hz
# 例如設置為6.25Hz：
#accel.set_data_rate(Adafruit_ADXL345.ADXL345_DATARATE_6_25HZ)

def main():
    print('打印「X，Y，Z」軸值，按Ctrl-C退出...')
    while True:
        # 讀取X，Y，Z軸加速度值並打印。
        x, y, z = accel.read()
        print('X={0}, Y={1}, Z={2}'.format(x, y, z))
        # 等待半秒鐘，然後重複。
        time.sleep(0.5)
        

if __name__ == '__main__':
    print ('啟動程式 ...')
    try:
        main()                          # 轉到「main()」函數調用以啟動程式

    except KeyboardInterrupt:
        pass
    
    finally:
        print('完成程式...')                  # 按「Ctrl+C」退出程式         


    