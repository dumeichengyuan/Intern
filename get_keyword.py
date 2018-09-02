#coding:utf-8
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
from textrank4zh import TextRank4Keyword
import gensim
from snownlp import SnowNLP


def get_keyword(tlist, desym = 0.6):
    text = u''
    for i in xrange(1, tlist.__len__()):
        text = text + unicode(str(i)) + u',' + tlist[i] + u'\n'

    tr4w = TextRank4Keyword(stop_words_file='./chinese_stopword.txt')  # 导入停止词

    #  使用词性过滤，文本小写，窗口为2
    tr4w.analyze(text=text, lower=True, window=2)
    """
    f = open('/Users/stille/Desktop/intern/keyword/temp.txt','w')
    f.truncate()  #  清空
    """
    model = gensim.models.KeyedVectors.load_word2vec_format("./baidubaike.bin", binary=True)
    keywordlist = []
    keyword = u''
    #   n个关键词每个的长度最小为1
    for item in tr4w.get_keywords(30, word_min_len=1):
        temp = SnowNLP(item.word).tags[0][1]
        if temp == u'n':
    #  or (temp == u'a'):
            mbuff = 0
            for i in xrange(0, keywordlist.__len__()):
                if keywordlist.__len__() != 0:
                    buff = model.similarity(keywordlist[i],item.word)
                    if buff > mbuff:
                        mbuff = buff
            if mbuff < desym:
                keywordlist.append(item.word)
                keyword = keyword + item.word + u',' + str(item.weight) + u'\n'
    return keyword