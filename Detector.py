import requests
import time
import smtplib, ssl
import sys
from bs4 import BeautifulSoup

'''
    Bot name: NMPA
        -code assembled by Nate Slagter
        '''
def main() :
    
    def sendEmail(details, key):
        port = 587  # For starttls
        smtp_server = 'smtp.gmail.com'
        sender_email = 'enter email here'
        receiver_email = 'enter email here'
        password = 'app password here'
        message = key + ' Restock!\n' + str(details)
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
            
    def searchFunko(details,key):
        url = details[0]
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
        if (details[1] == 'Funko'):
            response = requests.get(url, headers=headers)
            OGsoup = BeautifulSoup(response.text,'lxml')
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, "lxml")
            if soup == OGsoup:
                time.sleep(3)
            else:
                sendEmail(details,key)
        elif (details[1] == 'Hot Topic'):
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text,'lxml')
            soupString = soup.get_text()
            if soupString.count('Out of Stock') == 1:
                time.sleep(3)
            else:
                sendEmail(details,key)
        elif (details[1] == 'Gamestop') :
            response = requests.get(url,headers=headers)
            soup = BeautifulSoup(response.text,'lxml')
            soupString = soup.get_text()
            if soupString.count('Out of Stock') == 1:
                time.sleep(3)
            else:
                sendEmail(details,key)
            
        else:
            print('ERROR : NO FUNKO WITH THAT NAME FOUND')
    funko = {
                'Madara Uchiha' : ('https://www.gamestop.com/toys-collectibles/funko/pop/products/pop-animation-naruto-shippuden-madara-reanimation-only-at-gamestop/11095723.html','Gamestop'),
                'Glow Kurama' : ('https://www.gamestop.com/toys-collectibles/funko/pop/products/pop-animation-naruto-shippuden-kurama-glow-in-the-dark-6-inch-only-at-gamestop/10127756.html','Gamestop')
                }
    funkoList = list(funko.keys())
    while True:
        for key in funkoList:
            searchFunko(funko.get(key),key)
main()
