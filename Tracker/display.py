from Tracker.stats import stats, DPI
import time

# Last display time
last_display_time = time.time()

# Store the previous state of the stats
previous_stats = stats.copy()

# Function to check if data has changed
def has_data_changed():
    global previous_stats
    return any(previous_stats[key] != stats[key] for key in stats)

# Function to update the terminal display
def update_display():
    global last_display_time, previous_stats
    current_time = time.time()

    # Only update if data has changed
    if has_data_changed():
        mouse_distance_str = f"{round(stats['mouse_distance'], 2)} pixels ({mouse_distance_inches()})"
        scroll_distance_str = f"{round(stats['scroll_distance'], 2)} pixels ({scroll_distance_inches()})"

        print(f"\r====== Input Tracker Statistics ({stats['last_updated']}) ======", end="")
        print(f"\nMouse Moved Distance: {mouse_distance_str}", end="")
        print(f"\nMouse Clicks: {stats['mouse_clicks']}", end="")
        print(f"\nScroll Distance: {scroll_distance_str}", end="")
        print(f"\nKey Presses: {stats['key_presses']}", end="\n")

        last_display_time = current_time
        previous_stats = stats.copy()
# Convert pixel distances to inches
def mouse_distance_inches():
    return f"{round(stats['mouse_distance'] / DPI, 2)} in"

def scroll_distance_inches():
    return f"{round(stats['scroll_distance'] / DPI, 2)} in"
