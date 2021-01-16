# 導入需要模塊模塊
import os           # 導入os模塊，用於讀取操作系統中的文件的資訊
import time         # 導入時間模塊sleep()函數

#---------------------------------------------------------------------------------------------------------
# 注意：
# ds18b20的數據引腳必須連接到 GPIO04（pin7）進行1-Wire連接通訊
#---------------------------------------------------------------------------------------------------------
# 從傳感器讀取温度並打印到控制台
# id是傳感器的ID

def readSensor(id):
    
    tfile = open("/sys/bus/w1/devices/"+id+"/w1_slave") # 打開DS18B20的數據文件
    text = tfile.read()                         # 閱讀信息
    tfile.close()                               # 關閉DS18B20的數據文件
    secondline = text.split("\n")[1]            # 尋找換行符号「\n」分界
    temperaturedata = secondline.split(" ")[9]  # 獲取原始温度數據
    temperature = float(temperaturedata[2:])    # 將原始温度數據字串轉換成浮點數温度
    temperature = temperature / 1000            # 計算攝氏温度
    print('傳感器：' + id  + ' - 現在温度： %0.3f C' % temperature)   # 顯示温度

# 在「/sys/bus/w1/devices/」中找到的所有傳感器讀取温度
# DS18B20數字溫度傳感器以「28 -...」開頭
def readSensors():
    count = 0
    sensor = ""
    for file in os.listdir("/sys/bus/w1/devices/"):
    # 檢查操作系統“設備”目錄中的可用文件； 計算機可能有多個傳感器
        if (file.startswith("28-")):    # 找到字首為「28-」的文件（DS18B20的數據文件）
            readSensor(file)            # 讀取數據文件
            count+=1                    # 記錄傳感器數量
    if (count == 0):
        print("找不到傳感器！檢查連接。")

# 每秒讀取所有連接傳感器的温度
def main():                             # 定義「main」函數
    while True:
        readSensors()                   # 召喚用戶定義的「readSensors()」函數獲取温度。
        time.sleep(1)                   # 睡一秒鐘，然後再次檢查温度

# Nothing to cleanup
def destroy():
    pass

# Main starts here
if __name__ == "__main__":
    try:
        main()                          # 召喚「main」函數程式
    except KeyboardInterrupt:
        destroy()

