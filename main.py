# Code inspired by https://www.youtube.com/watch?v=J3fatZ2OVIU

#from time import sleep
import asyncio
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
    # Return all visible windows

    windows = []

    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(win_enum_handler, None)

    return windows


def get_window_name(hwnd):
    # Get the name of a window object

    return win32gui.GetWindowText(hwnd)


async def press_key_in_window(hwnd, key, seconds):
    # Press a key in a window

    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    await asyncio.sleep(seconds)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)


async def main():
    windows = get_windows()

    # Get all windows named something containing 'growtopia'
    game_windows = list(filter(
        lambda window: 'growtopia' in get_window_name(window).lower(), windows
    ))

    # Walk to the right in every game window
    for game_window in game_windows:
        asyncio.create_task(press_key_in_window(game_window, keys['d'], 10))


if __name__ == '__main__':
    asyncio.run(main())
