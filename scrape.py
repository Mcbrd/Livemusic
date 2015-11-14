from bs4 import BeautifulSoup
import requests
import io
class Website:
    def __init__(self, site):
        self.site = site
        self.r = requests.get(self.site)
        self.soup = BeautifulSoup(self.r.content,'html.parser')
        self.band = self.soup.find_all("div",{'class':"playbox-title"})
        self.time = self.soup.find_all("div",{'class':"playbox-time"})

    def webScraper(self):      
        self.soup 

    def parser(self):
        band = self.soup.find_all("div",{'class':"playbox-title"})
        time = self.soup.find_all("div",{'class':"playbox-time"})                
        self.soup       
        self.band 
        self.time 
        for b, t in zip(band, time):            
            print(b.text,t.text)

    def writer(self):
        band = self.soup.find_all("div",{'class':"playbox-title"})
        time = self.soup.find_all("div",{'class':"playbox-time"})
        self.r
        self.soup 
        self.band 
        self.time
        fo = open("letter.txt", "w")
        for b, t in zip(band, time):           
            fo.write(b.text+' '+str(t.text)+'\n')
        fo.close()
       
Shank = Website("http://www.shankhall.com")

Shank.webScraper()
Shank.parser()
Shank.writer()