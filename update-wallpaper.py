# update-wallpaper.py
# Scott Metoyer, 2013
import ctypes
import os 
from PIL import Image, ImageDraw, ImageFont, ImageEnhance

FONT = "Arial.ttf"
SPI_SETDESKWALLPAPER = 20 # According to http://support.microsoft.com/default.aspx?scid=97142
SPI_GETDESKWALLPAPER = 115
path = os.getcwd() + "/image.bmp"

def add_quote(in_file, text, out_file, opacity=0.25):
    img = Image.open(in_file).convert("RGB")
    quote_image = Image.new('RGBA', img.size, (0,0,0,0))
    size = 2
    n_font = ImageFont.truetype(FONT, size)
    n_width, n_height = n_font.getsize(text)
    while (n_width+n_height < quote_image.size[0]):
       size += 2
       n_font = ImageFont.truetype(FONT, size)
       n_width, n_height = n_font.getsize(text)
    draw = ImageDraw.Draw(quote_image, "RGBA")
    draw.text(((quote_image.size[0]-n_width)/2,(quote_image.size[1]-n_height)/2), text, font=n_font)
    alpha = quote_image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    quote_image.putalpha(alpha)
    Image.composite(quote_image, img, quote_image).save(out_file, "JPEG")

# Grab the current wallpaper
wallpaper = ctypes.c_buffer("\000" * 256)
ctypes.windll.user32.SystemParametersInfoA(SPI_GETDESKWALLPAPER, len(wallpaper), ctypes.byref(wallpaper), 0)

# Add the quote image overlay
add_quote("wallpaper.jpg", "This is test", wallpaper.value)

# Reset the wallpaper
errorCode = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, wallpaper, 0) 

if errorCode == 0:
	print(ctypes.GetLastError())
else:
	print("Wallpaper set.")
    