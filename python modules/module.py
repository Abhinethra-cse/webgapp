#math module
import math
print(math.pi)

#random module
import random 
print(random.randint(1,10))

#datetime module
import datetime 
now=datetime.datetime.now()
print(now)

#time module
import time
time.sleep(5)
print("Waited 5 seconds")

#os module
import os
os.remove("sample.txt")

#sys module
import sys
print(sys.version)

# statistics module
import statistics
print(statistics.mean([5, 8, 2, 4]))

#json module
import json
print(json.dumps({"name": "amar"}))

#csv module
import csv
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# re module
import re
print(re.findall(r"\d+", "My phone 1234"))

# urllib module
import urllib.request
response = urllib.request.urlopen('https://example.com')
print(response.status)

# requests module
import requests
r = requests.get("https://github.com/Abhinethra-cse")
print(r.status_code)

#g BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup('Hello', 'html.parser')
print(soup.h1.text)

#pprint module
from pprint import pprint
data = {"a": 1, "b": 2, "c": 3}
pprint(data)

#g random.choice module
import random
print(random.choice(["orange", "plum", "cherry"]))

# collections.Counter module
from collections import Counter
print(Counter("orange"))

# collections.defaultdict module
from collections import defaultdict
d = defaultdict(int)
d['a'] += 1
print(d)

# collections.namedtuple module
from collections import namedtuple
Point = namedtuple('Point', 'x y')
p = Point(30, 40)
print(p.x)

# itertools.count module
import itertools
counter = itertools.count(start=1, step=1)
print(next(counter))

#itertools.cycle module
import itertools
colors = itertools.cycle(['pink','white'])
print(next(colors))

#itertools.permutations module
import itertools
print(list(itertools.permutations([3,4,5])))

 #tertools.combinations module
import itertools
print(list(itertools.combinations([6,7,8],2)))

# shutil.copy module
import shutil
shutil.copy('file1.txt','file2.txt')

#glob module
import glob
print(glob.glob('*.txt'))

# hashlib module
import hashlib
print(hashlib.md5(b"hello").hexdigest())

# uuid module
import uuid
print(uuid.uuid4())

# logging module
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Program started")

# threading module
import threading
threading.Thread(target=lambda: print("Thread running")).start()

#functools.lru_cache module
from functools import lru_cache
lru_cache()
def add(x,y): return x+y
print(add(8,9))

#functools.reduce
from functools import reduce
print(reduce(lambda a,b: a+b, [5,2,1]))

#pathlib module
from pathlib import Path
print(Path.cwd())

#sqlite3 module
import sqlite3
conn = sqlite3.connect('test.db')

#array module
from array import array
arr = array('i',[1,2,3])
print(arr)

#decimal module
from decimal import Decimal
print(Decimal('0.1') + Decimal('0.2'))

# fractions.Fraction module
from fractions import Fraction
print(Fraction(5,3)+Fraction(2,3))

#subprocess module
import subprocess
print(subprocess.run(['echo','Hello']))

#calendar module
import calendar
print(calendar.month(2025, 1))

# zipfile module
import zipfile
with zipfile.ZipFile('test.zip','w') as z:
    z.write('file.txt')

# tarfile module
import tarfile
with tarfile.open('test.tar','w') as t:
  t.add('file.txt')

# base64 module
import base64
print(base64.b64encode(b"hello"))

#getpass module
import getpass
pwd = getpass.getpass()

#socket module
import socket
print(socket.gethostname())

# tkinter module
import tkinter as tk
root = tk.Tk()
root.mainloop()

# email module
from email.message import EmailMessage
msg = EmailMessage()
msg['Subject'] = 'Test'

# smtplib module
import smtplib
# server = smtplib.SMTP('smtp.gmail.com',587)

#multiprocessing module
import multiprocessing
p = multiprocessing.Process(target=print, args=("Hello",))
p.start()

# pickle module
import pickle
pickle.dump({"a":1}, open('data.pkl','wb'))

# copy module
import copy
x = [4,5,6]
y = copy.copy(x)
print(y)

#typing module
from typing import List
nums: List[int] = [4,7,8]
print(nums)

#enum module
from enum import Enum
class Color(Enum): RED=1; GREEN=2
print(Color.RED)