import jieba
from wordcloud import WordCloud
from com.Public import Public

class Word(Public):

    def getfont_path(self):
        return  self.pathjoin(self.getpath(), "lib", 'simhei.ttf')

    def getstop_list(self):
        # stopword
        stoppath = self.pathjoin(self.getpath(), "lib", 'stopwords.txt')

        # 读入 stopword
        with open(stoppath, 'r', encoding='utf-8-sig') as stopflie:
            stop_text = stopflie.read()
            return stop_text.splitlines()

    def wordstr(self,filename):

        # 读入文本内容
        text = open(self.pathjoin(self.getpath(), 'doc', filename), 'r', encoding='utf-8-sig').read()

        # 中文分词
        list = jieba.cut(text, cut_all=False)

        # 把文本中的stopword剃掉
        word_list = []

        for word in list:
            if len(word.strip()) > 1 and not (word.strip() in self.getstop_list()):
                word_list.append(word)

        return  ' '.join(word_list)

    def build_wordcloud(self,docname):

        # 生成词云
        wc = WordCloud(
            font_path=self.getfont_path(),
            background_color="white",
            random_state=42,
            width=1000,
            height=860,
        )
        wc.generate(self.wordstr(self.getfliename(docname)))

        # 生成图片
        wc.to_file('./pic/{}.png'.format(docname))