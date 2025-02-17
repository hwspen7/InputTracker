from datetime import datetime

from Tracker.tracker import last_updated

DPI = 96  # Pixels per inch

# Global statistics dictionary
stats = {
    "mouse_distance": 0,  # Mouse movement distance in pixels
    "mouse_clicks": 0,  # Total mouse clicks
    "scroll_distance": 0,  # Scroll wheel movement in pixels
    "key_presses": 0,  # Total keyboard presses
    "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Last updated timestamp
}
last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")