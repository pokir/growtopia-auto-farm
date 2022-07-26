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


def list_window_names():
    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')

    win32gui.EnumWindows(win_enum_handler, None)


def main():
    list_window_names()
    
    window_name = 'Growtopia'

    hwnd = win32gui.FindWindow(None, window_name)
    print(hwnd)
    #win = win32ui.CreateWindowFromHandle(hwnd)

    # focus the game window
    win32gui.SetForegroundWindow(hwnd)


if __name__ == '__main__':
    main()
