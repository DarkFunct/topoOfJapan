#-*- coding:utf-8 -*-
import pymongo
client = pymongo.MongoClient()
col_edge_degree = client['itdkall_info']['merge']#边
col_node = client['itdkall_info']['index_node']
col_node.drop()
i=0
for edge in col_edge_degree.find():
    q = {'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']}
    flag = col_node.find_one(q)
    if not flag:
        docu = {'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude'],'index':i}
        col_node.insert_one(docu)
        i+=1

    q = {'longitude':edge['end']['longitude'],'latitude':edge['end']['latitude']}
    flag = col_node.find_one(q)
    if not flag:
        docu = {'longitude':edge['end']['longitude'],'latitude':edge['end']['latitude'],'index':i}
        col_node.insert_one(docu)
        i+=1
with open("japen.txt",'w')as f:
    s = "node:"+str(col_node.count())+"edge:"+str(col_edge_degree.count())+"\n"
    f.write(s)
    for edge in col_edge_degree.find():
        s=''
        q = {'longitude':edge['start']['longitude'],'latitude':edge['start']['latitude']}
        flag = col_node.find_one(q)
        s = s+str(flag['index'])+'\t'
        q = {'longitude':edge['end']['longitude'],'latitude':edge['end']['latitude']}
        flag = col_node.find_one(q)
        s=s+str(flag['index'])+'\n'
        f.write(s)