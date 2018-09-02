#coding=utf-8
#  处理中文
import sys


import gensim
# 导入模型
model = gensim.models.Word2Vec.load("/Users/stille/Desktop/intern/news_12g_baidubaike_20g_novel_90g_embedding_64.model")

print model[u'酸奶']
type(model[u'酸奶'])


"""
#coding=utf-8
#  处理中文
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import numpy as np
import pandas as pd
from snownlp import SnowNLP
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

s = u'可以，东西非常好，赞～ 派送神速，价格便宜，还是原来的味道！不错不错，性价比高，给力~~'
s = s.replace('\t', '')
s = s.replace(' ', '')

#  SnowNLP筛关键字
kn = 4
keyword = SnowNLP(s).keywords(kn)
#  for i in range(0,kn):
#          print keyword[i].encode('utf-8')

count = 0
obj = pd.Series(keyword)
df = pd.DataFrame(obj)
df.to_csv(path_or_buf='/Users/stille/Desktop/intern/keyword/' + str(count) + '.txt', encoding='utf-8')

"""
"""
index = brand_list.index(content.decode('utf-8'))#weight
text_from_file_with_apath = open('/Users/stille/Desktop/intern/wordcloud/texts/'+str(index)+'.txt').read()
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)
my_wordcloud = WordCloud(font_path="/Library/Fonts/Microsoft/Fangsong.ttf").generate(wl_space_split)
plt.imshow(my_wordcloud)
plt.axis("off")


from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.JD
collection1 = db.ahead_jd
collection2 = db.dynamic
collection3 = db.search_words
collection4 = db.statistic
# connect to database and collections

yogurt = collection4.find({"classify": "酸奶"})
tea = collection4.find({"classify": "茶叶"})
meat = collection4.find({"classify": "肉干"})
nut = collection4.find({"classify": "瓜子"})
milk = collection4.find({"classify": "牛奶"})
# 将statistic库按5大品类分开

yogurt_list = []
for item in yogurt:
        yogurt_id = item["product_id"]
        yogurt_list.append(yogurt_id)

tea_list = []
for item in tea:
        tea_id = item["product_id"]
        tea_list.append(tea_id)

meat_list = []
for item in meat:
        meat_id = item["product_id"]
        meat_list.append(meat_id)

nut_list = []
for item in nut:
        nut_id = item["product_id"]
        nut_list.append(nut_id)

milk_list = []
for item in milk:
        milk_id = item["product_id"]
        milk_list.append(milk_id)
# 对每个品类建立一个list,包含所有statistic库中该品类商品的商品id

goods = collection2.find()
# dynamic库(与statistic库唯一共同索引即为商品id)

yogurt_rank = []
tea_rank = []
meat_rank = []
nut_rank = []
milk_rank = []

for item in goods:
        if (item["product_id"] in yogurt_list):
                yogurt_rank.append(item)
        if (item["product_id"] in tea_list):
                tea_rank.append(item)
        if (item["product_id"] in meat_list):
                meat_rank.append(item)
        if (item["product_id"] in nut_list):
                nut_rank.append(item)
        if (item["product_id"] in milk_list):
                milk_rank.append(item)
# 对每个品类建立一个用于排行的list,在dynamic库中,将所有该品类商品的记录append到该品类的list中

yogurt_rank.sort(key=lambda item: item['comment_count'], reverse=True)
tea_rank.sort(key=lambda item: item['comment_count'], reverse=True)
meat_rank.sort(key=lambda item: item['comment_count'], reverse=True)
nut_rank.sort(key=lambda item: item['comment_count'], reverse=True)
milk_rank.sort(key=lambda item: item['comment_count'], reverse=True)
# 将所有ranking list按照comment_count进行降序排序

import pandas as pd

input = ["肉干", "瓜子", "酸奶","牛奶","茶叶"]
for content in input:
        if content == "酸奶":
                pd.DataFrame(yogurt_rank).to_csv(path_or_buf='/Users/stille/Desktop/intern/ranking/comment_count_ranking/yogurt_ranking.csv', encoding='utf_8_sig')
        if content == "茶叶":
                pd.DataFrame(tea_rank).to_csv(path_or_buf='/Users/stille/Desktop/intern/ranking/comment_count_ranking/tea_ranking.csv', encoding='utf_8_sig')
        if content == "肉干":
                pd.DataFrame(meat_rank).to_csv(path_or_buf='/Users/stille/Desktop/intern/ranking/comment_count_ranking/meat_ranking.csv', encoding='utf_8_sig')
        if content == "瓜子":
                pd.DataFrame(nut_rank).to_csv(path_or_buf='/Users/stille/Desktop/intern/ranking/comment_count_ranking/nut_ranking.csv', encoding='utf_8_sig')
        if content == "牛奶":
                pd.DataFrame(milk_rank).to_csv(path_or_buf='/Users/stille/Desktop/intern/ranking/comment_count_ranking/milk_ranking.csv', encoding='utf_8_sig')
# 根据自定义需求以csv形式输出required品类评论数排行榜



"""