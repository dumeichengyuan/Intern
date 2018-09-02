#coding:utf-8
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

from wordcloud import WordCloud
import matplotlib.pyplot as plt
import jieba

def wcloud(keyword):
    text_from_file_with_apath = keyword
    wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
    wl_space_split = " ".join(wordlist_after_jieba)
    my_wordcloud = WordCloud(font_path="./Fangsong.ttf").generate(wl_space_split)
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()