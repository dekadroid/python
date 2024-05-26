import random, argparse, os, time, random
try:
    import requests
    import urllib3
    from urllib3.exceptions import InsecureRequestWarning
except ModuleNotFoundError:
    os.system("cls" if os.name == "nt" else "clear")
    print("\33[32m[Requests] Installing module...\33[0m\n")
    pip.main(["install", "requests"])
    print("\33[33m[Requests] Module installed!\33[0m\n")
    import requests
    import urllib3
    from urllib3.exceptions import InsecureRequestWarning
    
from requests import Response

urllib3.disable_warnings(InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"

from colorama import Fore,Back,Style,init
os.system('clear')
print("""\33[96m
                   MY_@c3po4x
                 
    ▒█▀▀█ ▒█▀▀▀█ ▒█▀▀█ ▀▀█▀▀ ░█▀▀█ ▒█░░░        
    ▒█▄▄█ ▒█░░▒█ ▒█▄▄▀ ░▒█░░ ▒█▄▄█ ▒█░░░        
    ▒█░░░ ▒█▄▄▄█ ▒█░▒█ ░▒█░░ ▒█░▒█ ▒█▄▄█        

 ▒█▀▀█ ▒█░▒█ ▒█▀▀▀ ▒█▀▀█ ▒█░▄▀ ▒█▀▀▀ ▒█▀▀█       
 ▒█░░░ ▒█▀▀█ ▒█▀▀▀ ▒█░░░ ▒█▀▄░ ▒█▀▀▀ ▒█▄▄▀       
 ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█▄▄█ ▒█░▒█ ▒█▄▄▄ ▒█░▒█      \n
\33[0mAls Beispiel :\33[4m\33[1m\33[03mhttp://perfect-planet.net:8080\33[0m 
\33[0m        ohne :\33[91m\33[4m\33[1m/𝘊/\n""")
url = input("\33[0m\33[0mENTER PORTAL :\33[33m\33[1m ")
print("\n\33[0m") 
user_agents_list = [
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)',
    'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1',
    'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01',
    'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0'
    'Mozilla/5.0 (X11; U; Linux i686; en-GB; rv:1.7.6) Gecko/20050405 Epiphany/1.6.1 (Ubuntu) (Ubuntu package 1.0.2)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; Nautilus/1.0Final) Gecko/20020408',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:0.9.3) Gecko/20010801',
    #'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36'
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Mobile Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 13_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.5 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:109.0) Gecko/20100101 Firefox/119.0',
    'Mozilla/5.0 (Android 13; Mobile; rv:109.0) Gecko/119.0 Firefox/119.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 12_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 [ip:127.0.0.1:80]'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Mobile Safari/537.36 [ip:127.0.0.1:80]'
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 [ip:127.0.0.1:80]',
]

payload = [
'/portal.php',
'/server/load.php',
'/stalker_portal/server/load.php',
'/c/portal.php',
'/c/server/load.php',
'/magaccess/portal.php',
'/portalcc.php',
'/bs.mag.portal.php',
'/magportal/portal.php',
'/maglove/portal.php',
'/tek/server/load.php', 
'/emu/server/load.php',
'/emu2/server/load.php',
'/ghandi_portal/server/load.php', 
'/magLoad.php',
'/ministra/portal.php',
'/ministra/portal.php',
'/portalstb/portal.php',
'/xx/portal.php', 
'/portalmega.php',
'/portalmega/portal.php',
'/rmxportal/portal.php', 
'/portalmega/portalmega.php',
'/powerfull/portal.php',
'/korisnici/server/load.php', 
'/nettvmag/portal.php', 
'/cmdforex/portal.php',
'/tek/server/load.php',
'/emu/server/load.php',
'/emu2/server/load.php',
'/k/portal.php',
'/p/portal.php',
'/cp/server/load.php',
'/extraportal.php',
'/Link_Ok/portal.php',
'/delko/portal.php',
'/delko/server/load.php',
'/bStream/portal.php',
'/bStream/server/load.php',
'/blowportal/portal.php',
'/client/portal.php', 
'/server/move.php',]
def searchpanel():
			for admin in payload:
				getrequest = requests.get(url + admin, headers={'User-Agent': random.choice(user_agents_list)})
				statuscode = str(getrequest.status_code)
				if statuscode == "200":
					print(  Fore.GREEN + " 【 𝟐𝟎𝟎 】\33[0m"+Fore.WHITE+admin)
				if statuscode == "401":
					print(  Fore.GREEN + " 【 𝟒𝟎𝟏 】\33[0m"+Fore.WHITE+admin)
				elif statuscode == "403":
					print(  Fore.RED + " 【 𝟰𝟬𝟯 】\33[0m"+Fore.WHITE+admin)
				if statuscode == "512":
					print(  Fore.GREEN + " 【 𝟓𝟏𝟐 】\33[0m"+Fore.WHITE+admin)
				elif statuscode == "520":
					print(  Fore.RED + " 【 𝟱𝟮𝟬 】\33[0m"+Fore.WHITE+admin)
				elif statuscode == "404":
					print(  Fore.BLUE + " 【 𝟰𝟬𝟰 】\33[0m"+Fore.WHITE+admin)
				elif statuscode == "302":
					print(  Fore.YELLOW + " 【 𝟯𝟬𝟮】\33[0m"+Fore.WHITE+admin)
searchpanel()
