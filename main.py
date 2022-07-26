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

    game_window_name = ''

    # Find a window name containing 'Growtopia'
    for window in windows:
        window_name = get_window_name(window)

        if 'growtopia' in window_name.lower():
            game_window_name = window_name

    hwnd = win32gui.FindWindow(None, game_window_name)
    #win = win32ui.CreateWindowFromHandle(hwnd)

    # Print the actual name of the window
    print('The actual name of the window is:', repr(game_window_name))

    # Focus the game window
    win32gui.SetForegroundWindow(hwnd)


if __name__ == '__main__':
    main()
