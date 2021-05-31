import requests
from bs4 import BeautifulSoup
import re
import subprocess
import sys

def app() :
    try:
        print ("*********************************\n")
        print ('your list url:', (sys.argv)[1])
        print ("\n*********************************\n")
    except:
        print ("Please enter your playlist URL :)")
        print ("\n*********************************\n")
        return 0


    URL = (sys.argv)[1]

    req = requests.get(URL)

    soup = BeautifulSoup(req.content, 'html5lib')

    links=[]

    for link in soup.find_all('a', href=True):
        a = link['href']
        if re.search("/v/\w+", a) :
            a = a[:8]
            
            links.append(a)

    links = list(dict.fromkeys(links))

    for link in links :
        link = "https://www.aparat.com" + link


        command = subprocess.run(['youtube-dl', link], capture_output=True)

        sys.stdout.buffer.write(command.stdout)
        sys.stderr.buffer.write(command.stderr)
        print("\n*****************************")

if __name__ == '__main__':
    app()