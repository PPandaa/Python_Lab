import time
from datetime import datetime

timeData = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(timeData)
time.sleep(1)

bd = datetime.strptime("1997-05-02 17:05:02", "%Y-%m-%d %H:%M:%S")
print("Peter Birthday "+ str(bd))