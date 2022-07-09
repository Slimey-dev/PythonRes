import pystray
import pywintypes
import win32api
import win32con
from PIL import Image
from pystray import MenuItem as item


def on_set_resolution(width: int, height:int):
    devmode = pywintypes.DEVMODEType()
    devmode.PelsWidth = width
    devmode.PelsHeight = height

    devmode.Fields = win32con.DM_PELSWIDTH | win32con.DM_PELSHEIGHT

    win32api.ChangeDisplaySettings(devmode, 0)


def on_quit():
    icon.visible = False
    icon.stop()


if __name__ == "__main__":
    image = Image.open("icon.png")

    menu = (
        item('1080p', lambda: on_set_resolution(1920, 1080)), 
        item('900p', lambda: on_set_resolution(1440, 900)),
        item('Quit', on_quit)
        )

    icon = pystray.Icon("ResChange", image, "ResChange", menu)
    icon.run()