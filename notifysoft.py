import tkinter 
import time
from plyer import notification
import plyer


print('enter the time for notification (HH:MM:SS) : ')
timefornot = input('> ')
print('enter the Title of the notification :')
thistitle = input('> ')
print('enter the body of the notification :')
thisbody = input('> ')
while True:
    currenttime = time.strftime('%H:%M:%S')
    if timefornot == currenttime:
        notification.notify(title=str(thistitle), message=str(thisbody), app_name='python', app_icon='https://tpc.googlesyndication.com/daca_images/simgad/16704393793568578771', timeout=10, toast=False)
        