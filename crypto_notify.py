import os
import time
import requests
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

while True :
    # requests json data and read it
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    r.json()
    resp = r.json()

    #parsing json and show usd currency
    price = resp["bpi"]["USD"]["rate_float"]
    time.sleep(10)
    top = 4500

    if price > top :
        print price
	#play mp3 
	os.system("mpg123 ding.mp3")
    # One time initialization of libnotify
        Notify.init("Crypto Notify")

        # Create the notification object
        summary = "Crypto Alert!"
        body = "BTC : $ %s" % (price)
        notification = Notify.Notification.new(summary,body)

        # Actually show on screen
        notification.show()

    else:
        r =requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        print price
        time.sleep(10)
