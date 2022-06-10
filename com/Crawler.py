import requests
from bs4 import BeautifulSoup
from com.Public import Public

class Crawler(Public):

    Titlelist = []

    def gethtml(self,url):
        r = requests.get(url)
        r.encoding = "utf-8"
        return BeautifulSoup(r.text, "html.parser")

    def geturl(self,url):
        soup = self.gethtml(url)
        urllist = []
        for link in soup.find_all('a'):
            geturl = str(link.get('href'))
            if "htm" in geturl:
                if "http://www.gov.cn/" not in geturl:
                    urllist.append("http://www.gov.cn/" + geturl)
                else:
                    urllist.append(geturl)
        return urllist

    def gettitle(self,url):
        soup = self.gethtml(url)
        for link in soup.find_all('title'):
            title = link.text.split("_")[0]
            return title

    def gettext(self,url):
        soup = self.gethtml(url)
        text = []
        for link in soup.find_all('p'):
            text.append(link.text)
        return text

    def checktitle(self,title):
        titleflag = True
        for titled in self.Titlelist:
            if title == titled:
                titleflag = False
        return titleflag

    def writetext(self,text,title):
        if text:
            file = open(self.pathjoin(self.getpath(), 'doc', self.getfliename(title)), 'w', encoding='utf-8-sig')
            for t in text:
                file.write(t + "\n")
            file.close()

    def writedoc(self,url):
        urllist = self.geturl(url)
        for u in urllist:
            title = self.gettitle(u)
            if self.checktitle(title):
                self.Titlelist.append(title)
                self.writetext(self.gettext(u),title)