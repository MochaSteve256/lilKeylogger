from pynput import keyboard

def on_press(key):
    try:
        print(' {0} pressed'.format(
            key.char))
    except AttributeError:
        print(' {0} pressed'.format(
            key))

with keyboard.Listener(
        on_press=on_press) as listener:
    listener.join()
