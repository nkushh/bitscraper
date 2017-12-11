from crontab import CronTab

my_cron = CronTab(user = 'pierombaabu')

my_cron.remove_all()
my_cron.write()