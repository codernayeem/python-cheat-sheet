# *** Working with Path ***
print("************** Pathlib **************")

from pathlib import Path
import os

p = Path("C:\\Program Files\\Microsoft")  # absulote path
p = Path(r"C:\Program Files\Microsoft")

p = Path()   # current path
p = Path("data\\files\\pdf files")               # relative path
p2 = Path("data\\files\\pdf files\\data.txt")    # relative path

# Joining path
p1 = Path('data') / Path("files\\pdf files") / "abcd" / "abcd.txt"
p12 = Path('data') / Path("files\\pdf files") / "abcd"
# os.path.join('data', "files\\pdf files", "abcd")

print(p.exists())  # True
print(p.is_file()) # False
print(p.is_dir())  # True

print(p.name)      # the name of the folder/file
print(p.stem)      # the name of the folder/file without extension
print(p2.suffix)   # returns the extension
print(p.parent)    # the name of the parent of the folder/file
print(p.absolute())  # return the absolute path

# p12.mkdir()             |  create directory
# p12.rename("anything")  |  rename directory
# p12.rmdir()             |  remove directory
p3 = p2.with_name("data2.txt")  # Just cahnge the name and retuns that new path
p3 = p2.with_suffix(".dat")     # Just cahnge the extention and retuns that new path
print(p3)


path = Path("data\\files\\pdf files")
for p in path.iterdir():
    print(p) # print all dir/files

all_files_folder = list(path.iterdir())
all_files = [p for p in path.iterdir() if p.is_file()]
all_dirs = [p for p in path.iterdir() if p.is_dir()]

path = Path("a_package")
py_files = [p for p in path.glob('*.py')]        # search only that directory
all_py_files = [p for p in path.rglob('*.py')]   # search that directory and it's child directories


from time import ctime

path = Path("data\\files\\pdf files") / 'data.txt'
if path.exists() and path.is_file():
    path.stat()   # info about this file like: size, atime, mtime, ctime
    print(ctime(path.stat().st_ctime))
    print(ctime(path.stat().st_mtime))
    # path.unlink()   |   delete that file

    print(path.read_text())  # reading data from that file
    print(path.read_bytes()) # reading data as bytes from that file
    path.write_text("whatever")   # write data to that file
    path.write_bytes(b"whatever")  # write data as bytes to that file

import shutil # this provide many things like: copy, move, getStorageUsage, make archive
shutil.copy(Path("data\\files\\pdf files\\data.txt"), Path("data\\files\\pdf files\\data3.txt"))



# *** Working with ZIP file ***
print("************** ZIP File **************")

from zipfile import ZipFile
zip_file = ZipFile("data\\files.zip", "w")

for p in Path("a_package").rglob("*.*"):
    zip_file.write(p)
zip_file.close()

# better with 'with'
with ZipFile("data\\files.zip", "w") as zip_file:
    for p in Path("a_package").rglob("*.*"):
        zip_file.write(p)

# reading zipfile
with ZipFile("data\\files.zip") as zip_file:
    print(zip_file.namelist())
    fl_info = zip_file.getinfo("a_package/calcx.py")
    fl_info.is_dir()
    fl_info.file_size
    fl_info.compress_size

    zip_file.extractall('data\\extract')
    zip_file.extract("a_package/calcx.py", 'data\\extract2')


# *** Working with CSV file ***
print("************** CSV **************")

# csv : comma seperated value
import csv

with open("data\\files\\pdf files\\data.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(['name', 'roll', 'marks'])
    writer.writerow(['Nayeem', 56, 85])
    writer.writerow(['Robin', 857, 78])
    writer.writerow(['Kawser', 786, 65])
    writer.writerow(['Sorif', 78, 19])


with open("data\\files\\pdf files\\data.csv") as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)



# *** Working with JSON file ***
print("************** JSON **************")
import json

marks = [45, 96, 752, 35]
data = {
    'name': "nayeem",
    'marks': marks,
    'other': None,
}

json_string = json.dumps(marks) # get json string
print('JSON data :', json_string)

json.dump(data, open("data\\files\\my_data.json", 'w')) # writing to a file directly

json_data = json.loads("""{"name": "nayeem", "marks": [45, 96, 752, 35], "other": null}""") # loads data from json string
print(type(json_data)) # dict

json_data = json.load(open("data\\files\\my_data.json")) # load data from a file
print(json_data)


# *** Working with SQLITE ***
print("******************* SQLITE ******************")

import sqlite3
marks = {'nayeem': 50, 'robin': 45, 'faruk': 48}

conn = sqlite3.connect('data/db.sqlite3')

def create_table():
    command = """CREATE TABLE students (id integer PRIMARY KEY, name text NOT NULL, mark integer NOT NULL)"""
    conn.execute(command)

for name, mark in marks.items():
    command = """INSERT INTO students (name, mark) VALUES (?, ?)"""
    conn.execute(command, (name, mark))

command = "SELECT * FROM students"
cursor = conn.execute(command)
for row in cursor:
    print(row)


# *** Working with TimeStamps, Datetime & TimeDelta ***
print("******* TimeStamps, Datetime & TimeDelta ******")

# timstamp
import time

tm = time.time() # get the current time
print(time.ctime(123456789)) # seconds to actual datetime
# print("Sleeping for 2 seconds")
# time.sleep(2)   # sleep for 2 seconds
# print("Sleeping completed")

import timeit # Measure execution time of small code

print('took ', timeit.timeit("""', '.join(["hi", "hello", "bye"])""", number=10000), 'seconds to run 10000 times')


# datetime
from datetime import datetime

dt = datetime(2002, 1, 1)
dt = datetime.now()
datetime.strptime("2045/05/23", "%Y/%m/%d") # get the datetime from a string by formatting it with directives
datetime.strftime(dt, "%Y/%m/%d")           # get the string from a datetime by formatting it with directives
# Some directives
# %a : get short weekday (Sun , Mon)
# %A : get full weekday (Sunday , Monday)
# %d : get day (01, 24)
# %m : get month (01, 12)
# %b : get short month (Jan, Feb)
# %B : get full month (January, February)
# %y : get short year (99, 20)
# %Y : get full year(1999, 2020)
# %I : get Hour 12-hour clock (4, 12)
# %H : get Hour 24-hour clock (6, 23)
# %M : get minute (10, 59)
# %S : get second (10, 59)
# % % : get '%' character

# convert Timestamp to Datetime
dt1 = datetime.fromtimestamp(time.time())
print(dt.year, dt.day)
dt2 = datetime(2002, 1, 1)
print(dt1 > dt2)


# timedelta
from datetime import timedelta

dt2 = dt1 + timedelta(days=1, seconds=454852)

duration = dt2 - dt1
print(duration)
print(duration.days)
print(duration.seconds)
print('total sec :', duration.total_seconds())


# ******** String ************
print("******** String ************")
import string

print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)

template = string.Template(Path("data/template.html").read_text())
print(template.substitute({"name": "Nayeem"}))

# ******* Generating Random Values **********
print("************ Random ****************")

import random

print(random.random())                  # get a random float < 1
print(random.randint(1, 10))            # get a random int between 1 to 10
print(random.choice(["head", "tail"]))  # get a random element
print(random.choices(['a', 'b', 'c', 'd', 'e', 'f', 'j', 'g'], k=2))  # get 2 random element

print("Random pin :", ''.join(random.choices('1234567890', k=4)))
print("Random password :", ''.join(random.choices(string.digits+string.ascii_letters, k=random.randint(8, 12))))

# shuffle element
numbers = [1, 2, 3, 4]
random.shuffle(numbers)
print('After shuffle:', numbers)


# ************ Webbrower *********
print("************ Webbrower *********")
import webbrowser
webbrowser.open("https://www.google.com") # Opening web browser


# ************ Send Email ***********
print("************ Send Email ***********")
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

message = MIMEMultipart()
message['from'] = "Nayeem"
message['to'] = "someone@gmail.com"
message['subject'] = "This is test"
# message.attach(MIMEText("This is body"))
# body = template.substitute({"name": "Rohim"})
body = template.substitute(name="Rohim")
message.attach(MIMEText(body, 'html'))

try:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo() # saying hello to smtp server
        smtp.starttls()
        smtp.login("testuser@gmail.com", "password123")
        smtp.send_message(message)
        print('Sent')
except smtplib.SMTPAuthenticationError:
    print("Wrong email/Password")
except Exception as e:
    print(e)


# ********** Command Line Arguments **********
print("********** Command Line Arguments **********")

import sys
print(sys.argv)    # all given arguments
print(sys.argv[0]) # first one is always the python file that we are running

if len(sys.argv) == 1:
    print("Please give any argv")
else:
    print("all argvs : ", sys.argv[1:])


# Run externel programs
print('************Run externel programs****************')
import subprocess

try:
    result = subprocess.run(['start', '2_list.py'])
except Exception as e:
    print(e)
else:
    print(type(result))
    print("args", result.args)             # arguments that we provide
    print("returncode", result.returncode) # 0 means success | non-zero means error
    print("stderr", result.stderr)
    print("stdout", result.stdout)         # None

result = subprocess.run(['python', "-h"], capture_output=True, text=True) # capture output
print("returncode", result.returncode) # 0 means success | non-zero means error
print("stderr", result.stderr)
print("stdout", result.stdout)         # The output
