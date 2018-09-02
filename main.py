#coding=utf-8
#  处理中文
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass

from pymongo import MongoClient


from get_comment import *
from get_commentc import *
from get_keyword import *
from div_gb import *
from wcloud import *

def main():
    client = MongoClient('localhost', 27017)
    #  client = Connection('localhost', 27017).performance_test
    collection1 = client.JD.ncomment  # 评论数据库
    collection2 = client.JD.nstatistic  #  商品数据库

    comment_list = get_commentc(collection1, collection2 , u'茶叶')
    #  comment_list = get_comment(collection1, collection2, u'慧虎')

    nlist = list(set(comment_list))

    tlist = get_goodlist(nlist, 0.2)

    keyword = get_keyword(tlist, 0.6)

    print keyword

    wcloud(keyword)


main()
