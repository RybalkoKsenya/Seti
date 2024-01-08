import time
from pywinauto.application import Application
import keyboard

app = Application().Start("E:\PuTTY\putty.exe -ssh ksenya03@tty.sdf.org")
main_window = app.window(title_re=".*PuTTY.*")
main_window.wait('ready')
main_window.set_focus()
keyboard.write('vdi7T3nZjNzxOA')
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(1)
keyboard.send('enter')
time.sleep(10)
