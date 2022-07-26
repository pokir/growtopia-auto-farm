from time import sleep
import win32gui


def list_window_names():
    def win_enum_handler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')

    win32gui.EnumWindows(, None)


if __name__ == '__main__':
    list_window_names()
