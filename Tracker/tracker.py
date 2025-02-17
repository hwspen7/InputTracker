import pynput
import math
import time
import threading
from datetime import datetime

DPI = 96  # Pixels per inch

# Global statistics dictionary
stats = {
    "mouse_distance": 0,  # Mouse movement distance in pixels
    "mouse_clicks": 0,  # Total mouse clicks
    "scroll_distance": 0,  # Scroll wheel movement in pixels
    "key_presses": 0  # Total keyboard presses
}

# Stores the last recorded mouse position
last_position = None
last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Convert pixels to inches and feet
def pixels_to_inches_feet(pixels):
    inches = round(pixels / DPI, 2)
    feet = int(inches // 12)
    remaining_inches = round(inches % 12, 2)
    return f"{inches} in ({feet} ft {remaining_inches} in)"

# Mouse movement event handler
def on_move(x, y):
    global last_position, last_updated
    if last_position is not None:
        dx = x - last_position[0]
        dy = y - last_position[1]
        stats["mouse_distance"] += math.sqrt(dx**2 + dy**2)
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_position = (x, y)

# Mouse click event handler
def on_click(x, y, button, pressed):
    if pressed:
        stats["mouse_clicks"] += 1

# Mouse scroll event handler
def on_scroll(x, y, dx, dy):
    stats["scroll_distance"] += round(abs(dy) * 3, 2)

# Keyboard key press event handler
def on_press(key):
    stats["key_presses"] += 1

# Start the event listener
def start_listener():
    with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
            pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()

# Run the listener in a separate thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()



