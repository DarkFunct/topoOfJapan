#-*- coding:utf-8 -*-
import pymongo
client = pymongo.MongoClient()
db_list=['Tokyo_left_logistic','Tokyo_leftdown_logistic','Tokyo_logistic','Tokyo_right_logistic','Tokyo_top_logistic',
         'Tokyo_top_straight_logistic','binsong','changqi','changye','chongsheng','chongsheng上','chuyun','dafen','dedao','fudao','gangshan',
         'gaosong','gaozhi','gongqi','guangdao','jinggang','jinze','jinze_left','jinze_right','luerdao','qiutian','shankou','wuqu',
         'xiantai','xinwu','xiongben','yanshou']
num=0
for db in db_list:
    col = client[db]['map_logi2loca']
    print(col.name)
    for node in col.find():
        if node['in']:
            num+=1
print(num)
