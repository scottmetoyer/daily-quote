daily-quote
===========

Scott Metoyer
scott.metoyer@gmail.com
01/21/2013

Simple python script that updates wallpaper with a random quote each time it's run. Also includes a quote server written in node.js that feeds up random quotes.

Usage:

Start the quote server by running

    node quoteserver.js
    
Run the wallpaper script by running

    update-wallpaper.py
    
The background wallpaper is wallpaper.jpg. Feel free to replace this with whatever you like (but make sure it's named wallpaper.jpg).

You need node.js, python 2.7, and PIL 1.1.7. Everything was written and tested only on Windows.