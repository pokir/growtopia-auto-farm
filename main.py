from time import sleep
import win32gui
import win32ui

try:
    import win32api
except:
    print('No win32api :(')

try:
    import win32con
except:
    print('No win32con :(')


def get_windows():
    windows = []

    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            windows.append(hwnd)

    win32gui.EnumWindows(win_enum_handler, None)

    return windows


def get_window_name(hwnd):
    return win32gui.GetWindowText(hwnd)


def main():
    windows = get_windows()

    # Get all windows named something containing 'Growtopia'
    game_windows = list(filter(
        lambda window: 'growtopia' in get_window_name(window).lower(), windows
    ))

    #win = win32ui.CreateWindowFromHandle(hwnd)

    # Loop through focusing each growtopia window 20 times
    for _ in range(20):
        for game_window in game_windows:
            sleep(0.05)
            win32gui.SetForegroundWindow(game_window)


if __name__ == '__main__':
    main()
