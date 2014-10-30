from datetime import timedelta
import caerus
import tasks
caerus.register_task('periodic task1', 'tasks.hoge', caerus.schedules.schedule(timedelta(seconds=30)))
caerus.register_task('periodic task2', 'tasks.hoge', caerus.schedules.crontab(), args=['fuga'])
