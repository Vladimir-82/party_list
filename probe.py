import os
import time
path = "e:\\Kostuykevich\\Моя работа\\КПВУ Н"
for dirpath, dirnames, dirfiles in os.walk(path):
    for n in dirfiles:
        full_file_time = os.path.join(dirpath, n)
        secs = os.path.getctime(full_file_time)
        file_time = time.gmtime(secs)
        if file_time[0] == 2021:
            print(full_file_time, secs, file_time)

for dirpath, dirnames, dirfiles in os.walk(path):
    print(os.path.dirname(dirpath))
# print(os.path.getsize(path))
