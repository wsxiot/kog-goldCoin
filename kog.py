import logging
import random
import os
from time import sleep
# ---------------在此处设置参数（很重要很重要很重要）--------
# 设备分辨率
device_x, device_y = 1920, 1080

# 时间间隔，单位秒：one(time)two(time)three(time)one
# one，two，three是图片名，详情见./imgs目录
step_wait = [180, 2, 10]

# 刷金币次数
repeat_times = 60
# ------------------------------------

# 日志输出
logging.basicConfig(format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    level=logging.DEBUG)

# 模拟点击函数，可适应不同分辨率
def tap_screen(x, y):
    """calculate real x, y according to device resolution."""
    base_x, base_y = 1920, 1080
    real_x = int(x / base_x * device_x)
    real_y = int(y / base_y * device_y)
    os.system('adb shell input tap {} {}'.format(real_x, real_y))
    logging.info('tap location {} {}'.format(real_x, real_y))

def do_money_work(current_times):
                 
    # click 闯关
    tap_screen(random.randint(1336,1540), random.randint(852,898))
    for i in range(step_wait[0]+random.randint(1,40), 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 0, i))
    
    # click 点击屏幕继续
    tap_screen(random.randint(200,1720), random.randint(200,880))
    for i in range(step_wait[1]+random.randint(1,5), 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 1, i))
    
    # click 再次挑战
    tap_screen(random.randint(1528,1738), random.randint(972,1020))
    for i in range(step_wait[2]+random.randint(1,6), 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 2, i))

if __name__ == '__main__':
    for i in range(repeat_times):
        do_money_work(i+1)