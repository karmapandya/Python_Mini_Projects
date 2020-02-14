import time
import webbrowser

## this program open link every specified interval.





def OpenBrowser(link):
    if type(link) is not str:
        raise TypeError("Argument needs to be a string.")
    webbrowser.open(link, new=2)

while True:
    time.sleep(3) # wait 3 seconds
    #time.sleep(60*60*2) # wait 2 hours --- Replace seconds or your time here.
    OpenBrowser('https://www.youtube.com/watch?v=dQw4w9WgXcQ') # Replace link here.


