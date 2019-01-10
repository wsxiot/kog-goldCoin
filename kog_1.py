import logging
import os
from time import sleep
# ---------------在此处设置参数--------
# 设备分辨率
device_x, device_y = 1280, 720

# 时间间隔，单位秒：one(time)three(time)five(time)six(time)one
# one，three，five, six是图片名，详情见./imgs目录
step_wait = [30, 150, 2, 10]

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

def do_money_work(current_times):
                 
    # step one 0
    tap_screen(1466, 920)
    for i in range(step_wait[0], 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 0, i))
    
    # step two 1
    for i in range(step_wait[1], 0, -1):
        tap_screen(1860, 92)
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 1, i))
    
    # step three 2
    tap_screen(960, 540)
    for i in range(step_wait[2], 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 2, i))
    
    # step four 3
    tap_screen(1606, 992)
    for i in range(step_wait[3], 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, 3, i))

if __name__ == '__main__':
    for i in range(repeat_times):
        do_money_work(i+1)