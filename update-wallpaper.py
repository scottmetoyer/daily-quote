# update-wallpaper.py
# Scott Metoyer, 2013
import ctypes
import os 
SPI_SETDESKWALLPAPER = 20 # According to http://support.microsoft.com/default.aspx?scid=97142
path = os.getcwd() + "/image.bmp"
errorCode = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, path, 0) 

if errorCode == 0:
	print(ctypes.GetLastError())
else:
	print("Wallpaper set.")
