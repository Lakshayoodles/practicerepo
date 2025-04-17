import pyautogui
import time
import random
import platform
import subprocess


def move_mouse():
    """Simulate random mouse movement."""
    screenWidth, screenHeight = pyautogui.size()
    x = random.randint(0, screenWidth - 1)
    y = random.randint(0, screenHeight - 1)
    pyautogui.moveTo(x, y, duration=0.5)
    # print(f"move mouse")


def click_mouse():
    """Simulate a mouse click."""
    pyautogui.click()
    # print("click mouse")


def type_random_keys():
    """Simulate typing random keys."""
    keys = ['a', 's', 'd', 'f', 'j', 'k', 'l', ';']
    for i in range(random.randint(3, 8)):
        key = random.choice(keys)
        pyautogui.press(key)
        time.sleep(0.2)
    # print("type random keys")


def switch_window():
    """Simulate switching between windows (Alt+Tab on Windows/Linux, Command+Tab on macOS)."""
    system = platform.system()
    if system == "Windows" or system == "Linux":
        pyautogui.keyDown('alt')
        pyautogui.press('tab')
        pyautogui.keyUp('alt')
    elif system == "Darwin":  # macOS
        pyautogui.keyDown('command')
        pyautogui.press('tab')
        pyautogui.keyUp('command')
    # print("switch window")


def prevent_sleep():
    """Prevent system sleep (Windows/Linux/macOS specific)."""
    system = platform.system()
    try:
        if system == "Windows":
            subprocess.run(
                "powercfg -change -standby-timeout-ac 0", shell=True)
        elif system == "Linux":
            subprocess.run(
                "gsettings set org.gnome.settings-daemon.plugins.power sleep-inactive-ac-type 'nothing'", shell=True)
        elif system == "Darwin":  # macOS
            subprocess.run("caffeinate -dims &", shell=True)
        print("prevent sleep")
    except Exception as e:
        print(f"{e}")


def prevent_idle():
    """Run idle prevention actions in a loop."""
    prevent_sleep()
    try:
        while True:
            actions = [move_mouse, switch_window, click_mouse,
                       switch_window, move_mouse, click_mouse]
            action = random.choice(actions)
            action()
            # Random interval between 1 to 2 minutes
            sleep_time = random.randint(10, 30)
            print(f"prevent idle \n")
            time.sleep(sleep_time)
    except KeyboardInterrupt:
        print("exit.")


prevent_idle()
