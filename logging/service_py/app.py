import random
import string
import time
from time import sleep, gmtime, strftime

min_num = 1
max_num = 5

while True:
   rndString = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(21))
   dats = strftime("%Y-%m-%dT%H:%M:%S      ", gmtime())
   print(dats, 'python', rndString)
   num = random.random() * (max_num - min_num) + min_num
   time.sleep(num)

