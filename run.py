from com import WordCloud
from com import Crawler

url = "http://www.gov.cn/xinwen/yaowen.htm"

if __name__ == '__main__':

    wordcloud = WordCloud.Word()
    crawler = Crawler.Crawler()

    crawler.writedoc(url)

    for title in crawler.Titlelist:
        wordcloud.build_wordcloud(title)