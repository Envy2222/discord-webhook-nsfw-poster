from doctest import NORMALIZE_WHITESPACE
import dhooks
from dhooks import Webhook,Embed
import requests
import time

neh = input("Webhook url for posting pfps : ")
hook = Webhook(neh)

def send_nsfw():
    while True:
        r = requests.get("http://api.nekos.fun:8080/api/hentai")
        res = r.json()
        print ("Sending hentoi")
        hook.send(res['image'])
        
        time.sleep(10)
        repr = requests.get("http://api.nekos.fun:8080/api/4k")
        rese = repr.json()
        print ("Sending 4k")
        hook.send(rese['image'])
        
        time.sleep(10)
        sax = requests.get("http://api.nekos.fun:8080/api/pussy")
        saxy = sax.json()
        print("Sending pussy")
        hook.send(saxy['image'])
        
        time.sleep(10)
        nvm = requests.get("http://api.nekos.fun:8080/api/boobs")
        saxnvm = nvm.json()
        hook.send(saxnvm['image'])
       
        time.sleep(10)
    
send_nsfw()
