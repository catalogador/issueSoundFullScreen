import pyautogui
import time
from playsound import playsound

def is_full_screen():
    screen_width, screen_height = pyautogui.size()
    active_window = pyautogui.getActiveWindow()

    if active_window:
        window_width, window_height = active_window.size
        return window_width == screen_width and window_height == screen_height
    return False

def main():
    was_full_screen = False

    while True:
        if is_full_screen():
            if not was_full_screen:
                playsound('sound.mp3')
                was_full_screen = True
        else:
            was_full_screen = False

        time.sleep(1)

if __name__ == "__main__":
    main()

