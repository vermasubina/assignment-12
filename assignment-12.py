#Q-1.
import datetime as dt
print(dt.date.today())

#Q-2.
import webbrowser
a=input("search video")
webbrowser.open_new_tab('http://youtube.com/search?q=%s'%a)

#Q-3.
import os
path = '/Users/subu/Desktop/hello-git/directory'
files = os.listdir(path)
i = 1

for file in files:
    a=input("name of file")
    os.rename(os.path.join(path, file), os.path.join(path, a+'.jpg'))
    i = i+1
