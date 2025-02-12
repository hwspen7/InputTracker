import threading
import pynput
import time
import math
from datetime import datetime

DPI = 96  # Pixels - inch

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
# Track the last time the display was updated
last_display_time = time.time()


# Convert pixels to inches and feet with 2 decimal precision
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

        # Calculate Euclidean distance
        distance = math.sqrt(dx ** 2 + dy ** 2)
        stats["mouse_distance"] += distance
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_display()
    last_position = (x, y)


# Mouse click event handler
def on_click(x, y, button, pressed):
    global last_updated
    if pressed:
        stats["mouse_clicks"] += 1
        last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        update_display()


# Mouse scroll event handler
def on_scroll(x, y, dx, dy):
    global last_updated
    # Approximate each scroll as 3 pixels, rounded
    stats["scroll_distance"] += round(abs(dy) * 3, 2)
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_display()


# Keyboard key press event handler
def on_press(key):
    global last_updated
    stats["key_presses"] += 1
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    update_display()


# Function to update terminal display in place without clearing the screen
def update_display():
    global last_display_time
    current_time = time.time()
    # Update every 1 second
    if (current_time - last_display_time) >= 1.0:
        mouse_distance_str = f"{round(stats['mouse_distance'], 2)} pixels ({pixels_to_inches_feet(stats['mouse_distance'])})"
        scroll_distance_str = f"{round(stats['scroll_distance'], 2)} pixels ({pixels_to_inches_feet(stats['scroll_distance'])})"

        print(f"\r====== Input Tracker Statistics ({last_updated}) ======", end="")
        print(f"\nMouse Moved Distance: {mouse_distance_str}", end="")
        print(f"\nMouse Clicks: {stats['mouse_clicks']}", end="")
        print(f"\nScroll Distance: {scroll_distance_str}", end="")
        print(f"\nKey Presses: {stats['key_presses']}", end="\n")
        last_display_time = current_time  # Update last display time


# Start listening for mouse and keyboard events
def start_listener():
    with pynput.mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as mouse_listener, \
            pynput.keyboard.Listener(on_press=on_press) as keyboard_listener:
        mouse_listener.join()
        keyboard_listener.join()


# Run the listener in a separate thread
if __name__ == "__main__":
    threading.Thread(target=start_listener, daemon=True).start()
    while True:
        time.sleep(0.5)




