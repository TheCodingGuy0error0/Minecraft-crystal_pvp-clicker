from pynput.keyboard import Controller as KeyboardController, Key
from pynput.mouse import Button, Controller as MouseController
import time
import threading


running = False
cycle_thread = None

def crystal_cycle():
    while running:
        mouse.click(Button.left)
        time.sleep(0.05)
        mouse.click(Button.right)
        time.sleep(0.05)

def on_press(key):
    global running, cycle_thread
    try:
        if key.char and key.char.lower() == 'l':
            if not running:
                running = True
                cycle_thread = threading.Thread(target=crystal_cycle)
                cycle_thread.start()
            else:
                running = False
                cycle_thread.join()
    except AttributeError:
        pass  # Special keys (not used here)

if __name__ == "__main__":
    print("Press L to start/stop crystal cycle loop.")
    with Listener(on_press=on_press) as listener:
        listener.join()
