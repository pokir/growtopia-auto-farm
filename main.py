# Code inspired by https://www.youtube.com/watch?v=J3fatZ2OVIU

from dotenv import load_dotenv
import asyncio
import os
import win32api
import win32con
import win32gui


# Set environment variables from .env
load_dotenv()

# Constants
try:
    WALK_SECONDS_PER_BLOCK = float(os.environ['WALK_SECONDS_PER_BLOCK'])
    PUNCH_SECONDS_PER_BLOCK = float(os.environ['PUNCH_SECONDS_PER_BLOCK'])
except (KeyError, ValueError):
    print('It looks like you did not configure the .env file correctly. Please create the .env file and set all values (see README.md and example.env)')
    exit()

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


async def do_farming(hwnd):
    # Start farming in a game window forever

    while True:
        # Start both walking and punching at the same time, then wait for both
        # to stop (either the walking or punching could take longer)
        move_right_task = asyncio.create_task(
            press_key_in_window(hwnd, keys['d'], WALK_SECONDS_PER_BLOCK)
        )

        punch_task = asyncio.create_task(
            press_key_in_window(hwnd, keys['space'], PUNCH_SECONDS_PER_BLOCK)
        )

        # Wait for both the moving and punching to stop
        await asyncio.gather(move_right_task, punch_task)


async def main():
    windows = get_windows()

    # Get all windows named something containing 'growtopia'
    game_windows = list(filter(
        lambda window: 'growtopia' in get_window_name(window).lower(), windows
    ))

    farming_tasks = []

    # Start farming in every game window
    for game_window in game_windows:
        task = asyncio.create_task(do_farming(game_window))

        farming_tasks.append(task)

    # Wait for every farming task to finish (which is never)
    await asyncio.gather(*farming_tasks)


if __name__ == '__main__':
    asyncio.run(main())
