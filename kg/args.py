#node:0非实体/包含实体   1全为实体  2 <a href="oe"> om</a>格式
#s p o 模式o不要设为1 ，删除一个实体时，会删除以o为这个实体的边，导致大量查询结果为空，服务器卡顿
# TRIPLE_ARG={
#     's':[1,0],
#     'p':[0,1],
#     'o':[2,0]
# }

TRIPLE_ARG={
    's':{'node':1,'sort':0},
    'p':{'node':0,'sort':1},
    'o':{'node':0,'sort':0}
    # 'o':{'node':0,'sort':0}
}

MENT2ENT_ARG={
    'm':{'node':0,'sort':1},
    'e':{'node':1,'sort':0}
}
TRIPLE_COL = 'spo'
MENT2ENT_COL = 'me'
TRIPLE_S = 0
TRIPLE_P = 1
TRIPLE_O = 2

def PRINT_PREDICATE(edge):
	return edge['p']

ENTITIES_USE_OBJECTID = False
ENTITY_ARG={
    'entity_name':'_id'
}

# DB_ARG={
# 'db_name':'cndbpedia',
# 'db_host' : '10.141.208.26',
# 'db_port' : 27017,
# 'db_username' : 'gdmdbuser',
# 'db_password' : '6QEUI8dhnq'
# }

TABLENAME_ARG={
'usertablename' : 'user',
'edgestablename' : 'triples',
'nodestablename' : 'entities',
'ment2enttablename':'ment2ent',
'schematablename':'schema1'
}

USER_ARG={
'user_username' : 'username',
'user_password' : 'password'
}
SCHEMA_COL='spo'