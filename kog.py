import logging
import os
from time import sleep
# ---------------在此处设置参数--------
# 设备分辨率
device_x, device_y = 1280, 720

# 时间间隔，单位秒：one()two_1()two_2()three()four()one
step_wait = [30, 2, 150, 2, 10]

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

def sleep_log(current_times, step):
    for i in range(step_wait[step], 0, -1):
        sleep(1)
        logging.info('round #{} step #{} time down #{}'.format(current_times, step, i))

def do_money_work(current_times):
    logging.info('round #{}'.format(current_times))
                 
    # step one 0
    tap_screen(1466, 920)
    sleep_log(current_times, 0)
    
    # step two 1 2
    sleep_log(current_times, 1)
    sleep_log(current_times, 2)
    
    # step three 3
    tap_screen(960, 540)
    sleep_log(current_times, 3)
    
    # step four 4
    tap_screen(1606, 992)
    sleep_log(current_times, 4)

if __name__ == '__main__':
    for i in range(repeat_times):
        do_money_work(i+1)