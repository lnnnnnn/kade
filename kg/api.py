from pymongo import MongoClient
from bson.objectid import ObjectId
from datetime import datetime
from . import args as args
import configparser
dbConfigFile="kg/db.ini"
cf = configparser.ConfigParser()
cf.read(dbConfigFile)



# DB_ARG=args.DB_ARG
# DB_NAME=DB_ARG['db_name']
# DB_HOST=DB_ARG['db_host']
# DB_PORT=DB_ARG['db_port']
# DB_USERNAME=DB_ARG['db_username']
# DB_PASSWORD=DB_ARG['db_password']

#数据库配置采用 db.ini
DB_NAME=cf['db']['DB_NAME']
DB_HOST=cf['db']['DB_HOST']
DB_PORT=cf['db']['DB_PORT']
DB_USERNAME=cf['db']['DB_USERNAME']
DB_PASSWORD=cf['db']['DB_PASSWORD']

CLIENT_URI = 'mongodb://%s:%s/%s' % (DB_HOST, DB_PORT, DB_NAME)

#从settings文件中获取数据库配置信息 并连接数据库
client = MongoClient(CLIENT_URI)
# client = MongoClient('mongodb://localhost:32017/')
# print(31,DB_USERNAME,DB_PASSWORD)
if DB_USERNAME is not None and DB_USERNAME != 'None' and DB_PASSWORD is not None and DB_PASSWORD != 'None':#远程服务器需认证 若不需用户名密码设为None
    client.admin.authenticate(DB_USERNAME,DB_PASSWORD,mechanism='SCRAM-SHA-1')
db = client[DB_NAME]


# 获取配置文件中的表名、字段名

userTableName = args.TABLENAME_ARG['usertablename']
nodesTableName =args.TABLENAME_ARG['nodestablename']
edgesTableName = args.TABLENAME_ARG['edgestablename']
schemaTableName=args.TABLENAME_ARG['schematablename']
# [user]
user_username = args.USER_ARG['user_username']
user_password = args.USER_ARG['user_password']

#仅仅entity表需要区分id的 oid str类型
# if not args.USE_OBJECTID: ObjectId = lambda x:x

nodes_node=args.ENTITY_ARG['entity_name']
# from args import TRIPLE_ARG

TRIPLE_ARG=args.TRIPLE_ARG
MENT2ENT_ARG=args.MENT2ENT_ARG
SCHEMA_COL=args.SCHEMA_COL
userTable = db[userTableName]
edgesTable = db[edgesTableName]
nodesTable = db[nodesTableName]
schemaTable=db[schemaTableName]
ment2entTable=None
if MENT2ENT_ARG!=None:
    ment2entTableName = args.TABLENAME_ARG['ment2enttablename']
    ment2entTable=db[ment2entTableName]
    MENT2ENT_MENTION_NAME, MENT2ENT_ENTITY_NAME = args.MENT2ENT_COL

SNAME = args.TRIPLE_COL[0]   #获取s的字段名
#SNAME=list(TRIPLE_ARG.keys())[0]#获取s的字段名
# def getEdgeCount(u,v,w,tp):
#     cnt=edgesTable.find({edges_u: u, edges_v: v, edges_w: w, edges_tp: tp}).count()
#     return cnt

#HAS_HREF=False
HAS_HREF = (2 in [x['node'] for x in TRIPLE_ARG.values()])
###################      读取db.ini中的内容 用于展示可视化+ 配置     ######################################
# [edges]#
# edges_u = cf['edges']['edges_u']
# edges_v = cf['edges']['edges_v']
# edges_w = cf['edges']['edges_w']
# edges_tp = cf['edges']['edges_tp']
# edges_timestamp = cf['edges']['edges_timestamp']
# edges_editable = cf['edges']['edges_editable']

# [nodes]
# nodes_id = cf['nodes']['nodes_id']
# nodes_node = cf['nodes']['nodes_node']
# nodes_timestamp=cf['nodes']['nodes_timestamp']
# nodes_editable = cf['nodes']['nodes_editable']

# DB_NAME=cf['db']['DB_NAME']
# DB_HOST=cf['db']['DB_HOST']
# DB_PORT=cf['db']['DB_PORT']
# DB_USERNAME=cf['db']['DB_USERNAME']
# DB_PASSWORD=cf['db']['DB_PASSWORD']

# tableName
# userTableName = cf['tableName']['userTableName']
# nodesTableName = cf['tableName']['nodesTableName']
# edgesTableName = cf['tableName']['edgesTableName']
# ment2entTableName=cf['tableName']['ment2entTableName']

# user_username = cf['user']['user_username']
# user_password = cf['user']['user_password']

#########################################################


#def get_MENT2ENT_ENTITY_NAME():
#    if MENT2ENT_ARG!=None:
#        for key in MENT2ENT_ARG:
#            if MENT2ENT_ARG[key]['node'] == 1:
#                return key
#    else :
#        return None

#MENT2ENT_ENTITY_NAME=get_MENT2ENT_ENTITY_NAME()
#MENT2ENT_MENTION_NAME = 'm' #待配置

#def getQuery(params):
#    print(params)
#    query = {}
#    ind = 0
#    for key in TRIPLE_ARG:
#        query[key] = params[ind]
#        ind += 1
#    return query

def getQuery(params):
    return {key:pp for pp, key in zip(params, args.TRIPLE_COL)}
	
#def getQuery_ment2ent(params):
#    query = {}
#    ind = 0
#    for key in MENT2ENT_ARG:
#        query[key] = params[ind]
#        ind += 1
#    return query

def getQuery_ment2ent(params):
    return {key:pp for pp, key in zip(params, args.MENT2ENT_COL)}
	
#def calcHref():
#    global HAS_HREF
#    for key in TRIPLE_ARG:
#        if TRIPLE_ARG[key]['node']==2:
#            HAS_HREF=True

#calcHref()

def transferParams(params):
    if len(params)==3:
        s, p, om = params
        oe=om
    else:
        s,p, om, oe = params
        o = '<a href="{}">{}</a>'.format(oe, om)
        params = (s, p, o)
    return params

def getEdgeCount(params):
    if HAS_HREF:
       params=transferParams(params)
    query=getQuery(params)
    # print(query)

    cnt=edgesTable.find(query).count()
    return cnt

def deleteEdgeById(nid):
    edgesTable.delete_one({'_id': ObjectId(nid)})
#用于更新 不必将id转为str
def getEdgeById(id):
    edge = edgesTable.find_one({'_id': ObjectId(id)})
    return edge

def updateEdge( id, params):
    print('in update edge')
    if HAS_HREF:
       params=transferParams(params)
    edge = getEdgeById(id)

    #ind = 0
    #for key in TRIPLE_ARG:
    #    edge[key] = params[ind]
    #    ind += 1
    for pp, key in zip(params, args.TRIPLE_COL): edge[key] = pp
    print(edge)
    edgesTable.update_one({'_id': ObjectId(id)}, {'$set': edge})

def addEdge(params):
    #print(params)
    #print('in addEdge,hashref',HAS_HREF)
    if HAS_HREF:
       params=transferParams(params)
    print(params)
    query=getQuery(params)

    # edgesTable.insert({edges_u: u, edges_v: v, edges_w: w, edges_tp: tp})
    edgesTable.insert(query)
def getOneEdge(params):
    return edgesTable.find_one(getQuery(params))
def getEdgesByU(s):
    # return edgesTable.find({SNAME: s})
    return map(T, edgesTable.find({SNAME: s}))
def deleteEdgesByNode(k,v):
    # print(k,v)
    edgesTable.delete_many({k: v})

def deleteMent2entByNode(k,v):
    ment2entTable.delete_many({k: v})



def getAllEdgesCount():
    return edgesTable.find().count()
####################################     ment2ent    ######################################
def getMent2entsByEntity(s):
    return map(T,ment2entTable.find({MENT2ENT_ENTITY_NAME:s}))
def getMent2entsByMention(s):
    return map(T, ment2entTable.find({MENT2ENT_MENTION_NAME:s}))
def getMent2entCount(params):
    query = getQuery_ment2ent(params)
    # print(query)

    cnt = ment2entTable.find(query).count()
    return cnt
def addMent2ent(params):
    query = getQuery_ment2ent(params)

    # edgesTable.insert({edges_u: u, edges_v: v, edges_w: w, edges_tp: tp})
    ment2entTable.insert(query)

def getMent2entById(id):
    return ment2entTable.find_one({'_id': ObjectId(id)})

def updateMent2ent(id,params):
    me = getMent2entById(id)
    print(id,me)

    #ind = 0
    #for key in MENT2ENT_ARG:
    #    me[key] = params[ind]
    #    ind += 1
    for pp, key in zip(params, args.MENT2ENT_COL): me[key] = pp
    ment2entTable.update_one({'_id': ObjectId(id)}, {'$set': me})

def deleteMent2entById(id):
    ment2entTable.delete_one({'_id': ObjectId(id)})
##########################################################################

def T(xx):
    if xx is None: return xx
    xx['_id'] = str(xx['_id'])
    for k, v in xx.items():
        if isinstance(v, datetime): xx[k] = v.timestamp()
    return xx

def getTopNodes(count):
    # return nodesTable.find().limit(count)
    # return map(T, nodesTable.find().limit(count))
    return map(T, nodesTable.find().limit(count))

def getNodeCount(u):
    return nodesTable.find({nodes_node: u}).count()

def addNode(u):
    nodesTable.insert({nodes_node: u})

def getOneNode(s):
    return T(nodesTable.find_one({nodes_node: s}))

def getOneNodeById(id):

    if not args.ENTITIES_USE_OBJECTID:
        return T(nodesTable.find_one({'_id': id}))
        # ObjectId = lambda x: x
    return T(nodesTable.find_one({'_id': ObjectId(id)}))
def getBlurNodes(s):
    # {node:/^asdff/}
    # return map(T,nodesTable.find({nodes_node: s}))
    return map(T,nodesTable.find({nodes_node: {'$regex': s}}).limit(5))

def deleteNodeByName(s):
    nodesTable.delete_one({nodes_node:s })
def deleteNodeById(id):
    if not args.ENTITIES_USE_OBJECTID:
        nodesTable.delete_one({'_id': id})
        return
        #ObjectId = lambda x: x
    nodesTable.delete_one({'_id':ObjectId(id) })

def getAllNodesCount():
    return nodesTable.find().count()


def getNodesAdvice(query, count=5):
    advs = nodesTable.find_one({nodes_node:query})
    advs = [] if advs is None else [advs]
    blur = list(nodesTable.find({nodes_node: {'$regex': '^' + query}}).limit(count))
    blur = [x for x in blur if x['_id'] not in {x['_id'] for x in advs}]
    advs.extend(blur)
    return map(T, advs[:count])

#def getNodesAdvice(query,count=5):
#   return map(T,nodesTable.find({nodes_node: {'$regex': '^' + query}}).limit(5))
###########################################################################

def getUserCount(user,pwd):
    return userTable.find({user_username: user, user_password: pwd}).count()

def getAllUserCount():
    return userTable.find().count()

####################   vis   #######################################
# def deleteEdgesByU(u):
#     edgesTable.delete_many({edges_u: u})
#
# def deleteEdgesByV(v):
#     edgesTable.delete_many({edges_v: v})

def getAllSchemas():
    return map(T, schemaTable.find())
def deleteSchemaById(nid):
    schemaTable.delete_one({"_id":ObjectId(nid)})
def getSchemaById(id):
    return schemaTable.find_one({'_id': ObjectId(id)})

def updateSchema(id,params):
    sc = getSchemaById(id)
    print(id,sc)
    # cols=list(SCHEMA_ARG.values())
    cols=SCHEMA_COL
    for pp, key in zip(params, cols): sc[key] = pp
    print(sc)
    schemaTable.update_one({'_id': ObjectId(id)}, {'$set': sc})
def addSchema(params):
    #cols = list(SCHEMA_ARG.values())
    cols = SCHEMA_COL
    query={key:pp for pp, key in zip(params,cols)}


    schemaTable.insert(query)
def getSchemaCount(params):
    # cols = list(SCHEMA_ARG.values())
    cols = SCHEMA_COL
    query = {key: pp for pp, key in zip(params, cols)}
    cnt = schemaTable.find(query).count()
    return cnt


