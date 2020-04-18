# encoding='utf-8'
# _*_ coding:utf-8 _*_
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
# from pymongo import MongoClient
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt, csrf_protect  # Add this
from bson.objectid import ObjectId
import json
from bson import json_util as jsonb
import datetime
import os
import configparser
import re
import hashlib
from datetime import datetime

import kg.api as api
args = api.args

TRIPLE_ARG = args.TRIPLE_ARG
MENT2ENT_ARG = args.MENT2ENT_ARG
ENTITY_ARG = args.ENTITY_ARG
HAS_MENT2ENT = MENT2ENT_ARG is not None
SCHEMA_COL=args.SCHEMA_COL


#获取配置文件中的数据库配置信息
dbConfigFile="kg/db.ini"
cf = configparser.ConfigParser()
cf.read(dbConfigFile)

# DB_ARG=args.DB_ARG
# DB_NAME=DB_ARG['db_name']
# DB_HOST=DB_ARG['db_host']
# DB_PORT=DB_ARG['db_port']
# DB_USERNAME=DB_ARG['db_username']
# DB_PASSWORD=DB_ARG['db_password']

DB_NAME=cf['db']['DB_NAME']
DB_HOST=cf['db']['DB_HOST']
DB_PORT=cf['db']['DB_PORT']
DB_USERNAME=cf['db']['DB_USERNAME']
DB_PASSWORD=cf['db']['DB_PASSWORD']
# 获取配置文件中的表名、字段名


userTableName = args.TABLENAME_ARG['usertablename']
nodesTableName =args.TABLENAME_ARG['nodestablename']
edgesTableName = args.TABLENAME_ARG['edgestablename']


user_username = args.USER_ARG['user_username']
user_password = args.USER_ARG['user_password']


TRIPLE_COL = args.TRIPLE_COL
if HAS_MENT2ENT: MENT2ENT_COL = args.MENT2ENT_COL

#nodes_node=ENTITY_ARG['entity_name']
NODE_NAME = ENTITY_ARG['entity_name']
#
# userTable = db[userTableName]
# edgesTable = db[edgesTableName]
# nodesTable = db[nodesTableName]



###################      读取db.ini中的内容 用于展示可视化+ 配置     ######################################
# DB_NAME=cf['db']['DB_NAME']
# DB_HOST=cf['db']['DB_HOST']
# DB_PORT=cf['db']['DB_PORT']
# DB_USERNAME=cf['db']['DB_USERNAME']
# DB_PASSWORD=cf['db']['DB_PASSWORD']

# tableName
# userTableName = cf['tableName']['userTableName']
# nodesTableName = cf['tableName']['nodesTableName']
# edgesTableName = cf['tableName']['edgesTableName']

# [user]
# user_username = cf['user']['user_username']
# user_password = cf['user']['user_password']

# [edges]#
# edges_u = cf['edges']['edges_u']
# edges_u_isnode = cf['edges']['edges_u_isnode']
# edges_u_sort = cf['edges']['edges_u_sort']
# edges_v = cf['edges']['edges_v']
# edges_v_isnode = cf['edges']['edges_v_isnode']
# edges_v_sort = cf['edges']['edges_v_sort']
# edges_w = cf['edges']['edges_w']
# edges_w_isnode = cf['edges']['edges_w_isnode']
# edges_w_sort = cf['edges']['edges_w_sort']
# edges_tp = cf['edges']['edges_tp']
# edges_tp_isnode = cf['edges']['edges_tp_isnode']
# edges_tp_sort = cf['edges']['edges_tp_sort']
# edges_timestamp = cf['edges']['edges_timestamp']
# edges_editable = cf['edges']['edges_editable']



################################################################



nodes_editable=True
edges_editable=True
# This skips csrf validation. Use csrf_protect to have validation
def index(request):

    ets=[]
    if nodes_editable:
        ets.append('nodes')
    if edges_editable:
        ets.append('edges')
    
    return render(request, "kg/index.html",{"ets":ets})

def visindex(request):
    return render(request, "kg/visindex.html")

def temp(request):
    return render(request, "kg/temp.html")


def settings(request):




    server={'DB_NAME':DB_NAME,'DB_HOST':DB_HOST,'DB_PORT':DB_PORT,'DB_USERNAME':DB_USERNAME,'DB_PASSWORD':DB_PASSWORD}
    # user={'userTableName':userTableName,'user_username':user_username,'user_password':user_password}
    # edges={'edgesTableName':edgesTableName,'edges_u':edges_u,'edges_v':edges_v,'edges_w':edges_w,'edges_tp':edges_tp,
    #          'edges_timestamp':edges_timestamp,'edges_editable':edges_editable}
    #
    # nodes={'nodesTableName':nodesTableName,'nodes_node':nodes_node,'nodes_timestamp':nodes_timestamp,'nodes_editable':nodes_editable}
    
    # print(148,server)
    # res={'server':server,'user':user,'edges':edges,'nodes':nodes}
    res = {'server': server}






    return render(request, "kg/settings.html",{'res':res})






def make_salt_md5(pwd):
    pwd = pwd + pwd[:-4]
    return hashlib.md5(pwd.encode()).hexdigest()

def get_user_token(user):
    return make_salt_md5(user+datetime.strftime(datetime.now(), '%m-%d')+'adfadf')
@csrf_exempt
def login(request):
    user = request.POST.get('user')
    pwd = request.POST.get('pwd')
    print(user, pwd)
    # cnt = userTable.find({user_username: user, user_password: pwd}).count()
    cnt=api.getUserCount(user,pwd)
    print(156,cnt)
    if cnt != 0:
        print(request.COOKIES)
        obj = redirect("/kg/index")
        obj.set_cookie("isLogin", True)
        #obj.set_cookie("username", user)
        obj.set_cookie("token", get_user_token(user))
        print(obj)
        return obj


    else:

        return render(request, 'kg/login.html')

def splitO(o):
    if o.find("href") != -1:
        ld = o.find("=\"")
        rd = o.find("\">")
        oe = o[ld + 2: rd]

        mld = o.find("\">")
        mrd = o.rfind("</a>")
        om = o[mld + 2: mrd]

        print(om,oe)
        return (om,oe)
    else:
        return o


def remove(request, nid):
    # edgesTable.delete_one({'_id': ObjectId(nid)})
    api.deleteEdgeById(nid)
    return HttpResponse("delete success")


def modify(request, id):
    # o = o.replace("*****", "/")  # 将/恢复
    # print('in mdify')
    params = request.GET.get('params')
    print(params)
    params = params.strip('\t').split('\t')
    print(params)
    #if len(params) != len(args.TRIPLE_COL): return HttpResponse("Not correct")

    num=api.getEdgeCount(params)

    if num != 0:
        return HttpResponse("already exist")

    api.updateEdge( id,params)
    return HttpResponse("modify success")

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

def validateEdge(params):
    # vp = params[args.TRIPLE_P]
    # print('vp:', vp)#
    # vo = params[args.TRIPLE_O]
    # print(vo,is_number(vo))
    schemas=api.getAllSchemas()
    for sc in schemas:
        number_flag = False
        condition_flag = False
        for col,param in zip(SCHEMA_COL,params):
            print(col,param)
            if sc[col] == 'String':
                continue
            elif sc[col] == "UnconNumber":
                if not is_number(param):
                    return False
            elif sc[col] == 'Number':
                number_flag=is_number(param)
            else:# eg.工号
                if param==sc[col]:
                    condition_flag=True

        if not condition_flag:
            return True
        else:
            return number_flag



        # if vp==sc[SCHEMA_ARG['p']] and sc[SCHEMA_ARG['o']].find('Number')!=-1 :
        #     if not is_number(vo):
        #         return False
    return True




def add(request):
    print('in add')
    params = request.GET.get('params')
    params = params.strip('\t').split('\t')
    #if len(params) != len(args.TRIPLE_COL): return HttpResponse("Not correct")

    # 没有href的o,无需验证是否在nodes表中
    # o = o.replace("*****", "/")  # 将/恢复
    print(params)
    num=api.getEdgeCount(params)
    if num != 0:
        return HttpResponse("already exist")

    #schema validate

    # edge[TRIPLE_COL[args.TRIPLE_S]]
    # if validateEdge(params):
    res = ""
    valid=validateEdge(params)
    if valid:
        api.addEdge(params)

        # 新增一个edges，如果s不存在，也需要加入到nodes表中



        # ind=-1
        # for field in TRIPLE_ARG:
        # #ind+=1
        for ind, field in enumerate(TRIPLE_COL):
            if TRIPLE_ARG[field]['node'] == 1:
                u = params[ind]
                print('add entity %s by edge %s' % (u, str(params)))
                cnt = api.getNodeCount(u)

                res = "add edge:" + str(params)
                # 如果entity表中无entity 在entity表中增加
                if cnt == 0:
                    # nodesTable.insert({nodes_node: u})
                    api.addNode(u)

                    res += "  and add entity:" + u

            elif TRIPLE_ARG[field]['node'] == 2:
                oe = params[ind + 1]
                # print(oe)
                if oe != "":
                    print('add entity %s by edge %s' % (oe, str(params)))
                    cnt = api.getNodeCount(oe)
                    if cnt == 0:
                        # nodesTable.insert({nodes_node: u})
                        api.addNode(oe)

                        res += "  and add entity:" + oe

    else :
        res="不符合Schema定义！"
    return HttpResponse(res)



def make_href(z):
    if not '</a>' in z: return z
    ret = []
    try:
        zs = z.split('</a>')
        for zz in zs:
            if not '<a' in zz:
                ret.append(zz)
                continue
            ment, ent = '', ''
            if '<a>' in zz: ment = zz.split('<a>')[-1]
            else:
                vv = re.search('<a href="(.+?)">(.+?)$', zz)
                ent, ment = vv.group(1), vv.group(2)
            href = ent if ent != '' else ment
            zt = zz.split('<a')[0]
            ret.append(zt + '<a tid="%s" onclick="query_entity(this.getAttribute(\'tid\'))">%s</a>'%(href, ment))
    except: return z
    return ''.join(ret)

def query_edge(request, s):
    print("query_edge" + s)
    if not edges_editable:
        return HttpResponse('non-editable')

    field = TRIPLE_ARG
    # post = api.getEdgesByU(s)
    # print(309,list(post))
    # print(s)
    # print(s == "")
    if s == "":
        nodes = api.getTopNodes(20)
        resEdge = []
        for node in nodes:
            node = node[NODE_NAME]
            resEdge.extend(api.getEdgesByU(node))
            if len(resEdge) > 100: break
        post = resEdge
    else:
        post=list(api.getEdgesByU(s))
    # print(318,list(post))

    o_name=args.TRIPLE_COL[args.TRIPLE_O]
    print(api.HAS_HREF)
    if not api.HAS_HREF:
        for x in post:
            if '<a' in x[o_name] and 'href' not  in x[o_name]: #仅仅显示长文本中的链接 包含实体的o依然分 om oe显示
                x[o_name] = make_href(x[o_name])
    # print(324,list(post))
    ret=[{'field':field,'jsons':list(post)}]
    jsonStr = json.dumps(list(ret), ensure_ascii=False)
    return HttpResponse(jsonStr)

## ___________________________________________________________________________________________

def query_ment2ent_by_entity(request, s):
    print("query_ment2ent_by_entity" + s)

    field=MENT2ENT_ARG

    if s=="":
        post=[]
        # nodes=nodesTable.find().limit(50)
        # nodes=list(api.getTopNodes(50))
        # print(304,nodes)
        # resNum=0
        # resEdgeStr=""
        # resEdge=[]
        # print(nodes[0])
        # node=nodes[0][nodes_node]
        # mes=api.getMent2entsByEntity(node)
        # print(mes)
        # # resEdgeStr=jsonb.dumps(list(mes))
        # # ret = {'field': field, 'jsons': resEdgeStr}
        # ret = {'field': field, 'jsons': list(mes)}
        # return HttpResponse(json.dumps(ret))


    post = list(api.getMent2entsByEntity(s))
    #print(295,post)
    post.extend(api.getMent2entsByMention(s))
    #print(post)
    ret={'field':field, 'jsons':list(post)}
    return HttpResponse(json.dumps(ret, ensure_ascii=False))
		
		
    #postStr = jsonb.dumps(list(post))
    #ret={'field':fieldStr,'jsons':postStr}
    # jsonStr = jsonb.dumps(list(post))
    #jsonStr=json.dumps(ret)
    #return HttpResponse(jsonStr)

def add_ment2ent(request, *params):

    num=api.getMent2entCount(params)
    if num != 0:
        return HttpResponse("already exist")

    api.addMent2ent(params)
    # 新增一个edges，如果s不存在，也需要加入到nodes表中

    
    res="success"
    for u,field in zip(params,MENT2ENT_COL):
        if MENT2ENT_ARG[field]['node']==1:
            #u=field
            cnt=api.getNodeCount(u)


            # 如果entity表中无entity 在entity表中增加
            if cnt == 0:
                # nodesTable.insert({nodes_node: u})
                api.addNode(u)

                res += "  and add entity:" + u


    return HttpResponse(res)


def modify_ment2ent(request,id,*params):
    num = api.getMent2entCount(params)
    # num = edgesTable.find({edges_u: u, edges_v: v, edges_w: w,edges_tp: tp}).count()

    if num != 0:
        return HttpResponse("already exist")

    api.updateMent2ent(id, params)
    return HttpResponse("success modify ")
def remove_ment2ent(request,nid):
    api.deleteMent2entById(nid)
    return HttpResponse("delete success")
# ___________________________________________________________________________________________
# 显示模糊查询的结果
def query_auto_entity(request, s):
    print("query_auto_entity" + s)

    if nodes_editable !=True:
        return HttpResponse('non-editable')

    resNodes=[]
    # posts = nodesTable


    if s=="":
       
        resNodes=api.getTopNodes(20)
    else:
        
        node_normal=api.getOneNode(s)
        # print(post)
        # print(node_normal)
        if node_normal != None:  # ?
            resNodes.append(node_normal)
            nid = node_normal['_id']
        else: nid = '####'
        if not HAS_MENT2ENT:
            nodes_blur = api.getBlurNodes(s)
            resNodes.extend( [node for node in nodes_blur if node['_id'] != nid] )
        # '/{0}/'.format(s) '/知识/'
        # nodes_blur = posts.find({nodes_node: {'$regex': s}})

    # jsonStr = jsonb.dumps(list(resNodes))

    #传入 是否有ment2ent表
    print()
    ret={'entity_name':NODE_NAME,'entities':list(resNodes),'has_ment2ent':HAS_MENT2ENT}
    retStr=json.dumps(ret,ensure_ascii=False)
    #print('in query auto entity:',retStr)


    return HttpResponse(retStr)




def remove_entity(request, id):#删除triple ment2ent中节点属性为1的记录
    print('in remove entity')
    # nodesTable.delete_one({nodes_node: nid})
    n = api.getOneNodeById(id)[NODE_NAME]
    # print(n)
    api.deleteNodeById(id)
    # print(376)
    # 删除nodes表中的 entity,会把其他表中所有的entity一起删除
    # edgesTable.delete_many({edges_u: nid})
    # edgesTable.delete_many({edges_v: nid})


    # api.deleteEdgesByU(nid)
    # api.deleteEdgesByV(nid)

    #for k in TRIPLE_ARG:
    #    print(k)
    #    if TRIPLE_ARG[k]['node'] == 1:
    #        print(k,n)
    #        api.deleteEdgesByNode(k,n)
	
    for k, v in TRIPLE_ARG.items():
        if v['node'] == 1: api.deleteEdgesByNode(k, n)
	
    
    #if MENT2ENT_ARG!=None:
    if HAS_MENT2ENT:
        for k, v in MENT2ENT_ARG.items():
            if v['node'] == 1: api.deleteMent2entByNode(k, n)

    return HttpResponse("delete success")


def add_entity(request, s):
    # num = nodesTable.find({nodes_node: s}).count()
    num=api.getNodeCount(s)
    if num != 0:
        return HttpResponse("already exist")

    # nodesTable.insert({nodes_node: s})
    api.addNode(s)
    return HttpResponse("add success")


# _______________ment2ent_____________________________________________________________________



#-------DB-settings----------------------------------------------------------------------
def saveDB_settings_server(request,db_name,db_host,db_port,db_username,db_password):
    cf.set("db", "DB_NAME", db_name)
    cf.set("db", "DB_HOST", db_host)
    cf.set("db", "DB_PORT", db_port)
    cf.set("db", "DB_USERNAME", db_username)
    cf.set("db", "DB_PASSWORD", db_password)

    cf.write(open(dbConfigFile, "r+"))


    res = 'saveDB_settings_server success'
    return HttpResponse(res)

'''
def saveDB_settings_user(request,_userTableName,_user_username,_user_password):
    res=''
    # print(db[userTableName].find().count())
    cnt=api.getAllUserCount()
    if cnt>0:
        res='用户表'+userTableName+'已存在，修改失败！'
        return HttpResponse(res)

    cf.set("tableName", "userTableName", _userTableName)
    cf.set("user", "user_username", _user_username)
    cf.set("user", "user_password", _user_password)
    cf.write(open(dbConfigFile, "r+"))
    res = 'saveDB_settings_user success'
    return HttpResponse(res)

def saveDB_settings_nodes(request,_nodesTableName,_nodes_editable,_nodes_node,_nodes_timestamp):
    if nodesTableName== _nodesTableName and  nodes_node==_nodes_node and nodes_timestamp==_nodes_timestamp:
       cf.set('nodes','nodes_editable',_nodes_editable)
       cf.write(open(dbConfigFile, "r+"))
       res = 'saveDB_settings_nodes success'
       return HttpResponse(res)
    else :
        cnt=api.getAllNodesCount()

        if cnt > 0:
            res = 'nodes表' + nodesTableName + '已存在，修改失败！'
            return HttpResponse(res)

        cf.set("tableName", "nodesTableName", _nodesTableName)
        cf.set("nodes", "nodes_editable", _nodes_editable)

        cf.set("nodes", "nodes_node", _nodes_node)
        cf.set("nodes", "nodes_timestamp", _nodes_timestamp)
        cf.write(open(dbConfigFile, "r+"))
        res = 'saveDB_settings_nodes success'
        return HttpResponse(res)

def saveDB_settings_edges(request,_edgesTableName,_edges_editable,_edges_u,_edges_v,_edges_w,_edges_tp,_edges_timestamp):
    if edgesTableName== _edgesTableName and edges_u==_edges_u and \
                     edges_v==_edges_v and edges_w==_edges_w and edges_tp==_edges_tp and edges_timestamp==_edges_timestamp :
       cf.set('edges','edges_editable',_edges_editable)
       cf.write(open(dbConfigFile, "r+"))
       res = 'saveDB_settings_edges success'
       return HttpResponse(res)
    else :
        if api.getAllEdgesCount() > 0:
            res = 'edges表' + edgesTableName + '已存在，修改失败！'
            return HttpResponse(res)

        cf.set("tableName", "edgesTableName", _edgesTableName)
        cf.set("edges", "edges_editable", _edges_editable)
        cf.set("edges", "edges_u", _edges_u)
        cf.set("edges", "edges_v", _edges_v)
        cf.set("edges", "edges_w", _edges_w)
        cf.set("edges", "edges_tp", _edges_tp)
        cf.set("edges", "edges_timestamp", _edges_timestamp)
        cf.write(open(dbConfigFile, "r+"))
        res = 'saveDB_settings_edges success'
        return HttpResponse(res)
    
'''
'''
def saveDB_settings_ment2ent(request,_ment2entTableName,_ment2ent_editable,_ment2ent_m,_ment2ent_e,_ment2ent_timestamp):
    if ment2entTableName== _ment2entTableName and ment2ent_m==_ment2ent_m and \
                     ment2ent_e==_ment2ent_e  and ment2ent_timestamp==_ment2ent_timestamp :
       cf.set('ment2ent','ment2ent_editable',_ment2ent_editable)
       cf.write(open(dbConfigFile, "r+"))
       res = 'saveDB_settings_ment2ent success'
       return HttpResponse(res)
    else :
        if db[ment2entTableName].find().count() > 0:
            res = '实体表' + ment2entTableName + '已存在，修改失败！'
            return HttpResponse(res)

        cf.set("tableName", "ment2entTableName", _ment2entTableName)
        cf.set("ment2ent", "ment2ent_editable", _ment2ent_editable)
        cf.set("ment2ent", "ment2ent_m", _ment2ent_m)
        cf.set("ment2ent", "ment2ent_e", _ment2ent_e)
        cf.set("ment2ent", "ment2ent_timestamp", _ment2ent_timestamp)
        cf.write(open(dbConfigFile, "r+"))
        res = 'saveDB_settings_ment2ent success'
        return HttpResponse(res)


def saveDB_settings_types(request,_typesTableName,_types_editable,_types_entity,_types_type,_types_timestamp):
    if typesTableName== _typesTableName and types_entity==_types_entity and \
                     types_type==_types_type  and types_timestamp==_types_timestamp :
       cf.set('types','types_editable',_types_editable)
       cf.write(open(dbConfigFile, "r+"))
       res = 'saveDB_settings_types success'
       return HttpResponse(res)
    else :
        if db[typesTableName].find().count() > 0:
            res = '实体表' + typesTableName + '已存在，修改失败！'
            return HttpResponse(res)

        cf.set("tableName", "typesTableName", _typesTableName)
        cf.set("types", "types_editable", _types_editable)
        cf.set("types", "types_entity", _types_entity)
        cf.set("types", "types_type", _types_type)
        cf.set("types", "types_timestamp", _types_timestamp)
        cf.write(open(dbConfigFile, "r+"))
        res = 'saveDB_settings_types success'
        return HttpResponse(res)

'''

# vis editor api##################################################################################################

def getEntitiesAdvice(request):
    def _T(x):
        if 'node' not in x: x['node'] = x[NODE_NAME]
        return x
    print('in advice')
    search=request.GET.get('search')
    print(search)
    # 匹配以xxx开头的值

	
    
    nodes=list(api.getNodesAdvice(search,5))
    nodes = [*map(_T, nodes)] #若无node 添加node字段

    
    #entities=[]
    #for node in nodes:
        # print(node)
        # print(node['_id'])
        #node['_id']=str(node['_id'])
        #entities.append(node)

    ret = {"total": len(nodes), "entities": nodes,
           "schema": {"name": "node", "properties": [{"name": "node"}], "collectionName": "node"}}

    # ret={"total":total,"entities":entities,"schema":{"name":nodes_node,"properties":[{"name":nodes_node}],"collectionName":nodesTableName}}

    
    return HttpResponse(json.dumps(ret, ensure_ascii=False))


def getTriples_vis(request):


    entityId = request.GET.get('entityId')
    entity=api.getOneNodeById(entityId)[NODE_NAME]
    
    edges=list(api.getEdgesByU(entity))
    
    res = []
    entities, triples = [], []
    

    #     res['entities']=[
    # //     {'_id': "5c1482c91a5ca12c94795c17",'_schema': { 'name': "node",
    # //       'properties':[{ 'name': 'node'}]},'node': "a1"},
    # //     {'_id': "5c0f701a9007052ca4016fec", '_schema': { 'name': "node",
    # //     'properties':[{ 'name': "node"}]},'node': "朱丽倩", },
    # //     {'_id': "5c00dae4e810192dec6b1342", '_schema': {'name': "node" ,
    # //     'properties':[{ 'name': "node"}]
    # //   },'node': "奥迪"}
    # //     ];

    # //   res['triples']=[
    # // {'_id': "5c14f56dd8af1c4f30fa2d69", 's': "5c0f6d5f9007052ca4016fea", 'p': "同学", 'o': "5c1482c91a5ca12c94795c17"},
    # // {'_id': "5c0f7029ba042e2ca4833129", 's': "5c0f6d5f9007052ca4016fea", 'p': "夫妻", 'o': "5c0f701a9007052ca4016fec"},
    # // {'_id': "5c1504dfd8af1c4f30fa2d6b", 's':"5c0f6d5f9007052ca4016fea", 'p': "购买", 'o': "5c00dae4e810192dec6b1342"}
    # //   ]
    for edge in edges:
        # p=edge['w']
        id = edge['_id']
        # p = edge['tp'] + '(' + edge['w'] + ')'
        p = args.PRINT_PREDICATE(edge)
        # sid = str(nodesTable.find_one({'node': edge['u']})['_id'])
        sid=api.getOneNode(edge[TRIPLE_COL[args.TRIPLE_S]])['_id']
        # o = nodesTable.find_one({'node': edge['v']})
        # o=api.getOneNode(edge['v'])
        oname = edge[TRIPLE_COL[args.TRIPLE_O]]

        #根据是否含href 来得到oname
        if TRIPLE_ARG[TRIPLE_COL[args.TRIPLE_O]]['node']==2:
            if oname.find('href')!=-1:
                om,oe=splitO(oname)
                oname=oe



        o = api.getOneNode(oname)
        if o is not None:
            oid = o['_id']
            print(sid, p, oid)  # 获取o_node
            onode = {'_id': oid, '_schema': {'name': "node", 'properties': [{'name': 'node'}]}, 'node': oname}
            entities.append(onode)
            triple = {'_id': id, 's': sid, 'p': p, 'o': oid}
            triples.append(triple)

    res = {'entities': entities, 'triples': triples}
    # print(res)
    return HttpResponse(json.dumps(res, ensure_ascii=False))
    # response.headers['Access-Control-Allow-Origin'] = '*'
    # return HttpResponse(jsonb.dumps(res))


def addEntity_vis(request):
    print('in addEntity')
    # requests.post('http://127.0.0.1:11111/api/v1/addEntity', data={'node':'adfadsfa'}) 可通过post forms获取
    # 	json.loads(request.data){"_type":"5c00d6ffe810192dec6b133d","node":"aaa"}
    # bottle restful
    # print(request.forms.items())

    entity =json.loads(str(request.body,encoding='utf-8'))['node']
    #print(entity)
    tmp=api.getOneNode(entity)
    
    if tmp is not None:
        print('entity repeat')
        
        return HttpResponse(json.dumps({'info': 'repeat'}))

    
    api.addNode(entity)
    
    _id=str(api.getOneNode(entity)['_id'])
    
    return HttpResponse(json.dumps({'entity': {'node': entity, '_id': _id}}))



def removeEntity_vis(request):
    # 前端传参只传了id 后期加上节点名
    id = json.loads(str(request.body,encoding='utf-8'))['id']
    return remove_entity(request, id)



def removeTriple_vis(request):
    # 前端传参只传了id 后期加上节点名
    id = json.loads(str(request.body,encoding='utf-8'))['id']
    
    api.deleteEdgeById(id)
    
    return HttpResponse('remove success')




def addTriple_vis(request):
    # 添加边之前一定已存在节点

    def _T(x):
        if 'node' not in x: x['node'] = x[NODE_NAME]
        return x

    t = json.loads(str(request.body,encoding='utf-8'))
    sid, oid = t['s'] , t['o']
    pp = t['p']#json
    #w =1

    #if not is_number(w):
    #    return HttpResponse(json.dumps({'info': 'w is not number'}))
    # s = nodesTable.find_one({'_id': ObjectId(sid)})['node']
    s = api.getOneNodeById(sid)[NODE_NAME]
    # o = nodesTable.find_one({'_id': ObjectId(oid)})['node']
    o = api.getOneNodeById(oid)[NODE_NAME]
    #print(s, p, o)
    # params_split=[s]
    # params_split.extend(pp.values())
    # params_split.append(o)
    # print(params_split)
    try:
        pp = json.loads(pp)
        pp[args.TRIPLE_COL[args.TRIPLE_S]] = s
        pp[args.TRIPLE_COL[args.TRIPLE_O]] = o
        params = [pp[key] for key in args.TRIPLE_COL]
    except:
        return HttpResponse(json.dumps({'info': 'wrong json'}))
    
    if api.getEdgeCount(params)!=0:
        
        return HttpResponse(json.dumps({'info': 'repeat'}))

    
    api.addEdge(params)
    edge=api.getOneEdge(params)
    edgeId = str(edge['_id'])

    #p = edge['tp'] + '(' + edge['w'] + ')'
    p = args.PRINT_PREDICATE(edge)
    redge = {'_id': edgeId, 's': sid, 'p': p, 'o': oid}
    #ret = {'triple': redge}
    # json.dumps(res, ensure_ascii = False)
    #return HttpResponse(json.dumps(ret))
    return HttpResponse(json.dumps({'triple': redge}, ensure_ascii=False))

##### schema op ###############################################################
def query_schema(request):
    print("query_schema" )


    field = SCHEMA_COL




    post=list(api.getAllSchemas())
    # print(318,list(post))


    ret=[{'field':field,'jsons':list(post)}]
    jsonStr = json.dumps(list(ret), ensure_ascii=False)
    return HttpResponse(jsonStr)


def remove_schema(request, nid):
    print("in  remove_schema")
    # edgesTable.delete_one({'_id': ObjectId(nid)})
    api.deleteSchemaById(nid)
    return HttpResponse("delete success")


def modify_schema(request, id):
    # o = o.replace("*****", "/")  # 将/恢复
    # print('in mdify')
    params = request.GET.get('params')
    #print(params)
    params = params.strip('\t').split('\t')
    #print(params)
    # if len(params) != len(args.TRIPLE_COL): return HttpResponse("Not correct")

    num = api.getSchemaCount(params)

    if num != 0:
        return HttpResponse("already exist")

    api.updateSchema(id, params)
    return HttpResponse("modify schema success")


def add_schema(request):
    print('in add schema')
    params = request.GET.get('params')
    params = params.strip('\t').split('\t')

    # 没有href的o,无需验证是否在nodes表中
    # o = o.replace("*****", "/")  # 将/恢复
    print(params)
    num = api.getSchemaCount(params)
    if num != 0:
        return HttpResponse("already exist")

    api.addSchema(params)
    # 新增一个edges，如果s不存在，也需要加入到nodes表中



    return HttpResponse("add")
