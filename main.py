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


def get_window_names():
    window_names = []

    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            window_names.append(win32gui.GetWindowText(hwnd))

    win32gui.EnumWindows(win_enum_handler, None)

    return window_names


def main():
    window_names = get_window_names()

    game_window_name = ''

    # Loop through all window names to find one containing the word Growtopia
    for window_name in window_names:
        if 'Growtopia' in window_name:
            game_window_name = window_name

    hwnd = win32gui.FindWindow(None, game_window_name)
    #win = win32ui.CreateWindowFromHandle(hwnd)

    # Focus the game window
    win32gui.SetForegroundWindow(hwnd)


if __name__ == '__main__':
    main()
