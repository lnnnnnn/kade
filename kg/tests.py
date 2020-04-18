from bson import json_util as jsonb

# from django.test import TestCase
#
# # Create your tests here.
# dict = {'Name': {'base':['a','b','c'],'file':['a','b','c']}, 'Name2': {'file':['a','b','c']}}
# set=dict['Name']
# set['file'].append('d')
# # dict.append(('name1','a'))
#
# print (set,dict['Name'],dict)
# # print(dict['Name2']['base'])
#
#
# spDict={}
# print('a' not in spDict)
# spDict={'天空之城（薛涛小说天空之城） 作者': {'file': [{'o': 'a'}, {'o': 'a1'}], 'base': [{'o': '<a>薛涛</a>'}]}, '天空之城（薛涛小说天空之城） 书名': {'file': [{'o': '天空之城4'}], 'base': [{'o': '<a>天空之城</a>'}]}}
# spDictStr=jsonb.dumps(spDict)
# print(spDictStr)

# listo=[[{'s':'世界人工智能大会','p':'会议地点','o':'中国上海西岸','slink':['世界人工智能大会','世界人工智能大会1']},{'s':'世界人工智能大会','p':'会议时间','o':'会议时间	2018年9月17日','slink':['世界人工智能大会','世界人工智能大会1']}]]
# listo[0][0]['slink'].append('世界人工智能大会2')
# print(listo[0][0]['slink'])
# print(list(listo))


import os
import configparser
cf = configparser.ConfigParser()

# cf.read("test.ini")
cf.read("db.ini")

#return all section
secs = cf.sections()
print ('sections:', secs, type(secs))