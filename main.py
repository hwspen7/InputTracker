import threading
import time
from Tracker import start_mouse_listener, start_keyboard_listener, update_display

# Start the mouse and keyboard listeners in separate threads
mouse_thread = threading.Thread(target=start_mouse_listener, daemon=True)
keyboard_thread = threading.Thread(target=start_keyboard_listener, daemon=True)

mouse_thread.start()
keyboard_thread.start()

# Keep updating the display
while True:
    update_display()
    time.sleep(0.5)

