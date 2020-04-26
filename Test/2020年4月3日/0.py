import datetime
import time
print(time.time())
print(datetime.datetime.now())
print(datetime.datetime.now().date())
print(datetime.datetime.now().date()-datetime.timedelta(days=30))