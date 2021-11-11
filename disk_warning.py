import os
import time
import sys
import logging
import utils
import paramiko
import psutil
import collections

from apscheduler.schedulers.background import BackgroundScheduler # 当调度器需要后台运行时使用
from apscheduler.triggers.interval import IntervalTrigger # 当以固定的时间间隔运行 job 时使用
# 开启磁盘空间检测
schedule = BackgroundScheduler()
# 间隔XX开启一个检测(根据需求进行设置时间)
intervalTrigger = IntervalTrigger(minutes=1)
# 给检测任务设定个id,方便任务的取消
schedule.add_job(utils.spaceMonitorJob, trigger=intervalTrigger, id='id_space_monitor')
schedule.start()

# 禁止apscheduler相关信息屏幕输出
logging.getLogger('apscheduler.executors.default').propagate=False
logging.error('check webroot space error.')

# 移除任务，并关闭schedule任务
schedule.remove_job(job_id='id_space_monitor')
schedule.shutdown(wait=False)
sys.exit(-3)
