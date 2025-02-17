from Tracker.stats import stats
import math
from datetime import datetime
from pynput import mouse

# Store last mouse position
last_position = None

# Mouse movement event handler
def on_move(x, y):
    global last_position
    if last_position is not None:
        dx = x - last_position[0]
        dy = y - last_position[1]
        distance = math.sqrt(dx**2 + dy**2)
        stats["mouse_distance"] += distance
        stats["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    last_position = (x, y)

# Mouse click event handler
def on_click(x, y, button, pressed):
    if pressed:
        stats["mouse_clicks"] += 1
        stats["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Mouse scroll event handler
def on_scroll(x, y, dx, dy):
    stats["scroll_distance"] += round(abs(dy) * 3, 2)
    stats["last_updated"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# Start the mouse listener
def start_mouse_listener():
    with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
        listener.join()
