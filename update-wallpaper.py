# update-wallpaper.py
# Scott Metoyer, 2013
import ctypes
import os
import textwrap
import json
import urllib2
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

FONT = "tahoma.ttf"
BOLD_FONT = "arialbd.ttf"
SPI_SETDESKWALLPAPER = 20 # According to http://support.microsoft.com/default.aspx?scid=97142

def get_quote(url):
    quote = json.load(urllib2.urlopen(url))
    return quote

def render_wallpaper(in_file, text, author, out_file, opacity=0.25):
    img = Image.open(in_file).convert("RGB")
    quote_image = Image.new('RGBA', img.size, (0,0,0,0))
    size = 2
    n_font = ImageFont.truetype(FONT, size)
    
    lines = textwrap.wrap(text, width = 40)    
    quote_width, quote_height = n_font.getsize(lines[0])
    
    # Scale the font size based on the length of a line of text
    while (quote_width + quote_height < quote_image.size[0]):
       size += 2
       n_font = ImageFont.truetype(FONT, size)
       quote_width, quote_height = n_font.getsize(lines[0])
    
    # Draw the quote
    draw = ImageDraw.Draw(quote_image, "RGBA")
    y_text = (quote_image.size[1] - (quote_height * len(lines))) / 2
    
    for line in lines:
        width, height = n_font.getsize(line)
        draw.text((0, y_text), line, font = n_font)
        y_text += height
    
    # Draw the author
    author_image = Image.new('RGBA', img.size, (0,0,0,0,))
    
    # Appropriately scale the author font
    if (size > 160):
        size = size / 4
    else:
        size = size / 2
        
    while (size % 2 != 0):
        size += 1
       
    n_bold = ImageFont.truetype(BOLD_FONT, size)
    author_width, author_height = n_bold.getsize(author)
    draw = ImageDraw.Draw(author_image, "RGBA")
    draw.text(((author_image.size[0] - author_width - size), (author_image.size[1] - author_height) / 2 + (quote_height * len(lines)) / 2 + 40), author, font = n_bold)
  
    # Adjust the opacity
    alpha = quote_image.split()[3]
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    quote_image.putalpha(alpha)
    
    # Render everything
    composite = Image.composite(quote_image, img, quote_image)
    Image.composite(author_image, composite, author_image).filter(ImageFilter.SMOOTH_MORE).save(out_file, "JPEG")

rendered_wallpaper = os.getcwd() + "/rendered.jpg"
quote = get_quote("http://127.0.0.1:1337")
render_wallpaper("wallpaper.jpg", quote["text"], quote["author"], rendered_wallpaper)
errorCode = ctypes.windll.user32.SystemParametersInfoA(SPI_SETDESKWALLPAPER, 0, rendered_wallpaper, 0) 

if errorCode == 0:
	print(ctypes.GetLastError())    