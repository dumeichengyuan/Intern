#coding=utf-8

#  处理中文
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def get_comment(collection1, collection2, name):
    #  选择一个品牌
    brand = collection2.find({"brand_name":name})

    #  搜索全部商品
    product_list = []
    for item1 in brand:
        product_id = item1["product_id"]
        product_list.append(product_id)

    #  搜索全部评论
    comment_list = []
    for i in xrange(0,product_list.__len__()):
        temp = []
        temp = collection1.find({"product_id":product_list[i]})
        for item in temp:
            comment_cnt = item["content"]
            #  print comment_cnt.decode('utf-8')
            comment_list.append(comment_cnt)

    return comment_list