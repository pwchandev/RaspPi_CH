import time
# 導入max7219安裝模塊庫
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.led_matrix.device import max7219
# 導入字體庫
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, LCD_FONT
# 中文顯示
from PIL import ImageFont
# 滾動文字			
from luma.core.virtual import viewport 

# 實例化max7219對象
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

def displayFont():			   # 顯示字體在max7219
    # CP437字體 (https://en.wikipedia.org/wiki/Code_page_437#Character_set)
    m1 = [chr(x) for x in range(65, 73)]   # 'A' to 'H'
    m2 = [chr(x) for x in range(48, 58)]   # '0' to '9'
    m3 = [chr(0)]                          # 空值
    msg = m1 + m2 + m3
    print(msg)
    for i in range(0, len(msg)):
        with canvas(device) as draw:
            text(draw, (0, 0), msg[i], fill="white", font=proportional(CP437_FONT))
        time.sleep(0.5)

def scrollFont(): 
    # 滾動文字
    msg = "max7219 8x8 matrix - fast"
    print(msg)
    # 快速滾動文字
    show_message(device, msg, fill="white", font=proportional(CP437_FONT))
    time.sleep(1)
    # 慢速滾動文字
    msg = "max7219 8x8 matrix - slow"
    show_message(device, msg, fill="white", font=proportional(LCD_FONT), scroll_delay=0.2)
    time.sleep(1)
    # 滾動文字滾動文字向上
    words = "Hong Kong SAR"+ "  "      
    virtual = viewport(device, width=device.width, height=len(words) * 8)
    with canvas(virtual) as draw:
        for i, word in enumerate(words):
            text(draw, (0, i * 8), word, fill="white", font=proportional(CP437_FONT))
    for i in range(virtual.height - device.height):
        virtual.set_position((0, i))
        time.sleep(0.2)

def displayZH():
    # 8x8 中文字體
    font = ImageFont.truetype("fonts/zpix-v3.1.1.ttf", 8)
    # 用PIL用模塊劃圖和字
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="white", fill="black")
    time.sleep(1)
    # 顯示中文字
    msg = "中文易学" + " "
    for i in range(0,len(msg)):
        with canvas(device) as draw:
            draw.text((0, 0), msg[i], fill="white", font=font)
        time.sleep(2)

if __name__ == '__main__':
    displayFont()
    scrollFont()
    displayZH()
    


