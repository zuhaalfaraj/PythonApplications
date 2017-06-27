import time
from datetime import datetime as dt
hostsTemp = r"C:\Programs\Python 3.6.1\Codes\Websites_blocker\hosts"
hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"
websites = ['www.twitter.com', 'twitter.com', 'www.facebook.com', 'facebook.com']

while (True) :
    if dt (dt.now().year , dt.now().month , dt.now().day , 2) < dt.now() < dt (dt.now().year , dt.now().month , dt.now().day ,6):
        print ("Working Time...")
        with open (hostsTemp , 'r+') as file :
            contant = file.read ()
            for wb in websites :
                if wb in contant :
                    pass
                else :
                    file.write (redirect+"  "+wb + "\n")

    else :
        with open (hostsTemp  , 'r+') as file :
            contain = file.readlines()
            file.seek(0)

            for line in contain :
                if not any (wb in line for wb in websites ) :
                    file.write (line)
            file.truncate()

        print ("Funny Time :D ")


    time.sleep(5)
