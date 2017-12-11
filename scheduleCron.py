from crontab import CronTab
import os
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
python_path = os.path.join(BASE_DIR, "../bit_venv/bin/python")
worker_file = os.path.join(BASE_DIR, "worker.py")

my_cron = CronTab(user='pierombaabu')

# for job in my_cron:
# 	print(job)
python = python_path
file_to_run = worker_file

job = my_cron.new(command = python+' '+ file_to_run, comment='bitcoininfo')
job.minute.every(30)
my_cron.write()