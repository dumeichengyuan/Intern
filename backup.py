#coding=utf-8
#  处理中文
import codecs
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

from pymongo import MongoClient
from textrank4zh import TextRank4Keyword, TextRank4Sentence
from wordcloud import WordCloud
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import jieba.posseg
"""
client = MongoClient('localhost', 27017)
collection1 = client.JD.comment  # 评论数据库
collection2 = client.JD.statistic  #  商品数据库

f = open("/Users/stille/Desktop/intern/comment.txt","w")

#  搜索全部评论
comment_list = []
for item in collection1.find():
    comment_id = item["content"]
    comment_list.append(comment_id)
    f.write(comment_id)
    f.write("\r\n")

f.close()
"""
#  textrank筛关键字（可根据需求设置停止词）
text = codecs.open('/Users/stille/Desktop/intern/comment.txt','r', 'utf-8').read()
tr4w = TextRank4Keyword(stop_words_file='/Users/stille/Desktop/intern/chinese_stopword.txt')  # 导入停止词

#  使用词性过滤，文本小写，窗口为2
tr4w.analyze(text=text, lower=True, window=2)

keyword = []
wlist = []
#  4个关键词每个的长度最小为1
for item in tr4w.get_keywords(10, word_min_len=1):
    keyword.append(item.word)
    wlist.append(item.weight)

obj = pd.Series(keyword)
df = pd.DataFrame(obj)
df.to_csv(path_or_buf='/Users/stille/Desktop/intern/keyword/temp.txt', encoding='utf-8')

index = wlist  #  weight
text_from_file_with_apath = open('/Users/stille/Desktop/intern/keyword/temp.txt').read()
#  seg = jieba.posseg.cut(text_from_file_with_apath)
wordlist_after_jieba = jieba.cut(text_from_file_with_apath)

'''
wordlist = ''
for i in seg:
    if i.flag == 'n' || i.flag == 'a'
        wordlist = wordlist + i.word + u',' + str(item.weight*100) + u'\n'


'''

wl_space_split = " ".join(wordlist_after_jieba)
my_wordcloud = WordCloud(font_path="/Library/Fonts/Microsoft/Fangsong.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()



"""
*****************
#  选择一个品牌
brand = collection2.find({"brand_name":"得益"})

#  搜索全部商品
product_list = []
for item in brand:
    product_id = item["product_id"]
    product_list.append(product_id)

#  搜索全部评论
comment_list = []
for i in range(1,product_list.__len__()):
    temp = []
    temp = collection1.find({"product_id":product_list[i]})
    for item in temp:
        comment_cnt = item["content"]
        comment_list.append(comment_cnt)

*******************************
备份：
#coding=utf-8
#  处理中文
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from pymongo import MongoClient
from snownlp import SnowNLP
import numpy as np
import matplotlib.pyplot as plt

client = MongoClient('localhost', 27017)
collection1 = client.JD.comment  # 评论数据库
collection2 = client.JD.statistic  #  商品数据库

#  搜索全部评论
comment_list = []
for item in collection1.find():
    comment_id = item["content"]
    comment_list.append(comment_id)

#  全部星级评论
score_list = []
for item in collection1.find():
    score_id = item["score"]
    score_list.append(score_id)

num = comment_list.__len__()
x = np.arange(1, 1000)
s1 = []
s2 = []
for i in x:
    #  情感评分
    s1.append(SnowNLP(unicode(str(comment_list[i]))).sentiments)
    #  星级评分
    s2.append((score_list[i]-1)/4)

plt.figure(1)
plt.plot(x, s1,'.')
plt.hold(True)

plt.plot(x, s2,'.')
plt.show()

"""