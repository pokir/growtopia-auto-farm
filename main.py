# Code inspired by https://www.youtube.com/watch?v=J3fatZ2OVIU

from time import sleep
import win32api
import win32con
import win32gui
import win32ui


# http://www.kbdedit.com/manual/low_level_vk_list.html
keys = {
    'w': 0x57,
    'a': 0x41,
    's': 0x53,
    'd': 0x44,
    'space': 0x20,
}


def get_windows():
    windows = []

    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(win_enum_handler, None)

    return windows


def get_window_name(hwnd):
    return win32gui.GetWindowText(hwnd)


def press_key_in_window(hwnd, key, seconds):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    sleep(seconds)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


def main():
    windows = get_windows()

    # Get all windows named something containing 'Growtopia'
    game_windows = list(filter(
        lambda window: 'growtopia' in get_window_name(window).lower(), windows
    ))

    #win = win32ui.CreateWindowFromHandle(hwnd)

    # Loop through focusing each growtopia window 20 times
    # TODO: it focuses one window and then fails on every other iteration
    for _ in range(3):
        for game_window in game_windows:
            win32gui.SetForegroundWindow(game_window)

            press_key_in_window(game_window, keys['w'], 0.3)

            sleep(0.5)


if __name__ == '__main__':
    main()
