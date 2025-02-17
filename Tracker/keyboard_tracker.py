from Tracker.stats import stats
from datetime import datetime
from pynput import keyboard

# Keyboard key press event handler
def on_press(key):
    stats["key_presses"] += 1
    stats["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the keyboard listener
def start_keyboard_listener():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
